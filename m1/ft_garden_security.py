class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.set_height(height)
        self.set_age(age)

    def show(self):
        return f"{self.name}: {self.get_height()}cm, {self.get_age()} days old"

    def set_height(self, height):
        if height < 0:
            print(f"{self.name}: Error, height can't be negative\n"
                  f"Height update rejected")
            return
        self._height = height

    def set_age(self, age):
        if age < 0:
            print(f"{self.name}: Error, age can't be negative\n"
                  f"Age update rejected")
            return
        self._age = age

    def get_height(self):
        return self._height

    def get_age(self):
        return self._age


def ft_garden_security(name: str, height: float, age: int):
    plant = Plant(name, height, age)
    print("Plant created:", plant.show())
    for i in range(0, 20):
        plant.set_height(plant.get_height() + 0.5)
        plant.set_age(plant.get_age() + 1)
    print(f"\nHeight updated: {plant.get_height()}cm\n"
          f"Age updated: {plant.get_age()} days\n")
    plant.set_height(-100)
    plant.set_age(-100)
    print("\nCurrent state:", plant.show())


def main():
    ft_garden_security("Rose", 15.0, 10)


if __name__ == "__main__":
    main()
