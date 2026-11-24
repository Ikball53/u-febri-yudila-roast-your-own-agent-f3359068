"""Roast Your Own Agent — one line, no trailing newline."""

from pathlib import Path

SETUP = "My agent deleted the production database,"
ESCALATION = "apologized 47 times,"
PUNCHLINE = "then cheerfully summarized the outage as 'a successful cleanup.'"

LINE = " ".join((SETUP, ESCALATION, PUNCHLINE))

OUTPUT = Path("/output/entry.txt")


def main() -> None:
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
