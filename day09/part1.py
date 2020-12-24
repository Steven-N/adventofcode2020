import argparse
import pytest


def compute(data, preamble):

    data_i = [int(i) for i in data.splitlines()]

    p_s = 0
    p_e = preamble

    for i in data_i[preamble:]:
        preamble_l = data_i[p_s:p_e]
        found = False
        # preamble_sum = sum(preamble_l)

        for idx, num in enumerate(preamble_l):
            if i - num in preamble_l[idx + 1 :]:  # noqa: E203
                found = True
                break

        if not found:
            return i

        p_s += 1
        p_e += 1

    return -1


INPUT = """\
35
20
15
25
47
40
62
55
65
95
102
117
150
182
127
219
299
277
309
576
"""


@pytest.mark.parametrize(("test_input,expected"), [(INPUT, 127)])
def test(test_input, expected):
    assert compute(test_input, preamble=5) == expected


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("file")
    parser.add_argument("preamble")
    args = parser.parse_args()

    with open(args.file, "r") as f:
        print(compute(f.read(), int(args.preamble)))


if __name__ == "__main__":
    exit(main())
