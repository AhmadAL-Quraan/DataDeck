from ex0.Creature import Creature
from .HealCapability import HealCapability


class Sproutling(HealCapability, Creature):
    def __init__(self) -> None:
        super().__init__("Sproutling", "Grass")

    def attack(self) -> str:
        return "Sproutling uses Vine Whip!"

    def heal(self, target: str) -> str:
        return f"Sproutling heals {target} and others for a large amount"
