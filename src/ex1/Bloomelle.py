from ex0.Creature import Creature
from .HealCapability import HealCapability


class Bloomelle(HealCapability, Creature):
    def __init__(self) -> None:
        super().__init__("Bloomelle", "Grass/Fairy")

    def heal(self, target: str) -> str:

        return f"Bloomelle heals {target} and others for a large amount"

    def attack(self) -> str:
        return "Bloomelle uses Petal Dance!"
