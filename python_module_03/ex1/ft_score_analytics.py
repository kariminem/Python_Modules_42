#!/usr/bin/env python3
import sys


def main() -> None:
    args: list[str] = sys.argv[1:]
    print("=== Player Score Analytics ===")

    usage: str = (
        "No scores provided. "
        "Usage: python3 ft_score_analytics.py <score1> <score2> ..."
    )

    if len(args) == 0:
        print(usage)
        return

    scores: list[int] = []
    for arg in args:
        try:
            scores.append(int(arg))
        except ValueError:
            print(f"Invalid parameter: '{arg}'")

    if len(scores) == 0:
        print(usage)
        return

    total: int = sum(scores)
    average: float = total / len(scores)
    high: int = max(scores)
    low: int = min(scores)

    print(f"Scores processed: {scores}")
    print(f"Total players: {len(scores)}")
    print(f"Total score: {total}")
    print(f"Average score: {round(average, 1)}")
    print(f"High score: {high}")
    print(f"Low score: {low}")
    print(f"Score range: {high - low}")


if __name__ == "__main__":
    main()
