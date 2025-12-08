import pytest

from days.day06 import part1, part2

test_data = [
    '123 328  51 64',
    ' 45 64  387 23',
    '  6 98  215 314',
    '*   +   *   +',
]


def test_day06_p1():
    assert part1(test_data) == 4277556


def test_day06_p2():
    assert part2(test_data) == 3263827
