from typing import Callable


def mage_counter() -> Callable:
    count = 0

    def counter() -> int:
        nonlocal count
        count += 1
        return count
    return counter


def spell_accumulator(initial_power: int) -> Callable:
    def accumulator(given_power: int) -> int:
        nonlocal initial_power
        initial_power += given_power
        return initial_power
    return accumulator


def enchantment_factory(enchantment_type: str) -> Callable:
    def enchantment_table(item: str) -> str:
        return f"{enchantment_type} {item}"
    return enchantment_table


def memory_vault() -> dict[str, Callable]:
    vault: dict[str, int] = {}

    def store(key: str, value: int) -> None:
        vault[key] = value

    def recall(key: str) -> int | str:
        if key not in vault:
            return "Memory not found"
        return vault[key]

    return {"store": store, "recall": recall}


def main() -> None:
    print("Testing mage counter...")
    counter_a = mage_counter()
    counter_b = mage_counter()
    print(f"counter_a call 1: {counter_a()}\n"
          f"counter_a call 2: {counter_a()}\n"
          f"counter_b call 1: {counter_b()}\n")

    print("Testing spell accumulator...")
    accumulator_a = spell_accumulator(100)
    accumulator_b = spell_accumulator(100)
    print(f"Base 100, add 20: {accumulator_a(20)}, {accumulator_a(20)}...")
    print(f"Base 100, add 30: {accumulator_b(30)}, {accumulator_b(30)}...\n")

    print("Testing enchantment factory...")
    enchantment1 = enchantment_factory("Flaming")
    enchantment2 = enchantment_factory("Frozen")
    print(f"{enchantment1("Sword")}\n{enchantment2("Shield")}\n")

    print("Testing memory vaults...")
    memvault: dict[str, Callable] = memory_vault()
    print("Store 'secret' = 42")
    memvault["store"]("secret", 42)
    print(f"Recall 'secret': {memvault["recall"]("secret")}\n"
          f"Recall 'unknown': {memvault["recall"]("unknown")}")


if __name__ == "__main__":
    main()
