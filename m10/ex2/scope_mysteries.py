def mage_counter() -> Callable:
    count = 0
    def counter():
        nonlocal count
        count += 1
        return count
    return counter


def spell_accumulator(initial_power: int) -> Callable:
    pass


def enchantment_factory(enchantment_type: str) -> Callable:
    pass


def memory_vault() -> dict[str, Callable]:
    pass


def main() -> None:
    print("Testing mage counter...")
    counter_a = mage_counter()
    counter_b = mage_counter()
    print(f"counter_a call 1: {counter_a()}\n"
          f"counter_a call 2: {counter_a()}\n"
          f"counter_b call 1: {counter_b()}\n")


if __name__ == "__main__":
    main()
