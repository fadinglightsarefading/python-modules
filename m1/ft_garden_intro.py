def ft_garden_intro(name: str, height: int, age: int):
    print("=== Welcome to My Garden ===")
    print(f"Plant: {name}\nHeight: {height}cm\nAge: {age} days")
    print("\n=== End of Program ===")


def main():
    ft_garden_intro("Rose", 25, 30)


if __name__ == "__main__":
    main()
