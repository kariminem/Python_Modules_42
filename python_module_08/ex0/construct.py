#!/usr/bin/env python3
import sys
import os
import site


def in_virtual_env() -> bool:
    return sys.prefix != sys.base_prefix


def show_outside() -> None:
    print("MATRIX STATUS: You're still plugged in\n")
    print(f"Current Python: {sys.executable}")
    print("Virtual Environment: None detected\n")
    print("WARNING: You're in the global environment!")
    print("The machines can see everything you install.\n")
    print("To enter the construct, run:")
    print("python -m venv matrix_env")
    print("source matrix_env/bin/activate  # On Unix")
    print("matrix_env\\Scripts\\activate  # On Windows\n")
    print("Then run this program again.")


def show_inside() -> None:
    env_path = sys.prefix
    env_name = os.path.basename(env_path)
    print("MATRIX STATUS: Welcome to the construct\n")
    print(f"Current Python: {sys.executable}")
    print(f"Virtual Environment: {env_name}")
    print(f"Environment Path: {env_path}\n")
    print("SUCCESS: You're in an isolated environment!")
    print("Safe to install packages without affecting")
    print("the global system.\n")
    print("Package installation path:")
    site_packages = site.getsitepackages() if hasattr(
        site, "getsitepackages"
    ) else [os.path.join(env_path, "lib", "site-packages")]
    print(site_packages[0])


def main() -> None:
    try:
        if in_virtual_env():
            show_inside()
        else:
            show_outside()
    except Exception as error:
        print(f"Error inspecting the environment: {error}")


if __name__ == "__main__":
    main()
