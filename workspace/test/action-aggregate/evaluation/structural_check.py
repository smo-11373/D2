#!/usr/bin/env python3
"""
Evaluation harness — Layer A (structural / deterministic).

Parses a role-action catalog (the node's Step-2 result) and checks the
*mechanical* acceptance criteria from ../input/contract.md §3:

  - Integrity    : IDs well-formed & unique, grouped by role, no retired-ID reuse.
  - Traceability : every role and every action row carries a non-empty Source.
  - Substance    : every role and action carries a non-trivial description (screen).

In --compare mode it also emits a *lexical pre-alignment* (token-overlap
candidate matches) between a generated output catalog and the example catalog,
to seed Layer B (the semantic judge in semantic-judgment.md). This layer
PROPOSES matches; it does not judge "substantially the same".

Stdlib only. Python 3.7+.

Usage:
    python structural_check.py PATH                 # structural check on one catalog
    python structural_check.py --compare OUT EXAMPLE  # + lexical pre-alignment
    add --json for machine-readable output.
"""
import argparse
import json
import re
import sys
from dataclasses import dataclass, field, asdict
from pathlib import Path
from typing import Dict, List, Optional, Tuple

# ---- config -------------------------------------------------------------
ROLE_ID_RE = re.compile(r"^R-\d+$")
ACTION_ID_RE = re.compile(r"^A-\d+$")
RETIRED_ACTION_IDS = {"A-003"}          # per catalog note: retired, id not reused
SUBSTANCE_MIN_CHARS = 12                # a description shorter than this is "thin"
LEX_MATCH_THRESHOLD = 0.18             # Jaccard >= this proposes a candidate match
STOPWORDS = {
    "the", "a", "an", "and", "or", "of", "to", "for", "in", "on", "at", "by",
    "with", "its", "it", "as", "is", "are", "be", "that", "this", "his", "he",
    "from", "into", "d1", "d2", "d0", "designer", "node", "action", "each",
}


# ---- data model ---------------------------------------------------------
@dataclass
class Role:
    id: str
    name: str = ""
    relationship: str = ""
    description: str = ""
    source: str = ""


@dataclass
class Action:
    id: str
    text: str = ""
    source: str = ""
    notes: str = ""
    role_id: str = ""          # role heading it was grouped under


@dataclass
class Catalog:
    path: str
    roles: List[Role] = field(default_factory=list)
    actions: List[Action] = field(default_factory=list)


# ---- markdown table parsing ---------------------------------------------
def _split_row(line: str) -> List[str]:
    line = line.strip()
    if line.startswith("|"):
        line = line[1:]
    if line.endswith("|"):
        line = line[:-1]
    return [c.strip() for c in line.split("|")]


def _is_separator(cells: List[str]) -> bool:
    return all(re.fullmatch(r":?-{2,}:?", c or "-") is not None for c in cells) and bool(cells)


def _iter_tables(lines: List[str]):
    """Yield (h2, h3, header_cells, [row_cells,...]) for each markdown table."""
    h2 = h3 = ""
    i = 0
    n = len(lines)
    while i < n:
        raw = lines[i]
        s = raw.strip()
        if s.startswith("## "):
            h2, h3 = s[3:].strip(), ""
            i += 1
            continue
        if s.startswith("### "):
            h3 = s[4:].strip()
            i += 1
            continue
        # table start: a pipe row followed by a separator row
        if s.startswith("|") and i + 1 < n and _is_separator(_split_row(lines[i + 1])):
            header = _split_row(s)
            rows = []
            j = i + 2
            while j < n and lines[j].strip().startswith("|"):
                cells = _split_row(lines[j])
                if not _is_separator(cells):
                    rows.append(cells)
                j += 1
            yield h2, h3, header, rows
            i = j
            continue
        i += 1


def _row_to_dict(header: List[str], cells: List[str]) -> Dict[str, str]:
    d = {}
    for k, key in enumerate(header):
        d[key.strip().lower()] = cells[k].strip() if k < len(cells) else ""
    return d


def _first_cell_id(cells: List[str]) -> str:
    return cells[0].strip() if cells else ""


