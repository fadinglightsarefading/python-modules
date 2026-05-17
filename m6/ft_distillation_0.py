from alchemy.potions import strength_potion, healing_potion


def main() -> None:
    print("=== Distillation 0 ===")
    print("Testing \'from alchemy.potions import <functions>\'")
    print(f"Calling strength_potion(): {strength_potion()}")
    print(f"Calling healing_potion(): {healing_potion()}")
    print()


if __name__ == "__main__":
    main()
