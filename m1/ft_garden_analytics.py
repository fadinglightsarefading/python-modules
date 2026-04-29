class Plant():
    class Stats():
        def __init__(self) -> None:
            self.grow_calls = 0
            self.age_calls = 0
            self.show_calls = 0

        def display(self) -> None:
            print(f"Stats: {self.grow_calls} grows, {self.age_calls} age, "
                  f"{self.show_calls} show")

    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name
        self.set_height(height)
        self.set_age(age)
        self.stats = Plant.Stats()

    def show(self) -> None:
        print(f"{self.name}: {self._height}cm, {self._age} days old")
        self.stats.show_calls += 1

    def set_height(self, height: float) -> None:
        if height < 0:
            print(f"{self.name}: Error, height can't be negative\n"
                  f"Height update rejected")
            return
        self._height = height

    def set_age(self, age: int) -> None:
        if age < 0:
            print(f"{self.name}: Error, age can't be negative\n"
                  f"Height update rejected")
            return
        self._age = age

    def grow(self, how_much: float) -> None:
        self.set_height(self._height + how_much)
        self.stats.grow_calls += 1

    def age(self, how_much: int) -> None:
        self.set_age(self._age + how_much)
        self.stats.age_calls += 1

    @staticmethod
    def older_than_year(age: int) -> bool:
        return age > 365

    @classmethod
    def anonymous(cls) -> "Plant":
        return cls("Unknown plant", 0.0, 0)


class Flower(Plant):
    def __init__(self, name: str, height: float, age: int,
                 colour: str) -> None:
        super().__init__(name, height, age)
        self.colour = colour
        self.bloomed = False

    def show(self) -> None:
        super().show()
        print(f" Colour: {self.colour}")
        if self.bloomed:
            print(f" {self.name} is blooming beautifully!")
        else:
            print(f" {self.name} has not bloomed yet")

    def bloom(self) -> None:
        self.bloomed = True


class Tree(Plant):
    class Stats(Plant.Stats):
        def __init__(self) -> None:
            super().__init__()
            self.shade_calls = 0

        def display(self) -> None:
            super().display()
            print(f" {self.shade_calls} shade")

    def __init__(self, name: str, height: float, age: int,
                 trunk_diametre: float) -> None:
        super().__init__(name, height, age)
        self.trunk_diametre = trunk_diametre
        self.stats = Tree.Stats()

    def show(self) -> None:
        super().show()
        print(f" Trunk diametre: {self.trunk_diametre}")

    def produce_shade(self) -> None:
        print(f"Tree {self.name} is now producing shade {self._height}cm "
              f"long and {self.trunk_diametre}cm wide.")
        self.stats.shade_calls += 1


class Seed(Flower):
    def __init__(self, name: str, height: float, age: int, colour: str,
                 seeds: int) -> None:
        super().__init__(name, height, age, colour)
        self.seeds = seeds

    def show(self) -> None:
        super().show()
        print(f" Seeds: {self.seeds}")

    def bloom(self, seeds: int) -> None:
        super().bloom()
        self.seeds += seeds


def ft_statistical_data(plant: Plant) -> None:
    plant.stats.display()


def ft_garden_analytics() -> None:
    print("=== Garden statistics ===")
    plant = [Flower("Rose", 15.0, 10, "red"),
             Tree("Oak", 200.0, 365, 5.0),
             Seed("Sunflower", 80.0, 45, "yellow", 0)]

    print("=== Check year-old")
    print(f"Is {plant[1]._age} more than a year? ->"
          f"{Plant.older_than_year(plant[1]._age)}")
    print(f"Is 400 more than a year? -> {Plant.older_than_year(400)}")

    print("\n=== Flower")
    plant[0].show()
    ft_statistical_data(plant[0])
    plant[0].grow(8)
    plant[0].bloom()
    plant[0].show()
    ft_statistical_data(plant[0])

    print("\n=== Tree")
    plant[1].show()
    ft_statistical_data(plant[1])
    plant[1].produce_shade()
    ft_statistical_data(plant[1])

    print("\n=== Seed")
    plant[2].show()
    plant[2].grow(30)
    plant[2].age(20)
    plant[2].bloom(42)
    plant[2].show()
    ft_statistical_data(plant[2])

    print("\n=== Anonymous")
    anon = Plant.anonymous()
    anon.show()
    ft_statistical_data(anon)


def main() -> None:
    ft_garden_analytics()


if __name__ == "__main__":
    main()
