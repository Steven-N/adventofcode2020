import argparse
import pytest


def compute(data):

    valid_passwords = 0
    for line in data.splitlines():
        policy, char, pwd = line.split()
        min_occur_s, max_occur_s = policy.split("-")
        min_occur, max_occur = int(min_occur_s), int(max_occur_s)
        char = char[0]
        occurences = pwd.count(char)
        if min_occur <= occurences <= max_occur:
            valid_passwords += 1

    return valid_passwords


TEST_INPUT = """\
1-3 a: abcde
1-3 b: cdefg
2-9 c: ccccccccc
"""


@pytest.mark.parametrize(("test_input,expected"), [(TEST_INPUT, 2)])
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
