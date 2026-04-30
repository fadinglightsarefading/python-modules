def input_temperature(temp_str: str) -> int | Exception:
    try:
        print("Temperature is now ", end='')
        return int(temp_str)
    except (ValueError, TypeError) as e:
        print("Caught input_temperature error: ", end='')
        return e

def test_temperature() -> None:
    print("=== Garden Temperature ===")
    print("\nInput data is \'25\'")
    temp = input_temperature("25")
    print(f"{temp}")
    print("\nInput data is \'abc\'")
    temp = input_temperature("abc")
    print(f"{temp}")
    print("\nAll tests completed -- programme didb't crash!")


def main() -> None:
    test_temperature()

if __name__ == "__main__":
    main()
