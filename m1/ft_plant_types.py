class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name
        self.set_height(height)
        self.set_age(age)

    def show(self) -> str:
        print(f"{self.name}: {round(self.height, 1)}cm, "
              f"{self.age_days} days old")

    def set_height(self, height: float) -> None:
        if height < 0:
            print(f"{self.name}: Error, height can't be negative"
                  f"Height update rejected")
            return
        self._height = height

    def set_age(self, age) -> None:
        if age < 0:
            print(f"{self.name}: Error, age can't be negative"
                  f"Age update rejected")
            return
        self._age = age

class Flower(Plant):
    def __init__(self, name: str, height: float, age: int, colour: str) -> None:
        super().__init__(name, height, age)
        self.colour = colour
        self.bloomed = False

    def show(self) -> str:
        print(f"{self.name}: {round(self._height, 1)}cm, "
              f"{self._age} days old\n Colour: {self.colour}")
        if self.bloomed:
            print(f" {self.name} is blooming beautifully!")
        else:
            print(f" {self.name} has not bloomed yet")

    def bloom(self):
        self.bloomed = True

class Tree(Plant):
    def __init__(self, name: str, height: float, age: int, trunk_diametre: float) -> None:
        super().__init__(name, height, age)
        self.trunk_diametre = trunk_diametre

    def show(self) -> None:
        print(f"{self.name}: {round(self._height, 1)}cm, "
              f"{self._age} days old\n Trunk diametre: {self.trunk_diametre}cm")

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

def ft_plant_types() -> None:
    print("=== Garden Plant Types ===")
    plants = [Flower("Rose", 15.0, 10, "red"),
              Tree("Oak", 200.0, 365, 5.0),
              Vegetable("Tomato", 5.0, 10, "Summer", 0)]
    print("=== Flower")
    plants[0].show()
    plants[0].bloom()
    plants[0].show()
    print("\n=== Tree")
    plants[1].show()
    plants[1].produce_shade() 
    print("\n=== Vegetable")
    plants[2].show()
    for i in range(0, 20):
        plants[2]._height += 2.1
        plants[2]._age += 1
        plants[2].nutritional_value += 1
    plants[2].show()

def main():
    ft_plant_types()

if __name__ == "__main__":
    main()
