from ex0.creatures import Creature
from .capabilities import HealCapability, TransformCapability


class Sproutling(Creature, HealCapability):
    def __init__(self) -> None:
        super().__init__("Sproutling", "Grass")

    def attack(self) -> None:
        print("Sproutling uses Vine Whip!")

    def heal(self) -> None:
        print("Sproutling heals itself for a small amount")


class Bloomelle(Creature, HealCapability):
    def __init__(self) -> None:
        super().__init__("Bloomelle", "Grass/Fairy")

    def attack(self) -> None:
        print("Bloomelle uses Petal Dance!")

    def heal(self) -> None:
        print("Bloomelle heals itself and others for a large amount")


class Shiftling(Creature, TransformCapability):
    def __init__(self) -> None:
        Creature.__init__(self, "Shiftling", "Normal")
        TransformCapability.__init__(self)

    def attack(self) -> None:
        if self.transformed:
            print("Shiftling performs boosted strike!")
        else:
            print("Shiftling attacks normally.")

    def transform(self) -> None:
        self.transformed = True
        print("Shitfling shifts into sharper form!")

    def revert(self) -> None:
        self.transformed = False
        print("Shiftling returns to normal.")


class Morphagon(Creature, TransformCapability):
    def __init__(self) -> None:
        Creature.__init__(self, "Morphagon", "Normal/Dragon")
        TransformCapability.__init__(self)

    def attack(self) -> None:
        if self.transformed:
            print("Morphagon unleashes a devastating morph strike!")
        else:
            print("Morphagon attacks normally.")

    def transform(self) -> None:
        self.transformed = True
        print("Morphagon morphs into dragonic battle form!")

    def revert(self) -> None:
        self.transformed = False
        print("Morphagon stabilises its form.")
