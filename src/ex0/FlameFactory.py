from .Flameling import _Flameling
from .Creature import Creature

from .Pyrodon import _Pyrodon

from .CreatureFactory import CreatureFactory


class FlameFactory(CreatureFactory):

    def create_base(self) -> Creature:
        return _Flameling()

    def create_evolved(self) -> Creature:
        return _Pyrodon()
