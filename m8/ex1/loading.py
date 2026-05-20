import sys
import importlib


def main() -> None:
    print("\nLOADING STATUS: Loading programmes...\n")
    with open("requirements.txt", "r") as f:
        requirements = f.read()
    ind_pacs = requirements.split('\n')
    pacs_vers = {}
    entry = []
    for pac in ind_pacs:
        entry = pac.split("==")
        if entry[0]:
            pacs_vers.update({entry[0]: entry[1]})
    print("Checking dependencies:")
    imperr = False
    for key in pacs_vers:
        skip = ["fonttools", "pillow", "python-dateutil"]
        try:
            if key not in skip:
                importlib.import_module(key)
        except ImportError as e:
            print(e)
            imperr = True
    if imperr:
        print("\nTo install required packages/dependencies:\n"
              "(using pip)\npip install -r requirements.txt\n"
              "(using Poetry)\npoetry install\n")
        return
    for key in pacs_vers:
        print(f"[OK] {key} ({pacs_vers[key]})", end=' ')
        if (key == "pandas"):
            print("- Data manipulation ready", end='')
        elif (key == "numpy"):
            print("- Numerical computation ready", end='')
        elif (key == "requests"):
            print("- Network access ready", end='')
        elif (key == "matplotlib"):
            print("- Visualissation ready", end='')
        print()
    print()


if __name__ == "__main__":
    main()
