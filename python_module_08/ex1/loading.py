#!/usr/bin/env python3
import importlib
import importlib.metadata
import sys

REQUIRED_PACKAGES: dict[str, str] = {
    "pandas": "Data manipulation ready",
    "numpy": "Numerical computation ready",
    "matplotlib": "Visualization ready",
}


def check_dependency(package: str, description: str) -> tuple[bool, str]:
    try:
        importlib.import_module(package)
        version = importlib.metadata.version(package)
        return True, f"[OK] {package} ({version}) - {description}"
    except ImportError:
        return False, f"[MISSING] {package} - {description}"


def show_install_instructions() -> None:
    print("\nDependencies are missing. Install them with pip:")
    print("    pip install -r requirements.txt")
    print("\nOr with Poetry:")
    print("    poetry install")
    print("    poetry run python loading.py")


def analyze_matrix_data() -> None:
    import numpy as np
    import pandas as pd

    print("\nAnalyzing Matrix data...")
    rng = np.random.default_rng(42)
    values = rng.normal(loc=0.0, scale=1.0, size=1000)
    print(f"Processing {len(values)} data points...")

    frame = pd.DataFrame({"signal": values})
    frame["rolling_mean"] = frame["signal"].rolling(window=10).mean()

    print("Generating visualization...")
    try:
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt

        plt.figure()
        plt.plot(frame["signal"], label="signal")
        plt.plot(frame["rolling_mean"], label="rolling mean")
        plt.legend()
        plt.title("Matrix Data Analysis")
        plt.savefig("matrix_analysis.png")
        plt.close()
        print("\nAnalysis complete!")
        print("Results saved to: matrix_analysis.png")
    except ImportError:
        print("\nmatplotlib unavailable, skipping visualization.")


def main() -> None:
    print("LOADING STATUS: Loading programs...\n")
    print("Checking dependencies:")

    all_ok = True
    for package, description in REQUIRED_PACKAGES.items():
        ok, message = check_dependency(package, description)
        print(message)
        all_ok = all_ok and ok

    if not all_ok:
        show_install_instructions()
        sys.exit(1)

    analyze_matrix_data()


if __name__ == "__main__":
    main()
