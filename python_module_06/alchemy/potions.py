#!/usr/bin/env python3
import elements

from .elements import create_air, create_earth


def healing_potion() -> str:
    return (
        f"Healing potion brewed with '{create_earth()}' and "
        f"'{create_air()}'"
    )


def strength_potion() -> str:
    return (
        f"Strength potion brewed with '{elements.create_fire()}' and "
        f"'{elements.create_water()}'"
    )
