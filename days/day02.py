"""
--- Gift Shop ---

https://adventofcode.com/2025/day/2
"""

def part1(data: list[str]) -> int:
    """Solution for part 1."""
    total = 0
    ranges = data[0].strip().split(',')
    for r in ranges:
        start, end = r.split('-')
        for i in range(int(start), int(end)+1):
            candidate = str(i)
            clen = len(candidate)

            if clen % 2 == 0:  # Part one
                mid = clen // 2
                if candidate == candidate[:mid] * 2:
                    total += i

    return total


def part2(data: list[str]) -> int:
    """Solution for part 2."""
    total = 0
    ranges = data[0].strip().split(',')
    for r in ranges:
        start, end = r.split('-')
        for i in range(int(start), int(end) + 1):
            candidate = str(i)
            clen = len(candidate)

            for c in range(clen // 2, 0, -1):  # Part two
                if clen % c == 0 and candidate == candidate[:c] * (clen // c):
                    total += i
                    break

    return total

    # Solution for part 2 using regexes
    import re
    pattern = re.compile(r'^(\d+)\1+$')

    total = 0
    ranges = data[0].strip().split(',')
    for r in ranges:
        start, end = r.split('-')
        for i in range(int(start), int(end) + 1):
            candidate = str(i)
            matches = pattern.findall(candidate)
            if len(matches):
                total += int(candidate)

    return total
