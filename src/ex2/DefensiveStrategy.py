from typing import cast

from ex0.Creature import Creature
from ex1.HealCapability import HealCapability
from ex2.BattleStrategy import BattleStrategy


class DefensiveStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, HealCapability)

    def act(self, creature: Creature):
        if not self.is_valid(creature):
            raise TypeError(
                f"Invalid {creature.name} for this defensive strategy"
            )

        creature.attack()
        cast(HealCapability, creature).heal("itself")
