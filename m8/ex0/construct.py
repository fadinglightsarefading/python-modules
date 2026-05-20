import site
import sys
import os


def blue_pill() -> None:
    print("MATRIX STATUS: You're still plugged in!\n")
    print(f"Current Python: {sys.executable}")
    print("Virtual Environment: None detected\n")
    print("WARNING: You're in the global environment!\n"
          "This machine can see everything you install.\n")
    print("To enter the construct, run:\n"
          "python3 -m venv matrix_env\n"
          "source matrix_env/bin/activate\t# On Unix\n"
          "matrix_env\\Scripts\\activate\t# On Windows\n"
          "\nThen run the programme again.")


def red_pill() -> None:
    print("MATRIX STATUS: Welcome to the construct\n")
    print(f"Current Python: {sys.executable}\n"
          f"Virtual Environment: {os.path.basename(sys.prefix)}\n"
          f"Environment Path: {sys.prefix}\n")
    print("SUCCESS: You're in an isolated environment!\n"
          "Safe to install packages without affecting the global system.\n")
    print(f"Package installation path:\n{site.getsitepackages()[0]}")


def main() -> None:
    if sys.prefix != sys.base_prefix:
        red_pill()
    else:
        blue_pill()


if __name__ == "__main__":
    main()
