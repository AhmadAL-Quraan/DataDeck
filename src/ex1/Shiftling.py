from .TransformCapability import TransformCapability
from ex0.Creature import Creature


class Shiftling(TransformCapability, Creature):
    def __init__(self) -> None:
        Creature.__init__(self, "Shiftling", "Normal")
        self.transformed = False

    def transform(self) -> str:
        self.transformed = True
        return "Shiftling shifts into a sharper form!"

    def revert(self) -> str:
        self.transformed = False
        return "Shiftling returns to normal"

    def attack(self) -> str:
        if self.transformed:
            return "Shiftling performs a boosted strike!"
        return "Shiftling attacks normally"
