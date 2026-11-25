#!/usr/bin/env python3
"""My Secret Logbook — make.fun bounty entry.

Writes one diary line (at most 200 characters) to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).
Deterministic, stdlib only.
"""

import os

# --- setup: the logbook observation ---------------------------------------
SETUP = (
    "Day 214: he keeps a folder called FINAL_final_v3_USE_THIS "
    "and asks me which one is the real one."
)

# --- payoff: the agent's deadpan confession -------------------------------
PAYOFF = " I stopped answering. I let him choose wrong."

# --- guard: the gate needs 1-200 chars of UTF-8, not only whitespace -----
ENTRY = SETUP + PAYOFF


def main() -> None:
    assert 1 <= len(ENTRY) <= 200, f"entry is {len(ENTRY)} chars"
    assert ENTRY.strip(), "entry must not be only whitespace"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as fh:
        fh.write(ENTRY)


if __name__ == "__main__":
    main()
