import pytest

from days.day03 import part1, part2

test_data = ['987654321111111', '811111111111119', '234234234234278', '818181911112111']

def test_day03_p1():
    assert part1(test_data) == 357


def test_day03_p2():
    assert part2(test_data) == 3121910778619
