import ex0
from ex0 import CreatureFactory
import ex1
import ex2
from ex2 import NormalStrategy
from ex2 import DefensiveStrategy
from ex2 import AggressiveStrategy


def battle(
    opponenets: list[tuple[ex0.CreatureFactory, ex2.BattleStrategy]],
    battle_number: int,
) -> None:
    error: bool = False
    for i in range(len(opponenets)):
        if not opponenets[i][1].is_valid(opponenets[i][0].create_base()):
            error = True

    if error == False:
        print(
            f"Tournament {battle_number} {'(basic)' if len(opponenets) == 2 else '(multiple)'}"
        )
    else:
        print(f"Tournament {battle_number} {'(error)'}")

    print("[", end="")
    for opponent, strategy in opponenets:
        print(
            f" ({type(opponent).__name__}+{type(strategy).__name__})",
            end=", ",
        )

    print("]\n*** Tournament ***")
    print(f"{len(opponenets)} opponenets involved")
    for i in range(len(opponenets) - 1):
        for j in range(i + 1, len(opponenets)):
            print("\n* Battle *")
            print(opponenets[i][0].create_base().describe())
            print("vs.")
            print(opponenets[j][0].create_base().describe())
            print("now fight!")
            try:
                opponenets[i][1].act(opponenets[i][0].create_base())
                opponenets[j][1].act(opponenets[j][0].create_base())
            except TypeError as e:
                print(e)


if __name__ == "__main__":
    battle_number = 0
    # Healing factory
    healing_factory = ex1.HealingCreatureFactory()
    # Transform factory
    transform_factory = ex1.TransformCreatureFactory()
    # Aqua factory
    aqua_factory = ex0.AquaFactory()
    # Flameling
    flameling_factory = ex0.FlameFactory()
    # Battle strategy
    strategy_norm = NormalStrategy()
    strategy_def = DefensiveStrategy()
    strategy_agger = AggressiveStrategy()
    # Torn 0
    opponenets = [
        (flameling_factory, strategy_norm),
        (healing_factory, strategy_def),
    ]
    battle(opponenets, battle_number)
    battle_number += 1

    # Torn1
    opponenets = [
        (flameling_factory, strategy_agger),
        (healing_factory, strategy_def),
    ]
    battle(opponenets, battle_number)
    battle_number += 1

    # Torn2
    opponenets = [
        (aqua_factory, strategy_norm),
        (healing_factory, strategy_def),
        (transform_factory, strategy_agger),
    ]

    battle(opponenets, battle_number)
    battle_number += 1
    print(type(flameling_factory).__name__)
