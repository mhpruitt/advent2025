"""
--- Lobby  ---

https://adventofcode.com/2025/day/3
"""

def find_joltage_p1(bank: str) -> int:
    """Find Joltage of a bank, picking 2 batteries"""
    first_battery = max(bank[:-1])  # biggest number not at the end
    first_battery_idx = bank.index(first_battery)
    second_battery = max(bank[first_battery_idx + 1:])  # biggest number of the remainder

    return int(first_battery + second_battery)

def find_joltage_p2(bank: str, batteries: int = 12) -> int:
    """Find joltage of a bank, picking x batteries."""
    stack = []
    skippable = len(bank) - batteries

    for battery in bank:
        while stack and skippable > 0 and stack[-1] < battery:
            stack.pop()
            skippable -= 1
        stack.append(battery)

    return int(''.join(stack[:batteries]))

def part1(data: list[str]) -> int | str:
    """Solution for part 1."""
    return sum(find_joltage_p1(bank.strip()) for bank in data)


def part2(data: list[str]) -> int | str:
    """Solution for part 2."""
    return sum(find_joltage_p2(bank.strip()) for bank in data)
