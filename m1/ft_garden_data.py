class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age

    def show(self):
        return f"{self.name}: {self.height}cm, {self.age} days old"


def ft_garden_data(name: str, height: int, age: int):
    plant = Plant(name, height, age)
    print(plant.show())


def main():
    print("=== Garden Plant Registry ===")
    ft_garden_data("Rose", 25, 30)
    ft_garden_data("Sunflower", 80, 45)
    ft_garden_data("Cactus", 15, 120)


if __name__ == "__main__":
    main()
