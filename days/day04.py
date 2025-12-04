"""
--- Printing Department  ---

https://adventofcode.com/2025/day/4
"""
from __future__ import annotations

from copy import deepcopy
from itertools import product


class Warehouse:
    """Warehouse full of paper rolls."""
    def __init__(self, data: list[str]) -> None:
        """Build the warehouse."""
        self.grid: list[list[str]] = []
        for row in data:
            self.grid.append(list(row))

    @property
    def rows(self) -> int:
        """Number of rows in warehouse."""
        return len(self.grid)

    @property
    def cols(self) -> int:
        """Number of cols in warehouse."""
        return len(self.grid[0])

    @property
    def total_paper(self) -> int:
        """The total number of rolls of paper in the warehouse"""
        return sum(row.count('@') for row in self.grid)

    def remove_roll(self, x: int, y: int) -> None:
        """Remove a roll of paper from the warehouse."""
        self.grid[x][y] = '.'

    def is_paper(self, x: int, y: int) -> bool:
        """Is location a paper roll?"""
        return self.grid[x][y] == '@'

    def is_accessable(self, x: int, y: int) -> bool:
        """How many paper rolls are nearby."""
        surrounding = [(x+dx, y+dy) for dx, dy in product([-1, 0, 1], repeat=2) if (dx, dy) != (0,0)]

        total = 0
        for nx, ny in surrounding:
            if 0 <= nx < self.rows and 0 <= ny < self.cols and self.is_paper(nx, ny):
                total += 1

        return total < 4

    def copy(self) -> Warehouse:
        """Copy the warehouse."""
        return deepcopy(self)


def part1(data: list[str]) -> int | str:
    """Solution for part 1."""
    warehouse = Warehouse(data)

    total = 0
    for row in range(warehouse.rows):
        for col in range(warehouse.cols):
            if warehouse.is_paper(row, col) and warehouse.is_accessable(row, col):
                total += 1

    return total



def part2(data: list[str]) -> int | str:
    """Solution for part 2."""
    warehouse = Warehouse(data)

    candidates = {(r, c) for r in range(warehouse.rows)
                  for c in range(warehouse.cols)
                  if warehouse.is_paper(r, c)}

    removed = 0
    while candidates:
        accessible = {(r, c) for r, c in candidates if warehouse.is_accessable(r, c)}

        if not accessible:
            break

        for r, c in accessible:
            warehouse.remove_roll(r, c)
            removed += 1
            candidates.discard((r, c))

    return removed
