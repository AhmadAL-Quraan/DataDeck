from .creature import creature


class _flameling(creature):
    def __init__(self):
        super().__init__("Flameling", "Fire")

    def attack(self) -> str:
        return "Flameling uses Ember!"
