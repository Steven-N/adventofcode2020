import argparse
import pytest


def compute(data):

    positions = {
        # left, right, up, down
        (1, 0),
        (-1, 0),
        (0, 1),
        (0, -1),
        # diagonal
        (1, 1),
        (-1, -1),
        (1, -1),
        (-1, 1),
    }

    data = [line for line in data.splitlines()]

    while True:
        changed = False
        y = 0
        new_seat_arrangement = []
        for line in data:
            line_arr = list(line)
            for idx, cur_seat in enumerate(line):
                if cur_seat == ".":
                    continue
                adj_seats = []
                for pos_x, pos_y in positions:
                    cur_x = idx + pos_x
                    cur_y = y + pos_y
                    while (
                        cur_x >= 0
                        and cur_y >= 0
                        and cur_x < len(line)
                        and cur_y < len(data)
                    ):
                        if data[cur_y][cur_x] == "#":
                            adj_seats.append(data[cur_y][cur_x])
                            break
                        if data[cur_y][cur_x] == "L":
                            break
                        cur_x += pos_x
                        cur_y += pos_y

                if all(seat != "#" for seat in adj_seats) and line[idx] == "L":
                    line_arr[idx] = "#"
                    changed = True
                elif adj_seats.count("#") >= 5 and line[idx] == "#":
                    line_arr[idx] = "L"
                    changed = True

            new_seat_arrangement.append("".join(line_arr))
            y += 1

        data = new_seat_arrangement

        if not changed:
            break

    occupied = 0
    for line in data:
        occupied += line.count("#")

    return occupied


INPUT = """\
L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL
"""


@pytest.mark.parametrize(("test_input,expected"), [(INPUT, 26)])
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
