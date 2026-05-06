import sys
import typing


def ft_ancient_text() -> None:
    print("=== Cyber Archives Recovery & Preservation ===")
    print(f"Accessing file \'{sys.argv[1]}\'")
    try:
        f = open(sys.argv[1], "r")
    except OSError as e:
        sys.stderr.write(f"[STDERR] Error opening file \'{sys.argv[1]}\': "
                         f"{e}\n")
        return
    content = f.read()
    print(f"---\n\n{content}\n---")
    f.close()
    print(f"File \'{sys.argv[1]}\' closed.\n")
    new_content = content.replace("\n", "#\n")
    print(f"Transform data:\n---\n\n{new_content}\n---")
    print("Enter new file name (or empty):", end=' ', flush=True)
    file_name = sys.stdin.readline().strip()
    if not len(file_name):
        print("Not saving data.")
        return
    print(f"Saving data to \'{file_name}\'")
    try:
        f = open(file_name, "w")
    except OSError as e:
        sys.stderr.write(f"[STDERR] Error opening file \'{file_name}\': {e}\n")
        sys.stderr.flush()
        print("Data not saved.")
        return
    print(f"Saving data to \'{file_name}\'")
    f.write(new_content)
    print(f"Data saved in file \'{file_name}\'")
    f.close()


def main() -> None:
    if len(sys.argv) == 1:
        print("Usage: python3 ft_ancient_text.py <file>\n")
        return
    ft_ancient_text()


if __name__ == "__main__":
    main()
