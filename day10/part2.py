import argparse
import pytest
import collections


def find_combinations(index, value, combinations, data):

    for idx, num in enumerate(data[:index]):

        if value - num <= 3:
            combinations[value] += combinations[num]

    if value not in combinations:
        combinations[value] = 1


def compute(data):

    data_i = sorted([int(i) for i in data.splitlines()])
    data_i.insert(0, 0)
    combinations = collections.defaultdict(int, {0: 1})

    for idx, num in enumerate(data_i):

        find_combinations(idx, num, combinations, data_i)

    return combinations[data_i[-1]]


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

INPUT_2 = """\
28
33
18
42
31
14
46
20
48
47
24
23
49
45
19
38
39
11
1
32
25
35
8
17
7
9
4
2
34
10
3
"""


@pytest.mark.parametrize(
    ("test_input,expected"), [(INPUT, 8), (INPUT_2, 19208)]
)  # noqa: E501
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
