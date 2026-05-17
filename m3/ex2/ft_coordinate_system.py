import math


def get_player_pos() -> tuple[float, float, float]:
    while True:
        coordinates_str = input("\nEnter new coordinates as floats "
                                "in the format \'x,y,z\': ").split(',')
        if len(coordinates_str) != 3:
            print("Error: Invalid syntax")
            continue
        coordinates = []
        try:
            for value in coordinates_str:
                coordinates += [float(value.strip())]
        except ValueError:
            print(f"Error on parametre \'{value.strip()}\': "
                  f"could not convert string to float: \'{value.strip()}\'")
            continue
        break
    return (coordinates[0], coordinates[1], coordinates[2])


def main() -> None:
    print("=== Game Coordinate System ===")
    first_set = get_player_pos()
    print(f"Got a first tuple: {first_set}\nIt includes: X={first_set[0]},"
          f" Y={first_set[1]}, Z={first_set[2]}")
    print(f"Distance to centre: {round(math.sqrt(
          (0 - first_set[0])**2 + (0 - first_set[1])**2 + (0 - first_set[2])**2
          ), 4)}")
    second_set = get_player_pos()
    print(f"Distance between the two sets of coordinates: "
          f"{round(math.sqrt(
            (second_set[0] - first_set[0])**2 +
            (second_set[1] - first_set[1])**2 +
            (second_set[2] - first_set[2])**2
          ), 4)}")


if __name__ == "__main__":
    main()
