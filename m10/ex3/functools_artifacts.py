from functools import reduce, partial, lru_cache, singledispatch
from operator import add, mul
from typing import Callable, Any


def spell_reducer(spells: list[int], operation: str) -> int:
    operations = {"add": add, "multiply": mul,
                  "max": max, "min": min}
    return reduce(operations[operation], spells)


def partial_enchanter(base_enchantment: Callable) -> dict[str, Callable]:
    return {1: partial(base_enchantment, 50, "Water"),
            2: partial(base_enchantment, 50, "Earth"),
            3: partial(base_enchantment, 50, "Fire")}


def use_enchantment(power: int, element: str, target: str) -> str:
    return f"Used LVL{power} {element} on {target}"


@lru_cache
def memoized_fibonacci(n: int) -> int:
    if n < 2:
        return n
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


def spell_dispatcher() -> Callable[[Any], str]:
    @singledispatch
    def dispatch(spell: Any) -> str:
        return "Unknown spell type"

    @dispatch.register
    def damage_spell(spell: int) -> str:
        return f"{spell} damage"

    @dispatch.register
    def enchantment(spell: str) -> str:
        return spell

    @dispatch.register
    def multicast(spell: list) -> str:
        return f"{len(spell)} spells"

    return dispatch


def main() -> None:
    spell_powers = [22, 41, 27, 11, 46, 12]
    operations = ['add', 'multiply', 'max', 'min']
    fibonacci_tests = [19, 11, 15]

    print("Testing spell reducer...")
    print(f"Sum: {spell_reducer([10, 20, 30, 40], "add")}\n"
          f"Product: {spell_reducer([10, 20, 30, 40], "multiply")}\n"
          f"Max: {spell_reducer([10, 20, 30, 40], "max")}\n"
          f"Min: {spell_reducer([10, 20, 30, 40], "min")}\n")

    print("Testing partial enchanter...")
    spells = partial_enchanter(use_enchantment)
    print(spells[1]("Jonathan"),
          spells[2]("Peter"),
          spells[3]("Gabriel"),
          sep='\n', end='\n\n')

    print("Testing memoized fibonacci...")
    print(f"Fib(0): {memoized_fibonacci(0)}\n"
          f"Fib(1): {memoized_fibonacci(1)}\n"
          f"Fib(10): {memoized_fibonacci(10)}\n"
          f"Fib(15): {memoized_fibonacci(15)}\n")

    print("Testing spell dispatcher...")
    print(f"Damage spell: {spell_dispatcher()(42)}\n"
          f"Enchantment: {spell_dispatcher()("fireball")}\n"
          f"Multi-cast: {spell_dispatcher()(["un", "deux", "trois"])}\n"
          f"{spell_dispatcher()(3.14)}\n")


if __name__ == "__main__":
    main()
