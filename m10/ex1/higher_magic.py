from typing import Callable


def heal(target: str, power: int) -> str:
    return f"Heal restores {target} {power} HP"


def fireball(target: str, power: int) -> str:
    return f"Fireball damages {target} by {power} HP"


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    def combined(tgt1: str, pwr1: int, tgt2: str, pwr2: int) -> tuple[str]:
        return spell1(tgt1, pwr1), spell2(tgt2, pwr2)
    return combined


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    def amplified(target: str, power: int) -> str:
        return base_spell(target, power * multiplier)
    return amplified


def conditional_caster(condition: Callable, spell: Callable) -> Callable | str:
    if callable(condition):
        return spell
    else:
        return "Spell fizzled"


def spell_sequence(spells: list[Callable]) -> Callable:
    def sequence(target: str, power: int) -> list[str]:
        spell_casts: list[str] = []
        for spell in spells:
            spell_casts.append(spell(target, power))
        return spell_casts
    return sequence


def main() -> None:
    combined = spell_combiner(heal, fireball)
    print(f"Spell combiner:\n{combined("Dragon", 15, "Goblin", 12)}\n")

    amplified = power_amplifier(fireball, 3)
    print(f"Power amplifier:\n{amplified("Wizard", 14)}\n")

    print(f"Conditional:\n"
          f"Calling real spell: {conditional_caster(heal, heal)}\n"
          f"Calling fake spell: {conditional_caster(1, 1)}\n")

    sequence = spell_sequence([heal, fireball, heal, fireball])
    print(f"Spell sequence (heal, fireball, heal, fireball):\n"
          f"{sequence("Knight", 16)}")


if __name__ == "__main__":
    main()
