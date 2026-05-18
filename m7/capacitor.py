from ex1 import HealingCreatureFactory, TransformCreatureFactory


def main() -> None:
    heal_creature_fac = HealingCreatureFactory()
    print("Testing Healing Capability Creature")
    print(" base:")
    sproutling = heal_creature_fac.create_base()
    sproutling.describe()
    sproutling.attack()
    sproutling.heal()
    print(" evolved:")
    bloomelle = heal_creature_fac.create_evolved()
    bloomelle.describe()
    bloomelle.attack()
    bloomelle.heal()
    transf_creature_fac = TransformCreatureFactory()
    print("\nTesting Transform Capability Creature")
    print(" base:")
    shiftling = transf_creature_fac.create_base()
    shiftling.describe()
    shiftling.attack()
    shiftling.transform()
    shiftling.attack()
    shiftling.revert()
    print(" evolved:")
    morphagon = transf_creature_fac.create_evolved()
    morphagon.describe()
    morphagon.attack()
    morphagon.transform()
    morphagon.attack()
    morphagon.revert()


if __name__ == "__main__":
    main()
