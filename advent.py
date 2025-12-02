#!/usr/bin/env -S uv run --script
import importlib.util
import sys
from pathlib import Path

import typer

app = typer.Typer()


@app.command(context_settings={'allow_extra_args': True, 'ignore_unknown_options': True})
def main(
    ctx: typer.Context,
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
    sys.modules[spec.name] = module

    sys.argv = [str(day_file), f'--day={day:02d}', f'--part={part}']
    if ctx.args:
        sys.argv.extend(ctx.args)

    spec.loader.exec_module(module)

    if hasattr(module, 'app'):
        module.app()
    else:
        typer.echo(f'Error: {day_file} does not have an app() callable', err=True)
        raise typer.Exit(code=1)


if __name__ == '__main__':
    app()
