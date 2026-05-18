from ex0 import CreatureFactory, FlameFactory, AquaFactory
from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex2 import BattleStrategy, NormalStrategy, AggressiveStrategy, DefensiveStrategy


def battle(opponents: list[tuple[CreatureFactory, BattleStrategy]]) -> None:
    


def main() -> None:
    flame_fac = FlameFactory()
    aqua_fac = AquaFactory()
    hc_fac = HealingCreatureFactory()
    tc_fac = TransformCreatureFactory()
    normal_strat = NormalStrategy()
    agress_strat = AggressiveStrategy()
    defens_strat = DefensiveStrategy()


if __name__ == "__main__":
    main()
