#!/usr/bin/env python3


class Plant:
    def __init__(
        self,
        name: str,
        height: float,
        age: int,
        growth_rate: float = 0.8
    ) -> None:
        self._name = name
        self._growth_rate = growth_rate

        if height < 0:
            print(f"{self._name}: Error, height can't be negative")
            self._height = 0.0
        else:
            self._height = height

        if age < 0:
            print(f"{self._name}: Error, age can't be negative")
            self._age = 0
        else:
            self._age = age

        print(f"Plant created: {self._name}: {round(self._height)}cm, "
              f"{self._age} days old")

    def show(self) -> None:
        print(f"{self._name}: {round(self._height)}cm, {self._age} days old")

    def grow(self) -> None:
        self._height = round(self._height + self._growth_rate, 1)

    def age(self) -> None:
        self._age += 1

    def set_height(self, height: float) -> None:
        if height < 0:
            print(f"{self._name}: Error, height can't be negative")
            print("Height update rejected")
        else:
            self._height = height
            print(f"Height updated: {height}cm")

    def set_age(self, age: int) -> None:
        if age < 0:
            print(f"{self._name}: Error, age can't be negative")
            print("Age update rejected")
        else:
            self._age = age
            print(f"Age updated: {age} days")

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._age


if __name__ == "__main__":
    print("=== Garden Security System ===")
    plants: list[Plant] = [
        Plant("Rose", 15.0, 10, 0.8)
    ]
    plants[0].set_height(25)
    plants[0].set_age(30)
    plants[0].set_height(-12)
    plants[0].set_age(-62)
    print("Current state: ", end="")
    plants[0].show()
