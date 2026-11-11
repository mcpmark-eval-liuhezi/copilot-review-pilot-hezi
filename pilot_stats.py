#!/usr/bin/env python3
"""Pilot example script for the Copilot code review demo.

Computes basic stats over a tiny in-memory dataset so we can show
Copilot review comments on a real PR diff.
"""


def main() -> None:
    data = [
        {"name": "file_a.py", "bytes": 1024, "lines": 42},
        {"name": "file_b.py", "bytes": 2048, "lines": 87},
        {"name": "readme.md", "bytes": 512, "lines": 15},
    ]

    total_bytes = sum(entry["bytes"] for entry in data)
    total_lines = sum(entry["lines"] for entry in data)

    print(f"Files:      {len(data)}")
    print(f"Total bytes: {total_bytes}")
    print(f"Total lines: {total_lines}")

    if total_lines == 0:
        raise ValueError("Empty dataset — nothing to summarize.")


if __name__ == "__main__":
    main()
