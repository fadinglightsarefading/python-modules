import abc


class Creature(abc.ABC):
    def __init__(self, name: str, _type: str):
        self.name = name
        self.type = _type

    @abc.abstractmethod
    def attack(self) -> None:
        pass

    def describe(self) -> None:
        print(f"{self.name} is a {self.type} type Creature")


class Flameling(Creature):
    def __init__(self) -> None:
        super().__init__("Flameling", "Fire")

    def attack(self) -> None:
        print("Flameling uses Ember!")


class Pyrodon(Creature):
    def __init__(self) -> None:
        super().__init__("Pyrodon", "Flame/Flying")

    def attack(self) -> None:
        print("Pyrodon uses Flamethrower!")


class Aquabub(Creature):
    def __init__(self) -> None:
        super().__init__("Aquabub", "Water")

    def attack(self) -> None:
        print("Aquabub uses Water Gun!")


class Torragon(Creature):
    def __init__(self) -> None:
        super().__init__("Torragon", "Water")

    def attack(self) -> None:
        print("Torragon uses Hydro Pump!")
