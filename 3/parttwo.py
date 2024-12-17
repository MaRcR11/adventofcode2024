import re


def sum_enabled_mul():
    with open("input.txt") as f:
        data = f.read()

        enabled = True
        total_sum = 0

        for match in re.finditer(r"(do\(\)|don't\(\)|mul\((\d+),(\d+)\))", data):
            if match.group(1) == "do()":
                enabled = True
            elif match.group(1) == "don't()":
                enabled = False
            elif enabled and match.group(2) and match.group(3):
                total_sum += int(match.group(2)) * int(match.group(3))

        return total_sum


print(sum_enabled_mul())
