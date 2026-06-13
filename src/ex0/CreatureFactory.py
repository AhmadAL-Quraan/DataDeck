from abc import ABC, abstractmethod

from .creature import creature
from .torragon import _torragon
from .aquabub import _aquabub
from .pyrodon import _pyrodon
from .flameling import _flameling


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
