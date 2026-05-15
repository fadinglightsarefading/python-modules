import typing
import abc

class Creature(abc.ABC):
    def __init__(self):
        pass

    @abc.abstractmethod
    def attack(self):
        pass
