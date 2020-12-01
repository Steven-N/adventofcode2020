import argparse
import pytest


def compute(data):

    nums = set()
    for num in data.split():
        n = int(num)
        nums.add(n)
    for num in nums:
        if 2020 - num in nums:
            return num * (2020-num)


@pytest.mark.parametrize(
    ("test_input,expected"),
    [
        ("1721 979 366 299 675 1456", 514579)
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
