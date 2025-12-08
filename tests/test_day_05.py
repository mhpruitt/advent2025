import pytest

from days.day05 import part1, part2

test_data = [
    '3-5',
    '10-14',
    '16-20',
    '12-18',
    '',
    '1',
    '5',
    '8',
    '11',
    '17',
    '32'
]


def test_day05_p1():
    assert part1(test_data) == 3


def test_day05_p2():
    assert part2(test_data) == 14
