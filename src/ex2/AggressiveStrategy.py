from .BattleStrategy import BattleStrategy
from ex1.TransformCapability import TransformCapability
from ex0.Creature import Creature
from typing import cast


class AggressiveStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        if isinstance(creature, TransformCapability):
            return True
        return False

    def act(self, creature: Creature) -> None:
        if not self.is_valid(creature):
            print(cast(TransformCapability, creature).transform())
            print(creature.attack())
            print(cast(TransformCapability, creature).revert())
        else:
            raise TypeError("Only transform can use the Aggressive Strategy")
