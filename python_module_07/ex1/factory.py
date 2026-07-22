#!/usr/bin/env python3
from typing import Union

from ex0.factory import CreatureFactory

from .creature import Sproutling, Bloomelle, Shiftling, Morphagon

HealingCreature = Union[Sproutling, Bloomelle]
TransformCreature = Union[Shiftling, Morphagon]


class HealingCreatureFactory(CreatureFactory):
    def create_base(self) -> HealingCreature:
        return Sproutling()

    def create_evolved(self) -> HealingCreature:
        return Bloomelle()


class TransformCreatureFactory(CreatureFactory):
    def create_base(self) -> TransformCreature:
        return Shiftling()

    def create_evolved(self) -> TransformCreature:
        return Morphagon()
