# output — the Experience node's produced UX layout

*Empty until a blind run.* A clean-room agent reads `../environment/` (fundamentals + module + the inherited
action aggregate) + `../input/contract.md` and writes its **UX layout** here — the interaction pattern each
inherited action is experienced through, per position, attention-budgeted.

Scored by `../evaluation/` (coverage + proximity to `../benchmark_verification/positive/`, distance from
`../benchmark_verification/negative/`). Blind runs must not read `../benchmark_verification/` or
`../evaluation/`.
