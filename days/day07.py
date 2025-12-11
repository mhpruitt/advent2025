"""
--- Laboratories ---

https://adventofcode.com/2025/day/7
"""

def part1(data: list[str]) -> int:
    """Solution for part 1."""
    activated_splitters = set()

    def _trace_beam(row: int, col: int) -> None:
        while row < len(data):
            if data[row][col] == '^':
                if (row, col) not in activated_splitters:
                    activated_splitters.add((row, col))
                    if col > 0:
                        _trace_beam(row + 1, col - 1)
                    if col < len(data[row]) - 1:
                        _trace_beam(row + 1, col + 1)
                return
            row += 1

    _trace_beam(1, data[0].find('S'))
    return len(activated_splitters)

def part2(data: list[str]) -> int | str:
    """Solution for part 2."""
    history = {}

    def _trace_beam(row: int, col: int) -> int:
        if (row, col) in history:
            return history[(row, col)]

        timelines = 0
        current = row

        while current < len(data):
            if data[current][col] == '^':
                if col > 0:
                    timelines += _trace_beam(current + 1, col - 1)

                if col < len(data[current]) - 1:
                    timelines += _trace_beam(current + 1, col + 1)

                history[(row, col)] = timelines
                return timelines

            current += 1

        history[(row, col)] = 1
        return 1

    return _trace_beam(1, data[0].find('S'))
