#!/usr/bin/env python3
import random

PLAYERS: list[str] = [
    "Alice", "bob", "Charlie", "dylan", "Emma",
    "Gregory", "john", "kevin", "Liam",
]


def main() -> None:
    print("=== Game Data Alchemist ===")
    print(f"Initial list of players: {PLAYERS}")

    capitalized: list[str] = [name.capitalize() for name in PLAYERS]
    print(f"New list with all names capitalized: {capitalized}")

    already_capitalized: list[str] = [
        name for name in PLAYERS if name[0].isupper()
    ]
    print(f"New list of capitalized names only: {already_capitalized}")

    scores: dict[str, int] = {
        name: random.randint(1, 999) for name in capitalized
    }
    print(f"Score dict: {scores}")

    average: float = sum(scores.values()) / len(scores)
    print(f"Score average is {round(average, 2)}")

    high_scores: dict[str, int] = {
        name: score for name, score in scores.items() if score > average
    }
    print(f"High scores: {high_scores}")


if __name__ == "__main__":
    main()
