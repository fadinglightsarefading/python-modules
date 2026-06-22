def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    return sorted(
            artifacts,
            key=lambda artifact: artifact["power"],
            reverse=True
    )


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    return list(filter(lambda mage: mage["power"] >= min_power, mages))


def spell_transformation(spells: list[str]) -> list[str]:
    return list(map(lambda spell: "* " + spell + " *", spells))


def mage_stats(mages: list[dict]) -> dict:
    return {
        "max_power": max(map(lambda mage: mage["power"], mages)),
        "min_power": min(map(lambda mage: mage["power"], mages)),
        "avg_power": (sum(map(lambda mage: mage["power"], mages))
                      / len(mages))
    }


def main() -> None:
    artifacts = [
        {'name': 'Storm Crown', 'power': 115, 'type': 'accessory'},
        {'name': 'Water Chalice', 'power': 118, 'type': 'focus'},
        {'name': 'Ice Wand', 'power': 102, 'type': 'accessory'},
        {'name': 'Water Chalice', 'power': 80, 'type': 'accessory'}
    ]
    mages = [
        {'name': 'Morgan', 'power': 90, 'element': 'lightning'},
        {'name': 'Jordan', 'power': 67, 'element': 'shadow'},
        {'name': 'Alex', 'power': 83, 'element': 'wind'},
        {'name': 'River', 'power': 96, 'element': 'light'},
        {'name': 'River', 'power': 83, 'element': 'earth'}
    ]
    spells = ['flash', 'earthquake', 'freeze', 'heal']

    print(f"\tARTIFACTS:\n-Unsorted-\n{artifacts}\n\n"
          f"-Sorted-\n{artifact_sorter(artifacts)}\n")

    print(f"\tMAGES:\n-Unfiltered-\n{mages}\n\n"
          f"-Filtered-\n{power_filter(mages, 90)}\n")

    print(f"\tSPELLS:\n-Untransformed-\n{spells}\n\n"
          f"-Transformed-\n{spell_transformation(spells)}\n")

    print(f"\tMIN/MAX/AVG POWER:\n{mage_stats(mages)}\n")


if __name__ == "__main__":
    main()
