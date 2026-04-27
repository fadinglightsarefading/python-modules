class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age_days = age

    def show(self):
        return f"{self.name}: {round(self.height, 1)}cm, " \
               f"{self.age_days} days old"

    def grow(self):
        if self.name == "Rose":
            self.height += 0.8
        elif self.name == "Sunflower":
            self.height += 1
        elif self.name == "Cactus":
            self.height += 0.2

    def age(self):
        self.age_days += 1


def ft_plant_growth(name: str, height: float, age: int):
    print("=== Garden Plant Growth ===")
    plant = Plant(name, height, age)
    print(plant.show())
    for i in range(1, 8):
        print(f"=== Day {i} ===")
        plant.grow()
        plant.age()
        print(plant.show())
    print(f"Growth this week {round(plant.height - height, 1)}cm")


def main():
    ft_plant_growth("Rose", 25, 30)
    print("")
    ft_plant_growth("Sunflower", 80, 45)
    print("")
    ft_plant_growth("Cactus", 15, 120)


if __name__ == "__main__":
    main()
