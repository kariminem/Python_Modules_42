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
    print("=== Plant Factory Output ===")
    plants = [
        Plant("Rose", 25.0, 30, 0.8),
        Plant("Oak", 200.0, 365, 0.4),
        Plant("Cactus", 5.0, 90, 0.3),
        Plant("Sunflower", 80.0, 45, 1.4),
        Plant("Fern", 15.0, 120, 0.2)
        ]
    for plant in plants:
        print("Created: ", end="")
        plant.show()
