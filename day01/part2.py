import argparse
import itertools
import pytest


def compute(data):

    nums = [int(num) for num in data.split()]
    for a, b, c in itertools.combinations(nums, 3):
        if 2020 - a - b - c == 0:
            return a * b * c


@pytest.mark.parametrize(
    ("test_input,expected"),
    [
        ("1721 979 366 299 675 1456", 241861950)
    ]
)
def test(test_input, expected):
    assert compute(test_input) == expected


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('file')
    args = parser.parse_args()

    with open(args.file, 'r') as f:
        print(compute(f.read()))


if __name__ == "__main__":
    exit(main())
