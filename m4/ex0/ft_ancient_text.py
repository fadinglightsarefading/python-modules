import sys
import typing


def ft_ancient_text() -> None:
    print("=== Cyber Archives Recovery ===")
    print(f"Accessing file \'{sys.argv[1]}\'")
    try:
        f = open(sys.argv[1], "r")
    except OSError as e:
        print(f"Error opening file \'{sys.argv[1]}\': {e}\n")
        return
    print(f"---\n\n{f.read()}---")
    f.close()
    print(f"File \'{sys.argv[1]}\' closed.\n")


def main() -> None:
    if len(sys.argv) == 1:
        print("Usage: python3 ft_ancient_text.py <file>\n")
        return
    ft_ancient_text()


if __name__ == "__main__":
    main()
