import alchemy.transmutation.recipes


def main() -> None:
    print("=== Transmutation 0 ===")
    print("Testing \'import alchemy.transmutation.recipes\'"
          "\nCalling \'alchemy.recipes.lead_to_gold()\'")
    print(f"Testing lead to gold: {alchemy.transmutation.recipes.lead_to_gold()}")
    print()


if __name__ == "__main__":
    main()
