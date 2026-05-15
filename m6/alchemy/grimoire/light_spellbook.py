from .light_validator import validate_ingredients


def light_spell_allowed_ingredients() -> list[str, str, str, str]:
    return ["earth", "air", "fire", "water"]


def light_spell_record(spell_name: str, ingredients: str) -> str:
    whether_validated = validate_ingredients(ingredients)
    if "VALID" in whether_validated:
        return f"Spell recorded: {spell_name} ({whether_validated})"
    elif "INVALID" in whether_validated:
        return f"Spell not recorded: {spell_name} ({whether_validated})"
