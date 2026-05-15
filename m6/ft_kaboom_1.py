import alchemy.grimoire.dark_spellbook


def main() -> None:
    print("=== Kaboom 1 ===")
    print("Testing \'import alchemy.grimoire.dark_spellbook\'\n"
          "Calling \'alchemy.grimoire.dark_spellbook.dark_spell_record()\'")
    result = alchemy.grimoire.dark_spellbook.dark_spell_record(
        'Death',
        'Bats, rust and arsenic')
    print(f"Testing function: {result}")


if __name__ == "__main__":
    main()
