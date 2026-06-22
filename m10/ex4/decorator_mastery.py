from functools import wraps
from typing import Callable


class MageGuild():
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        pass

    def cast_spell(self, spell_name: str, power: int) -> str:
        pass


def spell_timer(func: Callable) -> Callable:
    @wraps(func)
    def new_func() -> Callable:
        print(f"Casting {func.__name__}...")


def power_validator(min_power: int) -> Callable:
    pass


def retry_spells(max_attempts: int) -> Callable:
    pass


def main() -> None:
    pass


if __name__ == "__main__":
    main()
