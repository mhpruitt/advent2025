import pytest

from days.day04 import part1, part2

test_data = [
    '..@@.@@@@.',
    '@@@.@.@.@@',
    '@@@@@.@.@@',
    '@.@@@@..@.',
    '@@.@@@@.@@',
    '.@@@@@@@.@',
    '.@.@.@.@@@',
    '@.@@@.@@@@',
    '.@@@@@@@@.',
    '@.@.@@@.@.',
]


def test_day04_p1():
    assert part1(test_data) == 13


def test_day04_p2():
    assert part2(test_data) == 43
