import argparse
import pytest


def compute(data):

    data = data.splitlines()
    count = 0
    x = 3
    y = 1

    while y < len(data):
        if data[y][x] == "#":
            count += 1

        x += 3
        x %= len(data[0])
        y += 1

    return count


INPUT = """\
..##.......
#...#...#..
.#....#..#.
..#.#...#.#
.#...##..#.
..#.##.....
.#.#.#....#
.#........#
#.##...#...
#...##....#
.#..#...#.#
"""


@pytest.mark.parametrize(("test_input,expected"), [(INPUT, 7)])
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
