"""Print a compact summary of the local learning environment."""

from __future__ import annotations

import importlib.util
import platform
import sys


def package_status(name: str) -> str:
    return "ok" if importlib.util.find_spec(name) else "missing"


def main() -> None:
    packages = ["torch", "numpy", "matplotlib", "graphviz", "tqdm", "jupyterlab"]

    print(f"Python: {sys.version.split()[0]}")
    print(f"Platform: {platform.platform()}")
    for package in packages:
        print(f"{package}: {package_status(package)}")


if __name__ == "__main__":
    main()