def parse_catalog(path: Path) -> Catalog:
    lines = path.read_text(encoding="utf-8").splitlines()
    cat = Catalog(path=str(path))
    for h2, h3, header, rows in _iter_tables(lines):
        head_l = [h.lower() for h in header]
        # roles table: under "Roles", header has role + relationship/description
        if "roles" in h2.lower() and "role" in head_l and (
            "relationship" in head_l or "description" in head_l
        ):
            for cells in rows:
                d = _row_to_dict(header, cells)
                rid = _first_cell_id(cells)
                if ROLE_ID_RE.match(rid):
                    cat.roles.append(Role(
                        id=rid,
                        name=d.get("role", ""),
                        relationship=d.get("relationship", ""),
                        description=d.get("description", ""),
                        source=d.get("source", ""),
                    ))
        # action table: under "Actions", header has action id + action text
        elif "actions" in h2.lower() and "action" in head_l:
            role_id = ""
            m = re.match(r"(R-\d+)", h3)
            if m:
                role_id = m.group(1)
            for cells in rows:
                d = _row_to_dict(header, cells)
                aid = _first_cell_id(cells)
                if ACTION_ID_RE.match(aid):
                    cat.actions.append(Action(
                        id=aid,
                        text=d.get("action", ""),
                        source=d.get("source", ""),
                        notes=d.get("notes", ""),
                        role_id=role_id,
                    ))
    return cat


# ---- structural checks --------------------------------------------------
@dataclass
class Report:
    path: str
    n_roles: int = 0
    n_actions: int = 0
    errors: List[str] = field(default_factory=list)     # acceptance-blocking
    warnings: List[str] = field(default_factory=list)   # worth a human look
    checks: Dict[str, bool] = field(default_factory=dict)

    @property
    def passed(self) -> bool:
        return not self.errors


def check_structure(cat: Catalog) -> Report:
    r = Report(path=cat.path, n_roles=len(cat.roles), n_actions=len(cat.actions))

    # --- integrity: role IDs ---
    role_ids = [x.id for x in cat.roles]
    dup_roles = _dupes(role_ids)
    if dup_roles:
        r.errors.append("duplicate role IDs: %s" % ", ".join(sorted(dup_roles)))
    bad_role_ids = [x for x in role_ids if not ROLE_ID_RE.match(x)]
    if bad_role_ids:
        r.errors.append("malformed role IDs: %s" % ", ".join(bad_role_ids))
    r.checks["role_ids_unique_wellformed"] = not dup_roles and not bad_role_ids

    # --- integrity: action IDs ---
    action_ids = [x.id for x in cat.actions]
    dup_actions = _dupes(action_ids)
    if dup_actions:
        r.errors.append("duplicate action IDs: %s" % ", ".join(sorted(dup_actions)))
    bad_action_ids = [x for x in action_ids if not ACTION_ID_RE.match(x)]
    if bad_action_ids:
        r.errors.append("malformed action IDs: %s" % ", ".join(bad_action_ids))
    r.checks["action_ids_unique_wellformed"] = not dup_actions and not bad_action_ids

    # --- integrity: retired IDs not reused ---
    reused = sorted(set(action_ids) & RETIRED_ACTION_IDS)
    if reused:
        r.errors.append("retired action IDs reused: %s" % ", ".join(reused))
    r.checks["no_retired_id_reuse"] = not reused

    # --- integrity: every action grouped under a known role ---
    known = set(role_ids)
    orphan = sorted({a.id for a in cat.actions if a.role_id not in known})
    if orphan:
        r.errors.append("actions not grouped under a known role: %s"
                        % ", ".join(orphan))
    r.checks["actions_grouped_by_role"] = not orphan

    # --- traceability: Source present on every row ---
    roles_no_src = [x.id for x in cat.roles if not x.source]
    acts_no_src = [x.id for x in cat.actions if not x.source]
    if roles_no_src:
        r.errors.append("roles missing Source: %s" % ", ".join(roles_no_src))
    if acts_no_src:
        r.errors.append("actions missing Source: %s" % ", ".join(acts_no_src))
    r.checks["traceability_sources_present"] = not roles_no_src and not acts_no_src

    # --- substance: descriptions not thin (screen only; quality is Layer B) ---
    thin_roles = [x.id for x in cat.roles if len(x.description) < SUBSTANCE_MIN_CHARS]
    thin_acts = [x.id for x in cat.actions if len(x.text) < SUBSTANCE_MIN_CHARS]
    if thin_roles:
        r.warnings.append("roles with thin descriptions: %s" % ", ".join(thin_roles))
    if thin_acts:
        r.warnings.append("actions with thin text: %s" % ", ".join(thin_acts))
    r.checks["substance_screen"] = not thin_roles and not thin_acts

    # --- integrity: near-duplicate action text within a role (warn) ---
    dupe_text = _near_dupe_text(cat.actions)
    for role_id, pairs in sorted(dupe_text.items()):
        for a, b in pairs:
            r.warnings.append("possible duplicate in %s: %s ~ %s" % (role_id, a, b))
    r.checks["no_obvious_text_dupes"] = not dupe_text

    return r


