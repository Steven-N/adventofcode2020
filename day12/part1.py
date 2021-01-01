import argparse
import pytest


def calculate_direction(action, units, directions):

    opposite_dirs = {"N": "S", "S": "N", "E": "W", "W": "E"}

    opposite_dir = opposite_dirs[action]
    opposite_dir_val = directions[opposite_dir]

    new_distance = abs(units - opposite_dir_val)

    if units > opposite_dir_val:
        directions[action] += new_distance
        directions[opposite_dir] = 0
    else:
        directions[opposite_dir] = new_distance


def compute(data):

    dirs = ["N", "E", "S", "W"]

    directions = {"N": 0, "S": 0, "E": 0, "W": 0}

    cur_pos = 90

    for line in data.splitlines():
        action = line[0]
        units = int(line[1:])

        if action == "F":
            direction = dirs[int((cur_pos / 90) % 4)]
            calculate_direction(direction, units, directions)

        elif action == "R":
            cur_pos += units

        elif action == "L":
            cur_pos -= units

        elif action in dirs:
            calculate_direction(action, units, directions)

    return sum(directions.values())


INPUT = """\
F10
N3
F7
R90
F11
"""


@pytest.mark.parametrize(("test_input,expected"), [(INPUT, 25)])
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
