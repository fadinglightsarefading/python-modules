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
    have_fought: list[set] = []
    for i in range(0, len(opponents)):
        for j in range(1, len(opponents)):
            if fighters[i] == fighters[j]:
                continue
            if {fighters[i], fighters[j]} in have_fought:
                continue
            else:
                have_fought += [{fighters[i], fighters[j]}]
            print("\n* Battle *")
            fighters[i].describe()
            print(" vs.")
            fighters[j].describe()
            print(" now fight!")
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
            try:
                opponents[j][1].act(fighters[j])
            except BattleError as e:
                print(f"{e}, aborting tournament: Invalid Creature"
                      f" \'{fighters[j].name}\' for this "
                      f"{(
                          opponents[j][1].__class__.__name__
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

    print("\nTournament 1 (error)")
    tournament_1 = [
        (flame_fac, agress_strat),
        (hc_fac, defens_strat)
    ]
    battle(tournament_1)

    print("\nTournament 2 (multiple)")
    tournament_2 = [
        (aqua_fac, normal_strat),
        (hc_fac, defens_strat),
        (tc_fac, agress_strat)
    ]
    battle(tournament_2)


if __name__ == "__main__":
    main()
