import sys
import importlib


def versions_comparison(package: str, version: str, message: str) -> None:
    print(f"[OK] {package} ({version}) - {message}")


def generate_data() -> None:
    import pandas
    import numpy
    from matplotlib import pyplot

    print("Analyzing Matrix data...")
    matrix_data = numpy.random.randint(0, 50, size=200)
    print(f"Processing {len(matrix_data)} data points..."
          f"\nGenerating visualisation...")
    mdc = pandas.DataFrame(matrix_data, columns=["matrix value"])
    pyplot.figure(figsize=(7, 5))
    pyplot.plot(mdc["matrix value"])
    pyplot.title("Matrix Data")
    pyplot.xlabel("Ticks")
    pyplot.ylabel("Redpills Taken")
    ma = "matrix_analysis.png"
    pyplot.savefig(ma)
    print(f"\nAnalysis complete!\nresults saved to: {ma}\n")


def main() -> None:
    print("\nLOADING STATUS: Loading programmes...\n")

    packages = {
        "pandas": "Data manipulation ready",
        "matplotlib": "Visualisation ready",
        "numpy": "Numerical computation ready"
    }

    print("Checking dependencies:")

    import_error = False
    for package, message in packages.items():
        try:
            module = importlib.import_module(package)
        except ImportError as e:
            print(f"{e} - {package} is not installed")
            import_error = True
            module = None
        if module:
            version = module.__version__
            versions_comparison(package, version, message)

    if import_error:
        print("\nTo install required packages/dependencies:\n"
              "(using pip)\npip install -r requirements.txt\n"
              "(using Poetry)\npoetry install\n")
        sys.exit(1)

    generate_data()


if __name__ == "__main__":
    main()
