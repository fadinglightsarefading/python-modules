import random


def ft_data_alchemist() -> None:
    print("=== Game Data Alchemist ===\n")
    players = ["Alice", "bob", "Charlie", "dylan", "Emma",
               "Gregory", "john", "kevin", "Liam"]
    print(f"Initial list of players: {players}")
    all_capitalised = [player.capitalize() for player in players]
    print(f"New list with all names capitalised: {all_capitalised}")
    only_capitalised = [player for player in players if player[:1].isupper()]
    print(f"New list of capitalised names only: {only_capitalised}\n")
    players_scores = {player: random.randint(0, 1000) for player in all_capitalised}
    print(f"Score dict: {players_scores}")
    scores_sum = 0
    for key in players_scores:
        scores_sum += players_scores[key]
    average = round(scores_sum / len(players), 2)
    print(f"Score average: {average}")
    high_scores = {player: players_scores[player]
                   for player in players_scores if players_scores[player] > average}
    print(f"High scores: {high_scores}")


def main() -> None:
    ft_data_alchemist()


if __name__ == "__main__":
    main()
