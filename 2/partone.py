import csv


def count_safe_reports():
    with open("input.csv", mode="r") as f:
        return sum(
            not any(
                abs(nums[i] - nums[i - 1]) > 3
                or nums[i] == nums[i - 1]
                or (i > 1 and (nums[i] > nums[i - 1]) != (nums[i - 1] > nums[i - 2]))
                for i in range(1, len(nums))
            )
            for nums in (list(map(int, row)) for row in csv.reader(f, delimiter=" "))
        )


print(count_safe_reports())
