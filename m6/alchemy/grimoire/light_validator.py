def validate_ingredients(ingredients: str) -> str:
    from .light_spellbook import light_spell_allowed_ingredients
    ingredients_smallcaps = ingredients.lower()
    allowed_ingredients = light_spell_allowed_ingredients()
    for allowed in allowed_ingredients:
        if allowed in ingredients_smallcaps:
            return (ingredients + " - VALID")
    return (ingredients + " - INVALID")
