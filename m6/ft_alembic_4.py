import alchemy


def main() -> None:
    print("=== Alembic 4 ===")
    print("Testing \'import alchemy\'")
    print(f"Calling create_air(): {alchemy.create_air()}")
    print("Calling create_earth(): ", end='')
    try:
        alchemy.create_earth()
    except AttributeError as e:
        print(f"AttributeError: {e}")
    print()


if __name__ == "__main__":
    main()
