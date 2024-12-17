import csv

def count_safe_reports_with_dampener():
    with open('input.csv', mode='r') as f:
        return sum(
            any(
                all(
                    abs(nums[i] - nums[i-1]) <= 3 and nums[i] != nums[i-1] and
                    (i < 2 or (nums[i] > nums[i-1]) == (nums[i-1] > nums[i-2]))
                    for i in range(1, len(nums))
                ) for nums in (row[:j] + row[j+1:] for j in range(len(row)))
            ) for row in (list(map(int, r)) for r in csv.reader(f, delimiter=" "))
        )

print(count_safe_reports_with_dampener())
