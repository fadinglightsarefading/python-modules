from ex0.creatures import Creature, Flameling, Pyrodon, Aquabub, Torragon
from ex1.creatures import Sproutling, Bloomelle, Shiftling, Morphagon
from ex1.capabilities import HealCapability, TransformCapability
import abc


class BattleError(Exception, Creature):
    def __init__(self, message: str = "Caught BattleError"):
    Exception.__init__(self, message)


class BattleStrategy(abc.ABC):
    @abc.abstractmethod
    def is_valid(self, creature: Creature) -> bool:
        pass

    @abc.abstractmethod
    def act(self, creature: Creature) -> None:
        pass


class NormalStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        return True

    def act(self, creature: Creature) -> None:
        creature.attack()


class AggressiveStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, TransformCapability)

    def act(self, creature: Creature) -> None:
        if AggressiveStrategy().is_valid(creature):
            creature.transform()
            creature.attack()
            creature.revert()
        else:
            raise BattleError()


class DefensiveStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> None:
        return isinstance(creature, HealCapability)

    def act(self, creature: creature) -> None:
        if AggressiveStrategy().is_valid(creature):
            creature.attack()
            creature.heal()
        else:
            raise BattleError()
