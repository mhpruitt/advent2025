from days.day01 import part1, part2

test_data = [
    'L68',
    'L30',
    'R48',
    'L5',
    'R60',
    'L55',
    'L1',
    'L99',
    'R14',
    'L82',
]

def test_day01_part1():
    assert part1(test_data) == 3


def test_day01_part2():
    assert part2(test_data) == 6
