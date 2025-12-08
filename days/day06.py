"""
--- Trash Compactor ---

https://adventofcode.com/2025/day/6
"""
import operator
import re
from functools import reduce


def part1(data: list[str]) -> int:
    """Solution for part 1."""
    ops = data[-1].split()

    rows = [list(map(int, line.split())) for line in data[:-1]]
    cols = list(zip(*rows, strict=True))

    total = 0
    for i, col in enumerate(cols):
        op = ops[i]
        match op:
            case '*':
                total += reduce(operator.mul, col)
            case '+':
                total += reduce(operator.add, col)

    return total


def part2(data: list[str]) -> int:
    """Solution for part 2."""
    ops = data[-1].split()
    rows = data[:-1]

    fields = [(m.start(),  m.end()) for m in re.finditer(r' +', data[-1])]

    last = 0
    parsed_rows = []
    for row in rows:
        new_row = []
        for start, end in fields:
            new_row.append(''.join(reversed(row[start-1:end-1])))
            last = end
        new_row.append(''.join(reversed(row[last:].ljust(end-start))))
        parsed_rows.append(new_row)

    total = 0
    transformed_rows = zip(*parsed_rows, strict=True)
    for i, row in enumerate(transformed_rows):
        op = ops[i]
        vals = [int(''.join(t)) for t in zip(*row, strict=True)]
        match op:
            case '*':
                total += reduce(operator.mul, vals)
            case '+':
                total += reduce(operator.add, vals)

    return total


