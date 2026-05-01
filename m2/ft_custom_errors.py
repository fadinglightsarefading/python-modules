class GardenError(Exception):
    def __init__(self, message="Caught GardenError"):
        Exception.__init__(self, message)

class PlantError(GardenError):
    def __init__(self, message="Caught PlantError"):
        GardenError.__init__(self, message)

class WaterError(GardenError):
    def __init__(self, message="Caught WaterError"):
        GardenError.__init__(self, message)

class Plant:
    def __init__(self, name):
        self.name = name
        self.wilting = True

class Tank:
    def __init__(self):
        self.volume = 200


def test_tomato(wilting: bool) -> None:
    if wilting:
        raise PlantError()


def test_aqua(volume: int) -> None:
    if volume < 10000:
        raise WaterError()


def test_tomato_garden(wilting: bool) -> None:
    if wilting:
        raise GardenError()


def test_aqua_garden(volume: int) -> None:
    if volume < 10000:
        raise GardenError()


def ft_custom_errors() -> None:
    print("=== Custom Garden Errors Demo ===")
    print("\nTesting PlantError...")
    tomato_plant = Plant("tomato plant")
    try:
        test_tomato(tomato_plant.wilting)
    except PlantError as e:
        print(f"{e}: The {tomato_plant.name} is wilting!")
    print("\nTesting WaterError...")
    aquarium = Tank()
    try:
        test_aqua(aquarium.volume)
    except WaterError as e:
        print(f"{e}: Not enought water in tank!")
    print("\nTesting catching all garden errors...")
    try:
        test_tomato_garden(tomato_plant.wilting)
    except GardenError as e:
        print(f"{e}: The {tomato_plant.name} is wilting!")
    try:
        test_aqua_garden(aquarium.volume)
    except GardenError as e:
        print(f"{e}: Not enought water in tank!")
    print("\nAll custom types work correctly!")


def main() -> None:
    ft_custom_errors()

if __name__ == "__main__":
    main()
