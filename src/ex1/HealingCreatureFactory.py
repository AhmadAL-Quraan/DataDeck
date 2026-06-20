from ex0.CreatureFactory import CreatureFactory
from ex0.Creature import Creature
from ex1.Bloomelle import _Bloomelle
from ex1.Sproutling import _Sproutling


class HealingCreatureFactory(CreatureFactory):
    def create_base(self) -> Creature:
        return _Sproutling()

    def create_evolved(self) -> Creature:
        return _Bloomelle()
