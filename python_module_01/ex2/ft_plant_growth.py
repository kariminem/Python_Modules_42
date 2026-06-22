#!/usr/bin/env python3

class Plant:
    def __init__(
        self,
        name: str,
        height: float,
        age: int,
        growth_rate: float = 0.8
    ) -> None:
        self.name: str = name
        self.height: float = height
        self._age: int = age
        self.growth_rate: float = growth_rate

    def show(self) -> None:
        print(f"{self.name}: {round(self.height, 1)}cm, {self._age} days old")

    def grow(self) -> None:
        self.height += self.growth_rate

    def age(self) -> None:
        self._age += 1


if __name__ == "__main__":
    print("=== Garden Plant Growth ===")
    rose = Plant("Rose", 25.0, 30, 0.8)
    initial_height = rose.height
    rose.show()
    for day in range(1, 8):
        print(f"=== Day {day} ===")
        rose.grow()
        rose.age()
        rose.show()
    weekly_growth = rose.height - initial_height
    print(f"Growth this week: {round(weekly_growth, 1)}cm")
