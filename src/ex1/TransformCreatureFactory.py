from ex0.CreatureFactory import CreatureFactory
from ex0.Creature import Creature

from .Morphagon import _Morphagon
from .Shiftling import _Shiftling


class TransformCreatureFactory(CreatureFactory):
    def create_base(self) -> Creature:
        return _Shiftling()

    def create_evolved(self) -> Creature:
        return _Morphagon()
