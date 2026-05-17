import alchemy


def main() -> None:
    print("=== Distillation 1 ===")
    print("Testing \'import alchemy\'")
    print(f"Calling strength_potion(): {alchemy.strength_potion()}")
    print(f"Calling heal() alias: {alchemy.heal()}")
    print()


if __name__ == "__main__":
    main()
