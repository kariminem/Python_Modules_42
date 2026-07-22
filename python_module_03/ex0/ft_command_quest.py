#!/usr/bin/env python3
import sys


def main() -> None:
    args: list[str] = sys.argv
    print("=== Command Quest ===")
    print(f"Program name: {args[0]}")
    if len(args) == 1:
        print("No arguments provided!")
    else:
        print(f"Arguments received: {len(args) - 1}")
        index: int = 1
        while index < len(args):
            print(f"Argument {index}: {args[index]}")
            index += 1
    print(f"Total arguments: {len(args)}")


if __name__ == "__main__":
    main()
