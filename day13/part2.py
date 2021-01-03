import argparse
import pytest


def compute(data):

    time = 0
    data_s = data.splitlines()
    bus_ids = [
        (idx, int(bus_id))
        for idx, bus_id in enumerate(data_s[1].split(","))
        if bus_id != "x"
    ]
    start = bus_ids[0][1]

    for offset, bus_id in bus_ids[1:]:
        while (time + offset) % bus_id != 0:
            time += start

        start *= bus_id

    return time


INPUT = """\
939
7,13,x,x,59,x,31,19
"""


@pytest.mark.parametrize(("test_input,expected"), [(INPUT, 1068781)])
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
