"""
--- Secret Entrance ---

https://adventofcode.com/2025/day/1
"""


def part1(data: list[str]) -> int:
    """Solution for part 1."""
    current = 50
    total_zeros = 0

    for movement in data:
        d, m = movement[0], int(movement[1:])
        next_number = current + m if d == 'R' else current - m

        current = next_number % 100
        if current == 0:
            total_zeros += 1

    return total_zeros


def part2(data: list[str]) -> int:
    """Solution for part 2."""
    current = 50
    total_zeros = 0

    for movement in data:
        d, m = movement[0], int(movement[1:])
        for _ in range(m):
            current = (current + 1) % 100 if d == 'R' else (current - 1) % 100

            if current == 0:
                total_zeros += 1

    return total_zeros

    """Solution for part 2 using numpy."""
    import numpy as np

    # Parse all movements at once
    directions = np.array([1 if line[0] == 'R' else -1 for line in data])
    distances = np.array([int(line[1:]) for line in data])

    deltas = np.repeat(directions, distances)  # individual movements
    positions = (50 + np.cumsum(deltas)) % 100  # actual positions

    return int(np.count_nonzero(positions == 0))  # count zeros
