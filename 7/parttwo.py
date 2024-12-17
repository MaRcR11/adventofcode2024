from itertools import product

def evaluate_expression(nums, operators):
    result = nums[0]
    for i in range(len(operators)):
        if operators[i] == '+':
            result += nums[i + 1]
        elif operators[i] == '*':
            result *= nums[i + 1]
        elif operators[i] == '||':
            result = int(str(result) + str(nums[i + 1]))
    return result

def can_solve_equation(target, numbers):
    return any(evaluate_expression(numbers, ops) == target for ops in product(['+', '*', '||'], repeat=len(numbers) - 1))

def solve_calibration_equations(input_lines):
    return sum(int(line.split(':')[0]) for line in input_lines if can_solve_equation(int(line.split(':')[0]), list(map(int, line.split(':')[1].split()))))

with open("input.txt", "r") as file:
    print(solve_calibration_equations(file.readlines()))