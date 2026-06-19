from .Torragon import _Torragon
from .Aquabub import _Aquabub
from .CreatureFactory import CreatureFactory
from .Creature import Creature


class AquaFactory(CreatureFactory):

    def create_base(self) -> Creature:
        return _Aquabub()

    def create_evolved(self) -> Creature:
        return _Torragon()
