import re


def sum_all_mul():
    with open("input.txt", mode="r") as f:
        return sum(
            int(a) * int(b) for a, b in re.findall(r"mul\((\d+),(\d+)\)", f.read())
        )


print(sum_all_mul())
