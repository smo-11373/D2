# D2 Project

Design work for **D2**, organized as phased design artifacts plus a working Obsidian vault.

## Layout

- `artifact/` — source design material
  - `*.pdf` — phased design docs (Phase 1 Foundational Framing → Phase 6 items).
  - `D2_obsidian_vault/D2_obsedian/` — **the Obsidian vault**. Notes live here as
    Markdown (`.md`). Read and edit these directly; wiki-links (`[[Note Name]]`)
    resolve within this vault folder.

## How this project is used

- **Phone is the primary interface.** Most sessions happen from Claude Code on the
  web/mobile against the GitHub repo. Keep changes committed so they reach the phone.
- **Desktop (this CLI) stays in sync via git.** Always `git pull` at the start of a
  desktop session and `git push` (or commit) at the end so the phone sees your work.
- **Git is the sync mechanism**, not just version control. Small, frequent commits
  keep phone and desktop from diverging.

## Working conventions

- Prefer editing the Obsidian `.md` notes over the PDFs (PDFs are read-only source).
- When starting work, `git pull --rebase` first. When done, commit with a clear
  message describing the design change.
- `.obsidian/workspace.json` records per-device UI state and changes constantly.
  It is currently tracked; if it causes merge conflicts across devices, add it to
  `.gitignore` (there are commented-out lines ready for this).
