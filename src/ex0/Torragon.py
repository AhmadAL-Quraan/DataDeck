from Creature import creature


class _torragon(creature):
    def __init__(self):
        super().__init__("Torragon", "Water")

    def attack(self) -> str:
        return "Torragon uses Hydro Pump!"
