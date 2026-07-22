#!/usr/bin/env python3
import random

ACHIEVEMENTS: list[str] = [
    "Crafting Genius",
    "Strategist",
    "World Savior",
    "Speed Runner",
    "Survivor",
    "Master Explorer",
    "Treasure Hunter",
    "Unstoppable",
    "First Steps",
    "Collector Supreme",
    "Untouchable",
    "Sharp Mind",
    "Boss Slayer",
    "Hidden Path Finder",
]


def gen_player_achievements() -> set[str]:
    count: int = random.randint(5, 9)
    return set(random.sample(ACHIEVEMENTS, count))


def main() -> None:
    print("=== Achievement Tracker System ===\n")

    names: list[str] = ["Alice", "Bob", "Charlie", "Dylan"]
    players: dict[str, set[str]] = {}
    for name in names:
        players[name] = gen_player_achievements()
        print(f"Player {name}: {players[name]}")

    all_achievements: set[str] = set()
    for name in names:
        all_achievements = all_achievements.union(players[name])
    print(f"\nAll distinct achievements: {all_achievements}")

    common: set[str] = set(ACHIEVEMENTS)
    for name in names:
        common = common.intersection(players[name])
    print(f"Common achievements: {common}\n")

    for name in names:
        others: set[str] = set()
        for other in names:
            if other != name:
                others = others.union(players[other])
        only_mine: set[str] = players[name].difference(others)
        print(f"Only {name} has: {only_mine}")

    print()
    for name in names:
        missing: set[str] = all_achievements.difference(players[name])
        print(f"{name} is missing: {missing}")


if __name__ == "__main__":
    main()
