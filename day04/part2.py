import argparse
import pytest
import re

PASSPORT_FIELDS = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}


def validate_height(hgt):

    match = re.match(r"^(\d+)(cm|in)$", hgt)

    if match:
        if match[2] == "in":
            if 59 <= int(match[1]) <= 76:
                return True

        elif match[2] == "cm":
            if 150 <= int(match[1]) <= 193:
                return True

        else:
            return False

    return False


def validate_hair_colour(hcl):

    matcher = r"^#[a-f0-9]{6}$"

    if re.match(matcher, hcl):
        return True

    return False


def validate_eye_colour(ecl):

    eye_colours = set("amb blu brn gry grn hzl oth".split())

    if ecl in eye_colours:
        return True
    else:
        return False


def validate_passport_id(pid):

    if pid.isdigit() and len(pid) == 9:
        return True
    else:
        return False


def compute(data):
    data = data.split("\n\n")

    valid_passports = 0

    for passport in data:
        fields_split = [field.split(":") for field in passport.split()]
        fields = {k: v for k, v in fields_split}
        if (
            len(fields.keys() & PASSPORT_FIELDS) == len(PASSPORT_FIELDS)
            and 1920 <= int(fields["byr"]) <= 2002
            and 2010 <= int(fields["iyr"]) <= 2020
            and 2020 <= int(fields["eyr"]) <= 2030
            and validate_height(fields["hgt"])
            and validate_hair_colour(fields["hcl"])
            and validate_eye_colour(fields["ecl"])
            and validate_passport_id(fields["pid"])
        ):

            valid_passports += 1

    return valid_passports


INPUT = """\
eyr:1972 cid:100
hcl:#18171d ecl:amb hgt:170 pid:186cm iyr:2018 byr:1926

iyr:2019
hcl:#602927 eyr:1967 hgt:170cm
ecl:grn pid:012533040 byr:1946

hcl:dab227 iyr:2012
ecl:brn hgt:182cm pid:021572410 eyr:2020 byr:1992 cid:277

hgt:59cm ecl:zzz
eyr:2038 hcl:74454a iyr:2023
pid:3556412378 byr:2007

pid:087499704 hgt:74in ecl:grn iyr:2012 eyr:2030 byr:1980
hcl:#623a2f

eyr:2029 ecl:blu cid:129 byr:1989
iyr:2014 pid:896056539 hcl:#a97842 hgt:165cm

hcl:#888785
hgt:164cm byr:2001 iyr:2015 cid:88
pid:545766238 ecl:hzl
eyr:2022

iyr:2010 hgt:158cm hcl:#b6652a ecl:blu byr:1944 eyr:2021 pid:093154719
"""


@pytest.mark.parametrize(("test_input,expected"), [(INPUT, 4)])
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
