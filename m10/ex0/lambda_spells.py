def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    return sorted(artifacts, key=lambda artifacts: artifacts["power"], reverse=True)


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    return list(filter(lambda mage: mage[1] >= min_power, mages.items()))

'''
def spell_transformation(spells: list[str]) -> list[str]:
    pass


def mage_stats(mages: list[dict]) -> dict:
    pass
'''

def main() -> None:
    artifacts = [
        {'name': 'Storm Crown', 'power': 115, 'type': 'accessory'},
        {'name': 'Water Chalice', 'power': 118, 'type': 'focus'},
        {'name': 'Ice Wand', 'power': 102, 'type': 'accessory'},
        {'name': 'Water Chalice', 'power': 80, 'type': 'accessory'}
    ]
    print(f"Unsorted:\n{artifacts}\n\n"
          f"Sorted:\n{artifact_sorter(artifacts)}\n")
    mages = [
        {'name': 'Morgan', 'power': 90, 'element': 'lightning'},
        {'name': 'Jordan', 'power': 67, 'element': 'shadow'},
        {'name': 'Alex', 'power': 83, 'element': 'wind'},
        {'name': 'River', 'power': 96, 'element': 'light'},
        {'name': 'River', 'power': 83, 'element': 'earth'}
    ]
    spells = ['flash', 'earthquake', 'freeze', 'heal']


if __name__ == "__main__":
    main()
