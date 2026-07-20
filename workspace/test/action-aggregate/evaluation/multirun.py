#!/usr/bin/env python3
"""
Multi-run aggregation harness — Layer A over N blind runs of ONE module version.

Runs the structural check + lexical pre-alignment on each of N output catalogs against the
fixed example, and aggregates what a single run cannot show:

  - role / action count distribution + structural pass rate
  - per-example-action LEXICAL hit-count across runs -> UNION / INTERSECTION / NEVER sets
  - UNION coverage    = the derivable ceiling the version reaches *across* runs
                        (closes subtle-but-derivable items some runs get and others miss)
  - INTERSECTION      = the stable core every run reaches
  - run-to-run SPREAD = the noise band; a version-to-version delta is only real if it
                        exceeds this spread

Lexical only (Layer A) — it UNDER-states true coverage (paraphrase scores low); a semantic
Σmatch still needs a Layer-B judge. This tool bounds and seeds that pass, and — crucially —
quantifies the noise so deltas become attributable. Stdlib only; reuses structural_check.py.

Usage:
    python evaluation/multirun.py EXAMPLE RUN1 RUN2 [RUN3 ...]
    python evaluation/multirun.py --json EXAMPLE RUN1 RUN2 ...
"""
import sys
import json
import statistics
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import structural_check as sc  # noqa: E402


def analyze_run(path, ex):
    out = sc.parse_catalog(Path(path))
    rep = sc.check_structure(out)
    matched, _missing, _extra = sc.align_roles(out, ex)
    rows, _extra_actions = sc.prealign_actions(out, ex, matched)
    matched_ex = {r["example_action"] for r in rows
                  if r["proposed_output_match"] != "MISSING?"}
    return {
        "path": path,
        "roles": rep.n_roles,
        "actions": rep.n_actions,
        "structural_pass": rep.passed,
        "matched_example_actions": matched_ex,
        "lexical_cov": len(matched_ex),
    }


def aggregate(example_path, run_paths):
    ex = sc.parse_catalog(Path(example_path))
    ex_ids = [a.id for a in ex.actions]
    n_ex = len(ex_ids)
    runs = [analyze_run(p, ex) for p in run_paths]
    N = len(runs)

    hit = {aid: 0 for aid in ex_ids}
    for r in runs:
        for aid in r["matched_example_actions"]:
            hit[aid] += 1
    union = [a for a in ex_ids if hit[a] >= 1]
    inter = [a for a in ex_ids if hit[a] == N]
    never = [a for a in ex_ids if hit[a] == 0]

    rc = [r["roles"] for r in runs]
    ac = [r["actions"] for r in runs]
    lc = [r["lexical_cov"] for r in runs]

    def band(xs):
        return {"min": min(xs), "max": max(xs), "mean": round(statistics.mean(xs), 2)}

    return runs, {
        "n_runs": N, "n_example_actions": n_ex, "n_example_roles": len(ex.roles),
        "roles": band(rc), "actions": band(ac),
        "structural_pass_rate": round(sum(1 for r in runs if r["structural_pass"]) / N, 2),
        "lexical_cov_per_run": [round(c / n_ex, 3) for c in lc],
        "lexical_cov_mean": round(statistics.mean(lc) / n_ex, 3),
        "lexical_cov_spread": round((max(lc) - min(lc)) / n_ex, 3),
        "union_coverage": round(len(union) / n_ex, 3),
        "intersection_coverage": round(len(inter) / n_ex, 3),
        "never_matched": never,
    }


def render(runs, agg):
    n_ex = agg["n_example_actions"]
    L = ["Multi-run aggregate — %d runs vs example (%d actions, %d roles)"
         % (agg["n_runs"], n_ex, agg["n_example_roles"])]
    for r in runs:
        p = Path(r["path"])
        L.append("  %-28s roles=%d actions=%d structural=%s lexcov=%.2f" % (
            p.parent.name + "/" + p.name, r["roles"], r["actions"],
            "PASS" if r["structural_pass"] else "FAIL", r["lexical_cov"] / n_ex))
    L += ["",
          "  roles   : %s" % agg["roles"],
          "  actions : %s" % agg["actions"],
          "  structural pass rate : %.0f%%" % (agg["structural_pass_rate"] * 100),
          "",
          "  LEXICAL coverage (Layer A only — Layer B lifts these):",
          "    per run   : %s" % agg["lexical_cov_per_run"],
          "    mean      : %.2f    spread(max-min): %.2f   <- the NOISE BAND"
          % (agg["lexical_cov_mean"], agg["lexical_cov_spread"]),
          "    UNION     : %.2f    <- derivable ceiling reached across %d runs"
          % (agg["union_coverage"], agg["n_runs"]),
          "    INTERSECT : %.2f    <- reached by EVERY run (stable core)"
          % agg["intersection_coverage"],
          "",
          "  Example actions NEVER lexically matched (candidate hard-misses -> judge): %s"
          % (", ".join(agg["never_matched"]) if agg["never_matched"] else "none")]
    return "\n".join(L)


def main(argv=None):
    argv = list(sys.argv[1:] if argv is None else argv)
    as_json = False
    if argv and argv[0] == "--json":
        as_json = True
        argv = argv[1:]
    if len(argv) < 2:
        print("usage: python evaluation/multirun.py [--json] EXAMPLE RUN1 [RUN2 ...]")
        return 2
    runs, agg = aggregate(argv[0], argv[1:])
    print(json.dumps(agg, indent=2) if as_json else render(runs, agg))
    return 0


if __name__ == "__main__":
    sys.exit(main())
