from ex0 import CreatureFactory, FlameFactory, AquaFactory
from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex2 import (
    BattleError, BattleStrategy,
    NormalStrategy, AggressiveStrategy, DefensiveStrategy
)


def battle(
    opponents: list[tuple[CreatureFactory, BattleStrategy]]
) -> None:
    print("*** Tournament ***")
    print(f"{len(opponents)} opponents involved")
    fighters = []
    for i in range(len(opponents)):
        fighters += [opponents[i][0].create_base()]
    for i in range(1, len(opponents)):
        print("\n* Battle *")
        fighters[0].describe()
        print(f" vs.")
        fighters[i].describe()
        print(f" now fight!")
        try:
            opponents[0][1].act(fighters[0])
        except BattleError as e:
            print(f"{e}, aborting tournament: Invalid Creature"
                  f" \'{fighters[0].name}\' for this "
                  f"{(
                      opponents[0][1].__class__.__name__
                      .lower()
                      .replace("strat", " strat")
                  )}")
            return
        try:
            opponents[i][1].act(fighters[i])
        except BattleError as e:
            print(f"{e}, aborting tournament: Invalid Creature"
                  f" \'{fighters[i].name}\' for this "
                  f"{(
                      opponents[i][1].__class__.__name__
                      .lower()
                      .replace("strat", " strat")
                  )}")
            return


def main() -> None:
    flame_fac = FlameFactory()
    aqua_fac = AquaFactory()
    hc_fac = HealingCreatureFactory()
    tc_fac = TransformCreatureFactory()
    normal_strat = NormalStrategy()
    agress_strat = AggressiveStrategy()
    defens_strat = DefensiveStrategy()

    print("Tournament 0 (basic)")
    tournament_0 = [
        (flame_fac, normal_strat),
        (hc_fac, defens_strat)
    ]
    battle(tournament_0)

    print("Tournament 1 (error)")
    tournament_1 = [
        (flame_fac, agress_strat),
        (hc_fac, defens_strat)
    ]
    battle(tournament_1)


if __name__ == "__main__":
    main()
