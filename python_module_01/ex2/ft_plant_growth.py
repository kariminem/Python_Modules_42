#!/usr/bin/env python3

class Plant:
    def __init__(
        self,
        name: str,
        height: float,
        age: int,
        growth_rate: float
    ) -> None:
        self.name = name
        self.height = height
        self.days = age
        self.growth_rate = growth_rate

    def show(self) -> None:
        print(f"{self.name}: {self.height:.1f}cm, {self.days} days old")

    def grow(self) -> None:
        self.height += self.growth_rate

    def age(self) -> None:
        self.days += 1


if __name__ == "__main__":
    print("=== Garden Plant Registry ===")
    plants = [
        Plant("Rose", 25.0, 30, 0.8),
        Plant("Sunflower", 80.0, 45, 1.4),
        Plant("Cactus", 15.0, 120, 0.3)
        ]
    for plant in plants:
        if plant.name == "Rose":
            initial_height = plant.height
            plant.show()
            for i in range(1, 8):
                print(f"=== Day {i} ===")
                plant.grow()
                plant.age()
                plant.show()
            print(f"Growth this week: {(plant.height - initial_height):.1f}cm")
