def input_temperature(temp_str: str) -> str | Exception:
    try:
        temp = int(temp_str)
        if temp > 40:
            raise ValueError(f"{temp} C is too hot for plants (max 40 C)")
        elif temp < 0:
            raise ValueError(f"{temp} C is too cold for plants (min 0 c)")
        return f"Temperature is now {temp} C"
    except (ValueError, TypeError) as e:
        print("Caught input_temperature error: ", end='')
        return e


def test_temperature(temperature: str) -> None:
    print(input_temperature(temperature))


def main() -> None:
    print("=== Garden Temperature ===")

    print("\nInput data is \'25\'")
    test_temperature("25")

    print("\nInput data is \'abc\'")
    test_temperature("abc")

    print("\nInput data is \'100\'")
    test_temperature("100")

    print("\nInput data is \'-50\'")
    test_temperature("-50")

    print("\nAll tests completed -- programme didn't crash!")


if __name__ == "__main__":
    main()
