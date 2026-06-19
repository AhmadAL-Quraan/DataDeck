from ex0.CreatureFactory import CreatureFactory
from ex0.Creature import Creature

from .Morphagon import Morphagon
from .Shiftling import Shiftling


class TransformCreatureFactory(CreatureFactory):
    def create_base(self) -> Creature:
        return Shiftling()

    def create_evolved(self) -> Creature:
        return Morphagon()
