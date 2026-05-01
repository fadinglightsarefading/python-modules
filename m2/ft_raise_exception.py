def input_temperature(temp_str: str) -> int | Exception:
    try:
        temp = int(temp_str)
        if temp < 0:
            raise ValueError(f"{temp} C is too hot for plants (max 40 C)")
        elif temp > 40:
            raise ValueError(f"{temp} C is too hot for plants (min 0 c)")
        return temp
    except (ValueError, TypeError) as e:
        print("Caught input_temperature error: ", end='')
        return e

def test_temperature() -> None:
    print("=== Garden Temperature ===")
    print("\nInput data is \'25\'")
    temp = input_temperature("25")
    print(f"Temperature is now {temp}")
    print("\nInput data is \'abc\'")
    temp = input_temperature("abc")
    print(f"{temp}")
    print("\nInput data is \'100\'")
    temp = input_temperature("100")
    print(f"{temp}")
    print("\nInput data is \'-50\'")
    temp = input_temperature("-50")
    print(f"{temp}")
    print("\nAll tests completed -- programme didn't crash!")


def main() -> None:
    test_temperature()

if __name__ == "__main__":
    main()
