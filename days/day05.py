"""
--- Cafeteria ---

https://adventofcode.com/2025/day/5
"""

def parse_input(data: list[str]) -> tuple[list[tuple[int, int]], list[int]]:
    """Parse input data into a set of ranges and ingredients."""
    marker = data.index('')

    ranges = []
    for line in data[:marker]:
        start, end = map(int, line.split('-'))
        ranges.append((start, end))

    sorted_ranges = sorted(ranges)
    merged_ranges = [sorted_ranges[0]]

    for range_start, range_end in sorted_ranges[1:]:
        last_start, last_end = merged_ranges[-1]

        if range_start <= last_end:
            merged_ranges[-1] = (last_start, max(last_end, range_end))
        else:
            merged_ranges.append((range_start, range_end))

    ingredients = [int(line) for line in data[marker+1:]]

    return merged_ranges, ingredients

def part1(data: list[str]) -> int:
    """Solution for part 1."""
    ranges, ingredients = parse_input(data)

    total = 0
    for ingredient in ingredients:
        for lower, upper in ranges:
            if lower <= ingredient <= upper:
                total += 1
                break

    return total


def part2(data: list[str]) -> int:
    """Solution for part 2."""
    ranges, _ = parse_input(data)

    total = 0
    for r0, r1 in ranges:
        total += (r1 - r0 + 1)

    return total
