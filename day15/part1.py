import argparse
import pytest
import collections


def compute(data):

    data_i = [int(num) for num in data.split(",")]

    spoken = collections.defaultdict(list)

    turns = 2020
    for turn in range(turns):

        if turn < len(data_i):
            num = data_i[turn]
            spoken[num].append(turn)
            prev_spoken = num

        elif len(spoken[prev_spoken]) == 1:
            spoken[0].append(turn)
            prev_spoken = 0

        else:
            last_spoken = spoken[prev_spoken][-1]
            second_last_spoken = spoken[prev_spoken][-2]
            next_spoken = last_spoken - second_last_spoken
            if next_spoken in spoken:
                spoken[next_spoken].append(turn)
            else:
                spoken[next_spoken] = [turn]

            prev_spoken = next_spoken

    return prev_spoken


@pytest.mark.parametrize(
    ("test_input,expected"),
    [
        ("1,3,2", 1),
        ("2,1,3", 10),
        ("1,2,3", 27),
        ("2,3,1", 78),
        ("3,2,1", 438),
        ("3,1,2", 1836),
        ("0,3,6", 436),
    ],
)
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
