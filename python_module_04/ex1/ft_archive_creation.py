#!/usr/bin/env python3
import sys
import typing


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: ft_archive_creation.py <file>")
        return

    filename: str = sys.argv[1]
    print("=== Cyber Archives Recovery & Preservation ===")
    print(f"Accessing file '{filename}'")

    try:
        file: typing.IO[str] = open(filename, "r")
    except OSError as error:
        print(f"Error opening file '{filename}': {error}")
        return

    content: str = file.read()
    print("---")
    print(content)
    print("---")
    file.close()
    print(f"File '{filename}' closed.")

    lines: list[str] = content.split("\n")
    transformed: str = "#\n".join(lines)
    print("\nTransform data:")
    print("---")
    print(transformed)
    print("---")

    new_filename: str = input("Enter new file name (or empty): ")
    if len(new_filename) == 0:
        print("Not saving data.")
        return

    print(f"Saving data to '{new_filename}'")
    try:
        out_file: typing.IO[str] = open(new_filename, "w")
    except OSError as error:
        print(f"Error opening file '{new_filename}': {error}")
        return

    out_file.write(transformed)
    out_file.close()
    print(f"Data saved in file '{new_filename}'.")


if __name__ == "__main__":
    main()
