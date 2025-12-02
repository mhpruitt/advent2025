"""
--- TEMPLATE ---

https://adventofcode.com/2025/day/1
"""

import pathlib

import typer

app = typer.Typer()


def part1() -> None:
    """Solution for part 1."""
    print('Part 1 not implemented yet')


def part2() -> None:
    """Solution for part 2."""
    print('Part 2 not implemented yet')


@app.command()
def main(
    day: str = typer.Option(..., '--day', help='Day'),
    part: int = typer.Option(..., '--part', help='Part to run (1 or 2)'),
) -> None:
    """Run the solution for the specified part."""
    data = pathlib.Path(f'./inputs/day{day}-{part}.txt').read_text().splitlines()
    if part == 1:
        print(f'Day {day} Part 1 result: {part1(data)}')
    elif part == 2:
        print(f'Day {day} Part 2 result: {part2(data)}')


if __name__ == '__main__':
    app()
