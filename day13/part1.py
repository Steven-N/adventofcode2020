import argparse
import pytest


def compute(data):

    data_s = data.splitlines()
    departure = earliest_depart = int(data_s[0])
    bus_ids = [int(bus_id) for bus_id in data_s[1].split(",") if bus_id != "x"]

    while True:
        for bus_id in bus_ids:
            if departure % bus_id == 0:
                return bus_id * (departure - earliest_depart)

        departure += 1


INPUT = """\
939
7,13,x,x,59,x,31,19
"""


@pytest.mark.parametrize(("test_input,expected"), [(INPUT, 295)])
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
