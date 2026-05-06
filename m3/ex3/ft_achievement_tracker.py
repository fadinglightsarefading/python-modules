import random


def get_player_achievements(achievements_list: list) -> set:
    return set(random.sample(achievements_list, random.randrange(5, 10)))


def ft_achievement_tracker() -> None:
    print("=== Achievment Tracker System ===\n")
    players = ["William", "Charles", "George", "Jane"]
    achievements_list = ["Taking Inventory", "Getting Wood", "Benchmaking",
                         "Time to Mine!", "Hot Topic", "Acquire Hardware",
                         "Time to Farm!", "Bake Bread", "The Lie",
                         "Getting an Upgrade", "Delicious Fish", "On a Rail",
                         "Time to Strike!", "Monster Hunter", "Cow Tipper",
                         "When Pigs Fly", "Sniper Duel", "DIAMONDS!",
                         "Into the Nether", "Return to Sender", "Into Fire",
                         "Local Brewery", "The End?", "The End"]
    achievements = []
    i = 0
    while i < len(players):
        achievements += [get_player_achievements(achievements_list)]
        i += 1
    i = 0
    while i < len(players):
        print(f"\tPlayer {players[i]}:\n{achievements[i]}")
        i += 1
    distinct = set()
    i = 0
    while i < len(players):
        distinct = distinct.union(achievements[i])
        i += 1
    print(f"\nAll distinct achievements: {distinct}")

    common = achievements[0]
    i = 1
    while i < len(players):
        common = common.intersection(achievements[i])
        i += 1
    print(f"\nCommon achievements: {common}\n")
    i = 0
    while i < len(players):
        others = set()
        j = 0
        while j < len(players):
            if j != i:
                others = others.union(achievements[j])
            j += 1
        print(f"{players[i]} only has: {achievements[i].difference(others)}")
        i += 1
    print()
    i = 0
    while i < len(players):
        print(f"\t{players[i]} is missing:\n"
              f"{set(achievements_list).difference(achievements[i])}")
        i += 1


def main() -> None:
    ft_achievement_tracker()


if __name__ == "__main__":
    main()
