from .dark_spellbook import dark_spell_allowed_ingredients


def validate_ingredients(ingredients: str) -> str:
    ingredients_smallcaps = ingredients.lower()
    allowed_ingredients = dark_spell_allowed_ingredients()
    for allowed in allowed_ingredients:
        if allowed in ingredients_smallcaps:
            return (ingredients + " - VALID")
    return (ingredients + " - INVALID")
