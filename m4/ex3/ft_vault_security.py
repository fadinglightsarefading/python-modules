def secure_archive(file_name: str, action: str,
                   content: str | None = None) -> tuple[bool, str]:
    if action == "read":
        try:
            with open(file_name, 'r') as f:
                return True, f.read()
        except OSError as e:
            return False, str(e)
    elif action == "write":
        if content is None:
            return False, "invalid"
        try:
            with open(file_name, 'w') as new:
                new.write(content)
                return True, "Content has successfully been written to file."
        except OSError as e:
            return False, str(e)
    return False, "invalid"


def main() -> None:
    print("=== Cyber Archive Security ===")
    print(f"\nUsing 'secure_archive' to read from a nonexistant file:"
          f"\n{secure_archive("nonexistant.txt", "read")}")
    print(f"\nUsing 'secure_archive' to read from an inaccessible file:"
          f"\n{secure_archive("secret.txt", "read")}")
    print("\nUsing 'secure_archive' to read from a regular file:")
    contents = secure_archive("ancient_fragments.txt", "read")
    print(contents)
    print("\nUsing 'secure_archive' to write previous content to a new file:"
          f"\n{secure_archive("new.txt", "write", contents[1])}")


if __name__ == "__main__":
    main()
