class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name
        self.set_height(height)
        self.set_age(age)

    def show(self) -> None:
        print(f"{self.name}: {round(self._height, 1)}cm, "
              f"{self._age} days old")

    def set_height(self, height: float) -> None:
        if height < 0:
            print(f"{self.name}: Error, height can't be negative"
                  f"Height update rejected")
            return
        self._height = height

    def set_age(self, age: int) -> None:
        if age < 0:
            print(f"{self.name}: Error, age can't be negative"
                  f"Age update rejected")
            return
        self._age = age


class Flower(Plant):
    def __init__(
        self,
        name: str,
        height: float,
        age: int,
        colour: str
    ) -> None:
        super().__init__(name, height, age)
        self.colour = colour
        self.bloomed = False

    def show(self) -> None:
        print(f"{self.name}: {round(self._height, 1)}cm, "
              f"{self._age} days old\n Colour: {self.colour}")
        if self.bloomed:
            print(f" {self.name} is blooming beautifully!")
        else:
            print(f" {self.name} has not bloomed yet")

    def bloom(self) -> None:
        self.bloomed = True


class Tree(Plant):
    def __init__(
        self,
        name: str,
        height: float,
        age: int,
        trunk_diametre: float
    ) -> None:
        super().__init__(name, height, age)
        self.trunk_diametre = trunk_diametre

    def show(self) -> None:
        print(f"{self.name}: {round(self._height, 1)}cm, "
              f"{self._age} days old\n Trunk diametre:"
              f"{self.trunk_diametre}cm")

    def produce_shade(self) -> None:
        print(f"Tree {self.name} now produces shade {self._height}cm long "
              f"and {self.trunk_diametre}cm wide")


class Vegetable(Plant):
    def __init__(self, name: str, height: float, age: int, harvest_season: str,
                 nutritional_value: int) -> None:
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

    def show(self) -> None:
        print(f"{self.name}: {round(self._height, 1)}cm, {self._age} days old"
              f"\n Harvest season: {self.harvest_season}"
              f"\n Nutritional value: {self.nutritional_value}")


def main() -> None:
    print("=== Garden Plant Types ===")
    rose = Flower("Rose", 15.0, 10, "red")
    oak = Tree("Oak", 200.0, 365, 5.0)
    tomato = Vegetable("Tomato", 5.0, 10, "Summer", 0)
    print("=== Flower")
    rose.show()
    rose.bloom()
    rose.show()
    print("\n=== Tree")
    oak.show()
    oak.produce_shade()
    print("\n=== Vegetable")
    tomato.show()
    for i in range(0, 20):
        tomato._height += 2.1
        tomato._age += 1
        tomato.nutritional_value += 1
    tomato.show()


if __name__ == "__main__":
    main()
