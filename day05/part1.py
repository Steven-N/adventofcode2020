import argparse
import pytest


def bsearch(data, low, high):

    low = low
    mid = 0
    high = high

    mid = (high + low) // 2

    for char in data:

        if char in ["F", "L"]:
            high = mid

        elif char in ["B", "R"]:
            low = mid + 1

        mid = (high + low) // 2

    return mid


def compute(data):

    max_seat_id = 0

    for boarding_pass in data.splitlines():

        row = bsearch(boarding_pass[:7], 0, 127)
        column = bsearch(boarding_pass[7:], 0, 7)

        result = (row * 8) + column
        if result > max_seat_id:
            max_seat_id = result

    return max_seat_id


INPUT = """\
BFFFBBFRRR
FFFBBBFRRR
BBFFBBFRLL
"""


@pytest.mark.parametrize(("test_input,expected"), [(INPUT, 820)])
def test(test_input, expected):
    assert compute(test_input) == expected


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("file")
    args = parser.parse_args()

    with open(args.file, "r") as f:
        print(compute(f.read()))


if __name__ == "__main__":
    exit(main())