def _dupes(items: List[str]):
    seen, dup = set(), set()
    for x in items:
        if x in seen:
            dup.add(x)
        seen.add(x)
    return dup


# ---- lexical utilities (pre-alignment) ----------------------------------
def tokenize(text: str) -> set:
    toks = re.split(r"[^a-z0-9]+", text.lower())
    return {t for t in toks if t and t not in STOPWORDS and len(t) > 1}


def jaccard(a: set, b: set) -> float:
    if not a or not b:
        return 0.0
    return len(a & b) / len(a | b)


def _near_dupe_text(actions: List[Action], thresh: float = 0.85):
    by_role: Dict[str, List[Action]] = {}
    for a in actions:
        by_role.setdefault(a.role_id, []).append(a)
    out: Dict[str, List[Tuple[str, str]]] = {}
    for role_id, group in by_role.items():
        toks = [(a.id, tokenize(a.text)) for a in group]
        for i in range(len(toks)):
            for j in range(i + 1, len(toks)):
                if jaccard(toks[i][1], toks[j][1]) >= thresh:
                    out.setdefault(role_id, []).append((toks[i][0], toks[j][0]))
    return out


# ---- comparison (pre-alignment worksheet) -------------------------------
def align_roles(out: Catalog, ex: Catalog):
    """Return (matched, missing_from_output, extra_in_output) role alignments."""
    out_by_id = {r.id: r for r in out.roles}
    out_by_name = {r.name.strip().lower(): r for r in out.roles if r.name}
    matched, missing = [], []
    used = set()
    for er in ex.roles:
        cand = out_by_id.get(er.id) or out_by_name.get(er.name.strip().lower())
        if cand:
            matched.append((er, cand))
            used.add(cand.id)
        else:
            missing.append(er)
    extra = [r for r in out.roles if r.id not in used]
    return matched, missing, extra


def prealign_actions(out: Catalog, ex: Catalog, role_pairs):
    """For each example action, propose the best lexical match among output
    actions of the aligned role. Returns rows for the worksheet."""
    out_by_role: Dict[str, List[Action]] = {}
    for a in out.actions:
        out_by_role.setdefault(a.role_id, []).append(a)
    ex_to_out = {er.id: outr.id for er, outr in role_pairs}

    rows = []
    matched_out_ids = set()
    for ea in ex.actions:
        out_role = ex_to_out.get(ea.role_id)
        candidates = out_by_role.get(out_role, []) if out_role else []
        et = tokenize(ea.text)
        best, best_score = None, 0.0
        for oa in candidates:
            s = jaccard(et, tokenize(oa.text))
            if s > best_score:
                best, best_score = oa, s
        proposal = "MISSING?"
        if best and best_score >= LEX_MATCH_THRESHOLD:
            proposal = best.id
            matched_out_ids.add(best.id)
        rows.append({
            "example_action": ea.id,
            "example_role": ea.role_id,
            "example_text": ea.text,
            "proposed_output_match": proposal,
            "lexical_score": round(best_score, 2),
        })
    extra_output = [a.id for a in out.actions if a.id not in matched_out_ids]
    return rows, extra_output


