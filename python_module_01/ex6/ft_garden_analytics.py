#!/usr/bin/env python3


class Plant:
    class Statistics:
        def __init__(self) -> None:
            self._age_calls: int = 0
            self._grow_calls: int = 0
            self._show_calls: int = 0

        def record_age(self) -> None:
            self._age_calls += 1

        def record_grow(self) -> None:
            self._grow_calls += 1

        def record_show(self) -> None:
            self._show_calls += 1

        def display_stats(self) -> None:
            print(
                f"Stats: {self._grow_calls} grow, "
                f"{self._age_calls} age, "
                f"{self._show_calls} show"
            )

    def __init__(
        self,
        name: str,
        height: float,
        age: int,
        growth_rate: float = 0.8
    ) -> None:
        self.stats: Plant.Statistics = self.Statistics()
        self._name: str = name
        self._growth_rate: float = growth_rate

        if height < 0:
            print(f"{self._name}: Error, height can't be negative")
            self._height: float = 0.0
        else:
            self._height = height

        if age < 0:
            print(f"{self._name}: Error, age can't be negative")
            self._age: int = 0
        else:
            self._age = age

    def show(self) -> None:
        self.stats.record_show()
        print(f"{self._name}: {self._height:.1f}cm, {self._age} days old")

    def grow(self) -> None:
        self.stats.record_grow()
        self._height = round(self._height + self._growth_rate, 1)

    def age(self) -> None:
        self.stats.record_age()
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

    @staticmethod
    def is_greater_than_year(age: int) -> bool:
        return age > 365

    @classmethod
    def create_anonymous(cls) -> 'Plant':
        return cls("Unknown plant", 0.0, 0, 0.0)


class Flower(Plant):
    def __init__(
        self,
        name: str,
        height: float,
        age: int,
        growth_rate: float,
        color: str
    ) -> None:
        super().__init__(name, height, age, growth_rate)
        self.color: str = color
        self._bloomed: bool = False

    def bloom(self) -> None:
        self._bloomed = True

    def show(self) -> None:
        super().show()
        print()
        print(f"Color: {self.color}")
        print()
        if self._bloomed:
            print(f"{self._name} is blooming beautifully!")
        else:
            print(f"{self._name} has not bloomed yet")


class Seed(Flower):
    def __init__(
        self,
        name: str,
        height: float,
        age: int,
        growth_rate: float,
        color: str,
        seed_count: int
    ) -> None:
        super().__init__(name, height, age, growth_rate, color)
        self.seed_count: int = seed_count

    def show(self) -> None:
        super().show()
        if self._bloomed:
            print(f" Seeds: {self.seed_count}")
        else:
            print(" Seeds: 0")


class Tree(Plant):
    class TreeStatistics(Plant.Statistics):
        def __init__(self) -> None:
            super().__init__()
            self._shade_calls: int = 0

        def record_shade(self) -> None:
            self._shade_calls += 1

        def display_stats(self) -> None:
            super().display_stats()
            print(f" {self._shade_calls} shade")

    def __init__(
        self,
        name: str,
        height: float,
        age: int,
        growth_rate: float,
        trunk_diameter: float
    ) -> None:
        super().__init__(name, height, age, growth_rate)
        self.tree_stats: Tree.TreeStatistics = self.TreeStatistics()
        self.stats = self.tree_stats
        self.trunk_diameter: float = trunk_diameter

    def show(self) -> None:
        super().show()
        print()
        print(f"Trunk diameter: {self.trunk_diameter:.1f}cm")

    def produce_shade(self) -> None:
        self.tree_stats.record_shade()
        print(
            f"Tree {self._name} now produces a shade of "
            f"{self.get_height():.1f}cm long and "
            f"{self.trunk_diameter:.1f}cm wide."
        )


class Vegetable(Plant):
    def __init__(
        self,
        name: str,
        height: float,
        age: int,
        growth_rate: float,
        harvest_season: str,
        nutritional_value: int = 0
    ) -> None:
        super().__init__(name, height, age, growth_rate)
        self.harvest_season: str = harvest_season
        self.nutritional_value: int = nutritional_value

    def bloom(self) -> None:
        print(f"{self._name} is blooming")


def display_plant_stats(plant: Plant) -> None:
    plant.stats.display_stats()


if __name__ == "__main__":
    print("=== Garden statistics ===")
    print()
    print("Check year-old")
    print()
    print(
        f"Is 30 days more than a year? -> "
        f"{Plant.is_greater_than_year(30)}"
    )
    print(
        f"Is 400 days more than a year? -> "
        f"{Plant.is_greater_than_year(400)}"
    )
    print()
    print("=== Flower")
    print()
    rose = Flower("Rose", 15.0, 10, 8.0, "red")
    rose.show()
    print()
    print("[statistics for Rose]")
    display_plant_stats(rose)
    print()
    print("[asking the rose to grow and bloom]")
    print()
    rose.grow()
    rose.bloom()
    rose.show()
    print()
    print("[statistics for Rose]")
    display_plant_stats(rose)
    print()
    print("=== Tree")
    print()
    oak = Tree("Oak", 200.0, 365, 0.8, 5.0)
    oak.show()
    print()
    print("[statistics for Oak]")
    display_plant_stats(oak)
    print()
    print("[asking the oak to produce shade]")
    print()
    oak.produce_shade()
    print()
    print("[statistics for Oak]")
    display_plant_stats(oak)
    print()
    print("=== Seed")
    print()
    sunflower = Seed("Sunflower", 80.0, 45, 30.0, "yellow", 42)
    sunflower.show()
    print()
    print("[make sunflower grow, age and bloom]")
    sunflower.grow()
    sunflower.age()
    sunflower.bloom()
    sunflower.show()
    print()
    print("[statistics for Sunflower]")
    display_plant_stats(sunflower)
    print()
    print("Anonymous")
    print()
    anonymous = Plant.create_anonymous()
    anonymous.show()
    print("[statistics for Unknown plant]")
    display_plant_stats(anonymous)
