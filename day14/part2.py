import argparse
import pytest
import collections
import re
import itertools

mem_match = re.compile(r"^mem\[(\d+)\] = (\d+)$")


def parse_mask(mask, mem_loc_bin_s, floating_addresses):

    memory_locations = []
    floating_combs = itertools.product([0, 1], repeat=floating_addresses)

    for f_comb in floating_combs:
        count = 0
        new_mem_loc = []
        for idx, char in enumerate(mem_loc_bin_s):
            if mask[idx] == "X":
                new_mem_loc.append(str(f_comb[count]))
                count += 1
            elif mask[idx] == "1":
                new_mem_loc.append("1")
            else:
                new_mem_loc.append(char)

        new_mem_loc = int("".join(new_mem_loc), 2)
        memory_locations.append(new_mem_loc)

    return memory_locations


def compute(data):

    memory = collections.defaultdict(int)

    for line in data.splitlines():
        if line.startswith("mask"):
            mask = line.split(" = ")[-1]
            floating_addresses = mask.count("X")
        else:
            match = mem_match.match(line)
            input_mem_loc = int(match[1])
            mem_loc_bin_s = str(bin(input_mem_loc)[2:].zfill(36))
            mem_val = int(match[2])

            mem_locations = parse_mask(mask, mem_loc_bin_s, floating_addresses)

            for mem_loc in mem_locations:
                memory[mem_loc] = mem_val

    return sum(memory.values())


INPUT = """\
mask = 000000000000000000000000000000X1001X
mem[42] = 100
mask = 00000000000000000000000000000000X0XX
mem[26] = 1
"""


@pytest.mark.parametrize(("test_input,expected"), [(INPUT, 208)])
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
