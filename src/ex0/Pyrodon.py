from Creature import creature


class _pyrodon(creature):
    def __init__(self):
        super().__init__("Pyrodon", "Fire/Flying")

    def attack(self) -> str:
        return "Pyrodon uses Flamethrower!"
