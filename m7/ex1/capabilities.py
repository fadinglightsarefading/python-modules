import abc


class HealCapability(abc.ABC):
    @abc.abstractmethod
    def heal(self) -> None:
        pass


class TransformCapability(abc.ABC):
    def __init__(self) -> None:
        self.transformed = False

    @abc.abstractmethod
    def transform(self) -> None:
        pass

    @abc.abstractmethod
    def revert(self) -> None:
        pass
