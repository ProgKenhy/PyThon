import numpy as np


def run_length_encoding(data):
    unique_values, counts = np.unique(data, return_counts=True)
    return unique_values, counts


x = np.array([list(map(int, input("Enter the necessary vector: ").split()))])
result = run_length_encoding(x)
print(result)
