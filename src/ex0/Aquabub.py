from Creature import creature


class _aquabub(creature):
    def __init__(self):
        super().__init__("Aquabub", "Water")

    def attack(self) -> str:
        return "Aquabub uses Water Gun!"
