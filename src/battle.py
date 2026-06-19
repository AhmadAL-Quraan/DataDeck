import ex0


def reciveFunc(factoryObject: ex0.CreatureFactory) -> None:
    print("Testing factory")
    # Base flame
    base = factoryObject.create_base()
    print(base.describe())
    print(base.attack())
    evolved = factoryObject.create_evolved()

    print(evolved.describe())
    print(evolved.attack())


def battle(
    flameFactor: ex0.CreatureFactory,
    aquaFactor: ex0.CreatureFactory,
) -> None:

    print("Testing battle")
    fighter1 = flameFactor.create_base()
    fighter2 = aquaFactor.create_base()
    print(f"{fighter1.describe()} \nvs. \n{fighter2.describe()}")
    print("fight!")
    print(f"{fighter1.attack()}")
    print(f"{fighter2.attack()}")


if __name__ == "__main__":
    flame_family = ex0.FlameFactory()
    reciveFunc(flame_family)
    print()
    aqua_family = ex0.AquaFactory()
    reciveFunc(aqua_family)
    print()
    battle(flame_family, aqua_family)
