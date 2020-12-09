import argparse
import pytest

SLOPES = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]


def run(data, right, down):

    count = 0
    x = right
    y = down

    while y < len(data):
        if data[y][x] == "#":
            count += 1

        x += right
        x %= len(data[0])
        y += down

    return count


def compute(data):

    data = data.splitlines()
    result = 1
    for slope in SLOPES:

        right = slope[0]
        down = slope[1]

        result *= run(data, right, down)

    return result


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


@pytest.mark.parametrize(("test_input,expected"), [(INPUT, 336)])
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
