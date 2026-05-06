import sys

def ft_command_quest() -> None:
    print("=== Command Quest ===")
    print(f"Programme name: {sys.argv[0]}")
    if len(sys.argv) == 1:
        print("No argument provided!")
    else:
        print(f"Arguments received: {len(sys.argv) - 1}")
        i = 1
        while i < len(sys.argv):
            print(f"Argument {i}: {sys.argv[i]}")
            i += 1
    print(f"Total arguments: {len(sys.argv)}")

def main() -> None:
    ft_command_quest()

if __name__ == "__main__":
    main()
