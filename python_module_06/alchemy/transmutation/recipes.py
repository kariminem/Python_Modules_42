#!/usr/bin/env python3
import elements

from ..elements import create_air
from ..potions import strength_potion


def lead_to_gold() -> str:
    return (
        "Recipe transmuting Lead to Gold: brew "
        f"'{create_air()}' and '{strength_potion()}' "
        f"mixed with '{elements.create_fire()}'"
    )
