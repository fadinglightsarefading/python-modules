class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name
        self.height = height
        self.age_days = age

    def show(self) -> None:
        print(f"{self.name}: {round(self.height, 1)}cm, "
              f"{self.age_days} days old")

    def grow(self) -> None:
        if self.name == "Rose":
            self.height += 0.8
        elif self.name == "Sunflower":
            self.height += 1
        elif self.name == "Cactus":
            self.height += 0.2

    def age(self) -> None:
        self.age_days += 1


def main() -> None:
    print("=== Garden Plant Growth ===")
    name = "Rose"
    height = 25.0
    age = 30
    plant = Plant(name, height, age)
    plant.show()
    for i in range(1, 8):
        print(f"=== Day {i} ===")
        plant.grow()
        plant.age()
        plant.show()
    print(f"Growth this week {round(plant.height - height, 1)}cm")


if __name__ == "__main__":
    main()
