from .dark_validator import validate_ingredients


def dark_spell_allowed_ingredients() -> list[str]:
    return ["bats", "frogs", "arsenic", "eyeball"]


def dark_spell_record(spell_name: str, ingredients: str) -> str:
    whether_validated = validate_ingredients(ingredients)
    if "VALID" in whether_validated:
        return f"Spell recorded: {spell_name} ({whether_validated})"
    elif "INVALID" in whether_validated:
        return f"Spell not recorded: {spell_name} ({whether_validated})"
    else:
        return "Neither valid nor invalid."
    
