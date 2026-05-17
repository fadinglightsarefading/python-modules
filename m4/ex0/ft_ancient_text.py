import sys
import typing


def main() -> None:
    print("=== Cyber Archives Recovery ===")
    if len(sys.argv) == 1:
        print("Usage: python3 ft_ancient_text.py <file>\n")
        return
    print(f"Accessing file \'{sys.argv[1]}\'")
    try:
        f: typing.IO[str] = open(sys.argv[1], "r")
    except OSError as e:
        print(f"Error opening file \'{sys.argv[1]}\': {e}\n")
        return
    print(f"---\n\n{f.read()}\n---")
    f.close()
    print(f"File \'{sys.argv[1]}\' closed.\n")


if __name__ == "__main__":
    main()
