import alchemy.grimoire


def main() -> None:
    print("=== Kaboom 0 ===")
    print("Accessing \'import alchemy.grimoire\'\n"
          "Calling \'alchemy.grimoire.light_spell_record()\'")
    print(f"Testing function: {alchemy.grimoire.light_spell_record(
        'Fantasy',
        'Earth, wind and fire'
    )}\n")


if __name__ == "__main__":
    main()
