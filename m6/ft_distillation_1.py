import alchemy


def main() -> None:
    print("=== Distillation 1 ===")
    print(f"Testing strength_potion(): {alchemy.strength_potion()}")
    print(f"Testing heal() alias: {alchemy.heal()}")
    print()


if __name__ == "__main__":
    main()
