import argparse
import pytest
import collections
import re

mem_match = re.compile(r"^mem\[(\d+)\] = (\d+)$")


def compute(data):

    memory = collections.defaultdict(int)

    for line in data.splitlines():
        if line.startswith("mask"):
            mask = line.split(" = ")[-1]
        else:
            new_mem_val = []
            match = mem_match.match(line)
            mem_loc = int(match[1])
            mem_val = int(match[2])
            mem_bin_s = str(bin(mem_val)[2:].zfill(36))

            for idx, digit in enumerate(mask):
                if digit == "X" or mem_bin_s[idx] == digit:
                    new_mem_val.append(mem_bin_s[idx])
                elif mem_bin_s[idx] != digit:
                    new_mem_val.append(digit)

            new_mem_val = "".join(new_mem_val)
            memory[mem_loc] = int(new_mem_val, 2)

    return sum(memory.values())


INPUT = """\
mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X
mem[8] = 11
mem[7] = 101
mem[8] = 0
"""


@pytest.mark.parametrize(("test_input,expected"), [(INPUT, 165)])
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
