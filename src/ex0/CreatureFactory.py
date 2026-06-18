from abc import ABC, abstractmethod

from Creature import creature
from Torragon import _torragon
from Aquabub import _aquabub
from Pyrodon import _pyrodon
from Flameling import _flameling


class creatureFactory(ABC):
    @abstractmethod
    def create_base(self) -> creature:
        pass

    @abstractmethod
    def create_evolved(self) -> creature:
        pass


# Family making


class flameFactory(creatureFactory):

    def create_base(self) -> creature:
        return _flameling()

    def create_evolved(self) -> creature:
        return _pyrodon()


class aquaFactory(creatureFactory):

    def create_base(self) -> creature:
        return _aquabub()

    def create_evolved(self) -> creature:
        return _torragon()
