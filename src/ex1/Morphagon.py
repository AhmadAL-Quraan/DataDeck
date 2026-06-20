from ex0.Creature import Creature
from .TransformCapability import TransformCapability


class _Morphagon(TransformCapability, Creature):
    def __init__(self) -> None:
        Creature.__init__(self, "Morphagon", "Normal/Dragon")
        self.transformed = False

    def transform(self) -> str:
        self.transformed = True
        return "Morphagon shifts into a dragonic battle form!"

    def revert(self) -> str:
        self.transformed = False
        return "Morphagon stabilizes its form"

    def attack(self) -> str:
        if self.transformed:
            return "Morphagon unleashes a devastating morph strike!"
        return "Morphagon attacks normally"
