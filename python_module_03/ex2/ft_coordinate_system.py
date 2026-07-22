#!/usr/bin/env python3
import math


def get_player_pos() -> tuple[float, float, float]:
    while True:
        raw: str = input("Enter new coordinates as floats in format 'x,y,z': ")
        parts: list[str] = raw.split(",")
        if len(parts) != 3:
            print("Invalid syntax")
            continue
        values: list[float] = []
        failed: bool = False
        for part in parts:
            cleaned: str = part.strip()
            try:
                values.append(float(cleaned))
            except ValueError as error:
                print(f"Error on parameter '{cleaned}': {error}")
                failed = True
                break
        if failed:
            continue
        return (values[0], values[1], values[2])


def distance(
    a: tuple[float, float, float], b: tuple[float, float, float]
) -> float:
    return math.sqrt(
        (b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2 + (b[2] - a[2]) ** 2
    )


def main() -> None:
    print("=== Game Coordinate System ===")

    print("\nGet a first set of coordinates")
    first: tuple[float, float, float] = get_player_pos()
    print(f"Got a first tuple: {first}")
    print(f"It includes: X={first[0]}, Y={first[1]}, Z={first[2]}")
    center: tuple[float, float, float] = (0.0, 0.0, 0.0)
    print(f"Distance to center: {round(distance(center, first), 4)}")

    print("\nGet a second set of coordinates")
    second: tuple[float, float, float] = get_player_pos()
    print(
        f"Distance between the 2 sets of coordinates: "
        f"{round(distance(first, second), 4)}"
    )


if __name__ == "__main__":
    main()
