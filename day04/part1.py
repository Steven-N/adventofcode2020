import argparse
import pytest


PASSPORT_FIELDS = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}


def compute(data):
    data = data.split("\n\n")

    valid_passports = 0

    for passport in data:
        fields_split = [field.split(":") for field in passport.split()]
        fields = {k: v for k, v in fields_split}
        if len(fields.keys() & PASSPORT_FIELDS) == len(PASSPORT_FIELDS):
            valid_passports += 1

    return valid_passports


INPUT = """\
ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
byr:1937 iyr:2017 cid:147 hgt:183cm

iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
hcl:#cfa07d byr:1929

hcl:#ae17e1 iyr:2013
eyr:2024
ecl:brn pid:760753108 byr:1931
hgt:179cm

hcl:#cfa07d eyr:2025 pid:166559648
iyr:2011 ecl:brn hgt:59in
"""


@pytest.mark.parametrize(("test_input,expected"), [(INPUT, 2)])
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
