#!/usr/bin/env -S uv run --script
import importlib.util
from pathlib import Path

import typer

app = typer.Typer()


@app.command(context_settings={'allow_extra_args': True, 'ignore_unknown_options': True})
def main(
    _: typer.Context,
    day: int = typer.Argument(..., help='Day number'),
    part: int = typer.Argument(..., help='Part number'),
) -> None:
    """Run an Advent of Code solution for a specific day and part."""
    day_file = Path('days') / f'day{day:02d}.py'

    if not day_file.exists():
        typer.echo(f'Error: {day_file} does not exist', err=True)
        raise typer.Exit(code=1)

    spec = importlib.util.spec_from_file_location(f'day{day:02d}', day_file)
    if spec is None or spec.loader is None:
        typer.echo(f'Error: Could not load {day_file}', err=True)
        raise typer.Exit(code=1)

    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)

    try:
        data = [line.strip() for line in typer.open_file(f'./inputs/day{day:02d}.txt').readlines()]

        if part == 1:
            result = module.part1(data)
            print(f'Day {day} Part 1 result: {result}')
        elif part == 2:
            result = module.part2(data)
            print(f'Day {day} Part 2 result: {result}')
        else:
            typer.echo('Error: Must specify part 1 or part 2', err=True)

    except Exception as e:
        typer.echo(f'Error: {day_file} ended in error', err=True)
        raise typer.Exit(code=1) from e

if __name__ == '__main__':
    app()
