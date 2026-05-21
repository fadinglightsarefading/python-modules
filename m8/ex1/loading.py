import sys
import importlib


def package_versions(pacs_vers: dict[str]) -> None:
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


def generate_data() -> None:
    import pandas
    import numpy
    import matplotlib.pyplot

    print("Analyzing Matrix data...")
    matrix_data = numpy.random.randint(0, 50, size=200)
    print(f"Processing {len(matrix_data)} data points..."
          f"\nGenerating visualisation...")
    mdc = pandas.DataFrame(matrix_data, columns=["matrix value"])
    matplotlib.pyplot.figure(figsize=(7, 5))
    matplotlib.pyplot.plot(mdc["matrix value"])
    matplotlib.pyplot.title("Matrix Data")
    matplotlib.pyplot.xlabel("Ticks")
    matplotlib.pyplot.ylabel("Redpills Taken")
    ma = "matrix_analysis.png"
    matplotlib.pyplot.savefig(ma)
    print(f"\nAnalysis complete!\nresults saved to: {ma}")


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
    package_versions(pacs_vers)
    generate_data()


if __name__ == "__main__":
    main()
