def ft_count_harvest_recursive() -> None:
    days = int(input("Days until harvest: "))

    def recursive_print(current_day: int) -> None:
        if current_day > days:
            return
        print(f"Day {current_day}")
        recursive_print(current_day + 1)

    recursive_print(1)
    print("Harvest time!")
