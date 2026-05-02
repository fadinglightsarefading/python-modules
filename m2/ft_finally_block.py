class PlantError(Exception):
    def __init__(self, message="Caught PlantError"):
        Exception.__init__(self, message)
        
class Plant:
    def __init__(self, name):
        self.name = name
        self.watered = False

def water_plant(plant: Plant) -> None:
    if not ('A' <= plant.name <= 'Z'):
        raise PlantError
    else:
        plant.watered = True
        print(f"Watering {plant.name}: [OK]")


def test_watering_system(plant: Plant) -> None:
    print("Opening water system")
    i = 0
    try:
        while i < 3:
            water_plant(plant[i])
            i += 1
    except PlantError as e:
        print(f"{e}: Invalid plant name to water: \'{plant[i].name}\'")
        print(".. ending all tests and returning to main")
        return
    finally:
        print("Closing water system")


def main():
    print("=== Garden Watering System ===")
    print("\nTesting valid plants...")
    plants = [Plant("tomato"),
              Plant("lettuce"),
              Plant("carrots")]
    test_watering_system([Plant(p.name.capitalize()) for p in plants])
    print("\nTesting invalid plants...")
    plants[0].name = plants[0].name.capitalize()
    test_watering_system(plants)


if __name__ == "__main__":
    main()