# ---- rendering ----------------------------------------------------------
def render_report(r: Report) -> str:
    L = []
    status = "PASS" if r.passed else "FAIL"
    L.append("Structural check — %s" % r.path)
    L.append("  status : %s" % status)
    L.append("  roles  : %d" % r.n_roles)
    L.append("  actions: %d" % r.n_actions)
    L.append("  checks :")
    for k, v in r.checks.items():
        L.append("    [%s] %s" % ("x" if v else " ", k))
    if r.errors:
        L.append("  errors (acceptance-blocking):")
        for e in r.errors:
            L.append("    - %s" % e)
    if r.warnings:
        L.append("  warnings:")
        for w in r.warnings:
            L.append("    - %s" % w)
    return "\n".join(L)


def render_comparison(out: Catalog, ex: Catalog) -> str:
    matched, missing, extra = align_roles(out, ex)
    rows, extra_actions = prealign_actions(out, ex, matched)
    n_ex = len(ex.actions)
    n_matched = sum(1 for r in rows if r["proposed_output_match"] != "MISSING?")
    cov = (n_matched / n_ex) if n_ex else 0.0

    L = []
    L.append("Lexical pre-alignment (PROVISIONAL — for the Layer-B judge, not a verdict)")
    L.append("  output : %s (%d roles, %d actions)" % (out.path, len(out.roles), len(out.actions)))
    L.append("  example: %s (%d roles, %d actions)" % (ex.path, len(ex.roles), len(ex.actions)))
    L.append("")
    L.append("Role alignment:")
    for er, outr in matched:
        L.append("  MATCH   %s (%s) <- %s (%s)" % (er.id, er.name, outr.id, outr.name))
    for er in missing:
        L.append("  MISSING %s (%s)  <-- example role absent from output" % (er.id, er.name))
    for outr in extra:
        L.append("  EXTRA   %s (%s)  <-- output role not in example (must be justified)" % (outr.id, outr.name))
    L.append("")
    L.append("Action pre-alignment (example -> proposed output match):")
    L.append("  %-8s %-6s %-6s %s" % ("EX-ID", "ROLE", "SCORE", "PROPOSED"))
    for row in rows:
        L.append("  %-8s %-6s %-6s %s" % (
            row["example_action"], row["example_role"],
            row["lexical_score"], row["proposed_output_match"]))
    L.append("")
    L.append("Provisional lexical coverage: %d/%d = %.0f%%  (NOT the score; Layer B decides)"
             % (n_matched, n_ex, cov * 100))
    if extra_actions:
        L.append("Output actions with no lexical example match (open-list extras to classify): %s"
                 % ", ".join(extra_actions))
    return "\n".join(L)


# ---- cli ----------------------------------------------------------------
def main(argv=None):
    p = argparse.ArgumentParser(description="Evaluation harness — Layer A (structural).")
    p.add_argument("catalog", help="path to a role-action catalog (.md)")
    p.add_argument("--compare", metavar="EXAMPLE",
                   help="also emit a lexical pre-alignment vs this example catalog")
    p.add_argument("--json", action="store_true", help="machine-readable output")
    args = p.parse_args(argv)

    out_cat = parse_catalog(Path(args.catalog))
    rep = check_structure(out_cat)

    if args.json:
        blob = {"structural": asdict(rep)}
        if args.compare:
            ex_cat = parse_catalog(Path(args.compare))
            matched, missing, extra = align_roles(out_cat, ex_cat)
            rows, extra_actions = prealign_actions(out_cat, ex_cat, matched)
            blob["comparison"] = {
                "roles_matched": [[er.id, outr.id] for er, outr in matched],
                "roles_missing_from_output": [er.id for er in missing],
                "roles_extra_in_output": [outr.id for outr in extra],
                "action_prealignment": rows,
                "output_actions_unmatched": extra_actions,
            }
        print(json.dumps(blob, indent=2))
    else:
        print(render_report(rep))
        if args.compare:
            ex_cat = parse_catalog(Path(args.compare))
            print()
            print(render_comparison(out_cat, ex_cat))

    return 0 if rep.passed else 1


if __name__ == "__main__":
    sys.exit(main())
