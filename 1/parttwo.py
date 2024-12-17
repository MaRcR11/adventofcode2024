import pandas as pd


def calculate_similarity_score(input_file):
    data = pd.read_csv(input_file, header=None, sep=r"\s+")
    return sum(num * data[1].value_counts().get(num, 0) for num in data[0])


input_file = "input.csv"
print(f"Similarity score: {calculate_similarity_score(input_file)}")
