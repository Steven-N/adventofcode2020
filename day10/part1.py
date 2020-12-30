import argparse
import pytest


def compute(data):

    data_i = sorted([int(i) for i in data.splitlines()])

    differences = {1: 1, 2: 0, 3: 1}

    for idx, num in enumerate(data_i):
        j = idx + 1

        if j >= len(data_i):
            break

        diff = data_i[j] - data_i[idx]
        differences[diff] += 1

    return differences[1] * differences[3]


INPUT = """\
16
10
15
5
1
11
7
19
6
12
4
"""


@pytest.mark.parametrize(("test_input,expected"), [(INPUT, 35)])
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
