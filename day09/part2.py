import argparse
import pytest


def compute(data, preamble):

    data_i = [int(i) for i in data.splitlines()]

    p_s = 0
    p_e = preamble
    invalid = -1
    invalid_index = -1

    for idx_i, i in enumerate(data_i[preamble:]):
        preamble_l = data_i[p_s:p_e]
        found = False

        for idx, num in enumerate(preamble_l):
            if i - num in preamble_l[idx + 1 :]:  # noqa: E203
                found = True
                break

        if not found:
            invalid = i
            invalid_index = idx_i + preamble
            break

        p_s += 1
        p_e += 1

    for idx, i in enumerate(data_i[:invalid_index]):
        contiguous = [i]
        for j in data_i[idx + 1 : invalid_index]:  # noqa: E203
            contiguous.append(j)
            contiguous_sum = sum(contiguous)
            if contiguous_sum == invalid:
                contiguous = sorted(contiguous)
                return contiguous[0] + contiguous[len(contiguous) - 1]
            if contiguous_sum > invalid:
                break

    return -1


TEST_PREAMBLE = 5

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


@pytest.mark.parametrize(("test_input,expected"), [(INPUT, 62)])
def test(test_input, expected):
    assert compute(test_input, TEST_PREAMBLE) == expected


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("file")
    parser.add_argument("preamble")
    args = parser.parse_args()

    with open(args.file, "r") as f:
        print(compute(f.read(), int(args.preamble)))


if __name__ == "__main__":
    exit(main())
