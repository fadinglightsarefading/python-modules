from ex0 import CreatureFactory, FlameFactory, AquaFactory


def test_factories(factory: CreatureFactory) -> None:
    base_creature = factory.create_base()
    base_creature.describe()
    base_creature.attack()
    evolved_creature = factory.create_evolved()
    evolved_creature.describe()
    evolved_creature.attack()


def battle(flame_factory: FlameFactory,
           aqua_factory: AquaFactory) -> None:
    flameling = flame_factory.create_base()
    aquabub = aqua_factory.create_base()
    flameling.describe()
    print(" vs.")
    aquabub.describe()
    print(" fight!")
    flameling.attack()
    aquabub.attack()


def main() -> None:
    flame_factory = FlameFactory()
    aqua_factory = AquaFactory()
    print("Testing factory")
    test_factories(flame_factory)
    print("\nTesting factory")
    test_factories(aqua_factory)
    print("\nTesting battle")
    battle(flame_factory, aqua_factory)


if __name__ == "__main__":
    main()
