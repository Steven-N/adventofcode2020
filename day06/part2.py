import argparse
import pytest


def compute(data):

    result = 0
    answers = set()

    for group in data.split("\n\n"):
        lines = group.split()
        answers = set(lines[0])
        for answer in lines[1:]:
            answers.intersection_update(set(answer))

        result += len(answers)
        answers.clear()

    return result


INPUT = """\
abc

a
b
c

ab
ac

a
a
a
a

b
"""


@pytest.mark.parametrize(("test_input,expected"), [(INPUT, 6)])
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
