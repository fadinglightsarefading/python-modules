from functools import wraps
from typing import Callable, Any
from time import perf_counter


def spell_timer(func: Callable) -> Callable:
    @wraps(func)
    def timer_wrapper(*args, **kwargs) -> Any:
        print(f"Casting {func.__name__}()...")
        start = perf_counter()
        return_val = func(*args, **kwargs)
        end = perf_counter()
        print(f"Spell completed in {end - start:.3f} seconds")
        return return_val
    return timer_wrapper


@spell_timer
def fireball() -> str:
    return "Cast fireball"


def power_validator(min_power: int) -> Callable:
    def validator_decorator(func: Callable):
        @wraps(func)
        def validator_wrapper(*args, **kwargs) -> Callable | str:
            if args[2] < min_power:
                return "Insufficient power for this spell"
            return func(*args, **kwargs)
        return validator_wrapper
    return validator_decorator


def retry_spells(max_attempts: int) -> Callable:
    def retry_decorator(func: Callable) -> Callable:
        @wraps(func)
        def retry_wrapper(*args, **kwargs) -> Any:
            for n in range(1, max_attempts):
                try:
                    return func(*args, **kwargs)
                except Exception:
                    print(f"Spell failed, retrying..."
                          f"(attempt {n}/{max_attempts})")
            return f"Spell casting failed after {max_attempts} attempts"
        return retry_wrapper
    return retry_decorator


@retry_spells(max_attempts=3)
def spell_fail() -> None:
    raise ValueError


@retry_spells(max_attempts=3)
def spell_success() -> str:
    return "Cast some spell"


class MageGuild():
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        if (
                len(name) < 3 or not
                all(ch.isalpha() or ch.isspace() for ch in name)
        ):
            return False
        return True

    @power_validator(min_power=10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        return f"Successfully cast {spell_name} with {power} power"


def main() -> None:
    print("Testing spell timer...")
    print(fireball(), '\n')

    print("Testing retrying spell...")
    print(spell_fail(), spell_success(), sep='\n', end='\n\n')

    print("Testing MageGuild...")
    mg = MageGuild()
    print(mg.validate_mage_name("Rowan"),
          mg.validate_mage_name("Alex123"),
          sep='\n')
    print(mg.cast_spell("lightning", 15),
          mg.cast_spell("X", 5),
          sep='\n', end='\n\n')


if __name__ == "__main__":
    main()
