import numpy as np


def run_length_encoding(data):
    indices = np.append(np.where(data[1:] != data[:-1]), len(data) - 1)
    value = np.diff(np.append(-1, indices))
    return data[indices], value


x = np.array(list(map(int, input("Enter the necessary vector: ").split())))
result = run_length_encoding(x)
print("run_length_encoding:\t", result)
