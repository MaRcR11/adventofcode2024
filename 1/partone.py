import pandas as pd

def calc_total_distance():

    data = pd.read_csv('input.csv', header=None, sep=r'\s+')

    left = sorted(data[0])
    right = sorted(data[1])

    total_distance = sum(abs(l - r) for l, r in zip(left, right))

    return total_distance

print(calc_total_distance())


