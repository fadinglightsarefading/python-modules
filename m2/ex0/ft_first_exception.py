def input_temperature(temp_str: str) -> int | Exception:
    try:
        return int(temp_str)
    except (ValueError, TypeError) as e:
        print("Caught input_temperature error: ", end='')
        return e


def main() -> None:
    print("=== Garden Temperature ===")
    print("\nInput data is \'25\'")
    temp = input_temperature("25")
    print(f"Temperature is now {temp}")
    print("\nInput data is \'abc\'")
    temp = input_temperature("abc")
    print(f"{temp}")
    print("\nAll tests completed -- programme didn't crash!")


if __name__ == "__main__":
    main()
