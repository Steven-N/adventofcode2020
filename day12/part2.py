import argparse
import pytest


def calculate_ship_location(move_s_x, move_s_y, ship):

    cur_s_x, cur_s_y = ship

    new_s_x = cur_s_x + move_s_x
    new_s_y = cur_s_y + move_s_y

    return (new_s_x, new_s_y)


def calculate_waypoint_move(action, units, w_x, w_y):

    if action == "N":
        w_y += units
    elif action == "S":
        w_y -= units
    elif action == "E":
        w_x += units
    elif action == "W":
        w_x -= units
    else:
        raise NotImplementedError(f"Action '{action}' not recognized.")

    return (w_x, w_y)


def calculate_waypoint_rotation(action, unit, w_x, w_y):

    if (action == "L" and unit == 90) or (action == "R" and unit == 270):
        new_w_x = -w_y
        new_w_y = w_x

    elif (action == "L" and unit == 270) or (action == "R" and unit == 90):
        new_w_x = w_y
        new_w_y = -w_x

    elif unit == 180:
        new_w_x = -w_x
        new_w_y = -w_y

    else:
        raise NotImplementedError(
            f"Rotation '{action}' '{unit}' degrees has not been implemented."
        )

    return (new_w_x, new_w_y)


def compute(data):

    dirs = ["N", "E", "S", "W"]

    ship = (0, 0)

    waypoint = (10, 1)

    for line in data.splitlines():
        action = line[0]
        units = int(line[1:])

        w_x, w_y = waypoint

        if action == "F":

            new_s_x = w_x * units
            new_s_y = w_y * units

            ship = calculate_ship_location(new_s_x, new_s_y, ship)

        elif action in ["R", "L"]:

            waypoint = calculate_waypoint_rotation(action, units, w_x, w_y)

        elif action in dirs:
            waypoint = calculate_waypoint_move(action, units, w_x, w_y)

    return sum([abs(val) for val in ship])


INPUT = """\
F10
N3
F7
R90
F11
"""


@pytest.mark.parametrize(("test_input,expected"), [(INPUT, 286)])
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
