import argparse
import pytest


def compute(data):

    operations = [op for op in data.splitlines()]
    cur_line = 0
    next_line = 0
    accumulator = 0
    visited = set()

    while cur_line < len(operations):
        if cur_line in visited:
            break

        operation, value = operations[cur_line].split(" ")

        if operation == "nop":
            next_line += 1
        elif operation == "acc":
            accumulator += int(value)
            next_line += 1
        elif operation == "jmp":
            next_line += int(value)

        visited.add(cur_line)
        cur_line = next_line

    return accumulator


INPUT = """\
nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6
"""


@pytest.mark.parametrize(("test_input,expected"), [(INPUT, 5)])
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
