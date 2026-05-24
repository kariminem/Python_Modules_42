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
        self._height = height
        self._days = age
        self._growth_rate = growth_rate
        self.validator()

    def validator(self) -> None:
        if (self._height < 0 or self._days < 0):
            print("Can't create the plant due to wrong input values!")
        else:
            print("Plant created: ", end="")
            self.show()
            print()

    def show(self) -> None:
        print(f"{self.name}: {self._height:.1f}cm, {self._days}  days old")

    def grow(self) -> None:
        self._height += self._growth_rate

    def age(self) -> None:
        self._days += 1

    def set_height(self, height: float) -> None:
        if height < 0:
            print(f"{self.name}: Error, height can't be negative")
            print("Height update rejected")
        else:
            self._height = height
            print(f"Height updated: {height}cm")

    def set_age(self, age: int) -> None:
        if age < 0:
            print(f"{self.name}: Error, age can't be negative")
            print("Age update rejected")
        else:
            self._days = age
            print(f"Age updated: {age} days")

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._days


if __name__ == "__main__":

    print("=== Garden Security System ===")
    plants = [
        Plant("Rose", 15.0, 10, 0.8),
        ]
    plants[0].set_height(25)
    plants[0].set_age(30)
    print()
    plants[0].set_height(-12)
    plants[0].set_age(-62)
    print("\nCurrent state: ", end="")
    plants[0].show()
