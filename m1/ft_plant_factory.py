class Plant:
    def __init__(self, name, height, age) -> None:
        self.name = name
        self.height = height
        self.age_days = age

    def show(self):
        return f"{self.name}: {round(self.height, 1)}cm, " \
               f"{self.age_days} days old"


def ft_plant_factory():
    print("=== Plant Factory Output ===")
    plants = [
        Plant("Rose", 25.0, 30),
        Plant("Oak", 200.0, 365),
        Plant("Cactus", 5.0, 90),
        Plant("Sunflower", 80.0, 45),
        Plant("Fern", 15.0, 120)
    ]
    for i in range(0, 5):
        print("Created:", plants[i].show())


def main():
    ft_plant_factory()


if __name__ == "__main__":
    main()
