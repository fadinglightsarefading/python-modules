def garden_operations(operation_number: int) -> None:
    if operation_number == 0:
        int("abc")
    elif operation_number == 1:
        i = 10 / 0
    elif operation_number == 2:
        open("i_dont_exist.txt")
    elif operation_number == 3:
        i = "mnam" + 5
    else:
        print("Operation completed successfully")


def test_error_types() -> None:
    print("=== Garden Error Types Demo ===")
    i = 0
    while i < 5:
        print(f"Testing operation {i}...")
        try:
            garden_operations(i)
        except ValueError as e:
            print(f"Caught ValueError: {e}")
        except ZeroDivisionError as e:
            print(f"Caught ZeroDivisionError: {e}")
        except FileNotFoundError as e:
            print(f"Caught FileNotFoundError: {e}")
        except TypeError as e:
            print(f"Caught TypeError: {e}")
        i += 1
    print("\nAll error types tested successfully!")

def main() -> None:
    test_error_types()

if __name__ == "__main__":
    main()
