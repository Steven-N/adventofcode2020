import argparse
import pytest
import collections
import re


def compute(data):

    bags = collections.defaultdict(list)
    total_colours = set()

    OUTER_BAG_MATCHER = re.compile(r"(.+?(?= bags contain))")
    INNER_BAG_MATCHER = re.compile(r"(\d+) ((\w+) (\w+))")

    for line in data.splitlines():
        outer_bag = OUTER_BAG_MATCHER.search(line)[0]
        inner_bags = [i_b[1] for i_b in INNER_BAG_MATCHER.findall(line)]
        for inner_bag in inner_bags:
            bags[inner_bag].append(outer_bag)

    bags_left = bags["shiny gold"]
    while bags_left:
        curr_colour = bags_left.pop()
        total_colours.add(curr_colour)
        bags_left.extend(bags[curr_colour])

    return len(total_colours)


INPUT = """\
light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags.
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
