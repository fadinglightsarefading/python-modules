import alchemy


def main() -> None:
    print("=== Alembic 4 ===")
    print(f"Testing create_air(): {alchemy.create_air()}")
    print("Testing create_earth(): ", end='')
    try:
        alchemy.create_earth()
    except AttributeError as e:
        print(f"AttributeError: {e}")
    print()


if __name__ == "__main__":
    main()
