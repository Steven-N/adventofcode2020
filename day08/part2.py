import argparse
import pytest


def compute(data):

    cur_line = 0
    next_line = 0
    accumulator = 0
    flipped_line = 0
    reset_flip = False
    operations = []
    prev_full_op = ""
    flippable_ops_lines = set()
    visited = set()

    flip_dict = {"jmp": "nop", "nop": "jmp"}

    for idx, op in enumerate(data.splitlines()):
        operations.append(op)
        if op.split(" ")[0] in flip_dict.keys():
            flippable_ops_lines.add(idx)

    while cur_line < len(operations):
        operation, value = operations[cur_line].split(" ")

        if cur_line in visited:
            visited = set()
            cur_line = next_line = accumulator = 0
            if reset_flip:
                operations[flipped_line] = prev_full_op
            flipped_line = flippable_ops_lines.pop()
            prev_full_op = operations[flipped_line]
            prev_op = prev_full_op[0:3]
            new_op = flip_dict[prev_op[0:3]]
            operations[flipped_line] = prev_full_op.replace(prev_op, new_op)
            reset_flip = True
            continue

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


@pytest.mark.parametrize(("test_input,expected"), [(INPUT, 8)])
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
