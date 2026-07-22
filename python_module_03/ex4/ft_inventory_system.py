#!/usr/bin/env python3
import sys


def main() -> None:
    args: list[str] = sys.argv[1:]
    print("=== Inventory System Analysis ===")

    inventory: dict[str, int] = {}
    for arg in args:
        parts: list[str] = arg.split(":")
        if len(parts) != 2 or len(parts[0]) == 0:
            print(f"Error - invalid parameter '{arg}'")
            continue
        item_name: str = parts[0]
        if item_name in inventory.keys():
            print(f"Redundant item '{item_name}' - discarding")
            continue
        try:
            quantity: int = int(parts[1])
        except ValueError as error:
            print(f"Quantity error for '{item_name}': {error}")
            continue
        inventory.update({item_name: quantity})

    print(f"Got inventory: {inventory}")

    item_list: list[str] = list(inventory.keys())
    print(f"Item list: {item_list}")

    total: int = sum(inventory.values())
    print(f"Total quantity of the {len(item_list)} items: {total}")

    if total > 0:
        for item_name in item_list:
            percent: float = inventory[item_name] / total * 100
            print(f"Item {item_name} represents {round(percent, 1)}%")

        most_item: str = item_list[0]
        least_item: str = item_list[0]
        for item_name in item_list:
            if inventory[item_name] > inventory[most_item]:
                most_item = item_name
            if inventory[item_name] < inventory[least_item]:
                least_item = item_name
        print(
            f"Item most abundant: {most_item} "
            f"with quantity {inventory[most_item]}"
        )
        print(
            f"Item least abundant: {least_item} "
            f"with quantity {inventory[least_item]}"
        )

    inventory.update({"magic_item": 1})
    print(f"Updated inventory: {inventory}")


if __name__ == "__main__":
    main()
