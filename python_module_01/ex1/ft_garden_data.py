#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age

    def show(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.age} days old")


if __name__ == "__main__":
    print("=== Garden Plant Registry ===")
    # plants: list[Plant] = []
    # while (True):
    #     name = input("Enter new plant name. or 'quit' to exit\n")
    #     if name == "quit":
    #         break
    #     height = int(input("Enter the plant's height\n"))
    #     age = int(input("Enter the plant's age\n"))
    #     plants.append(Plant(name, height, age))
    plants: list[Plant] = [
        Plant("Rose", 25, 30),
        Plant("Sunflower", 80, 45),
        Plant("Cactus", 15, 120),
    ]
    for plant in plants:
        plant.show()
