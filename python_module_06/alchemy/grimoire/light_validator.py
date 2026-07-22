#!/usr/bin/env python3

LIGHT_ALLOWED_INGREDIENTS = ["earth", "air", "fire", "water"]


def validate_ingredients(ingredients: str) -> str:
    lowered = ingredients.lower()
    if any(item in lowered for item in LIGHT_ALLOWED_INGREDIENTS):
        return f"{ingredients} - VALID"
    return f"{ingredients} - INVALID"
