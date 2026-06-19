import ex0
import ex1


def healing_capabilities(factoryObj: ex0.Creature) -> None:
    print(factoryObj.describe())
    print(factoryObj.attack())
    if isinstance(factoryObj, ex1.HealCapability):
        print(factoryObj.heal("itself"))


def transform_capabilities(factoryObj: ex0.Creature) -> None:
    print(factoryObj.describe())
    print(factoryObj.attack())
    if isinstance(factoryObj, ex1.TransformCapability):
        print(factoryObj.transform())
    print(factoryObj.attack())
    if isinstance(factoryObj, ex1.TransformCapability):
        print(factoryObj.revert())


if __name__ == "__main__":
    print("Testing Creature with healing capability")
    print("base:")
    obj_healing = ex1.HealingCreatureFactory()
    healing_capabilities(obj_healing.create_base())
    print("evolved:")
    healing_capabilities(obj_healing.create_evolved())
    print("\nTesting Creature with transform capability")
    print("base:")
    obj_transform = ex1.TransformCreatureFactory()
    transform_capabilities(obj_transform.create_base())
    print("evolved:")
    transform_capabilities(obj_transform.create_evolved())
