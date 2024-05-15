import numpy as np

with open('1.txt', 'r') as f:
    a = np.array([[int(num) for num in line.split(',')] for line in f])
print("Sum of all elements:", a.sum())
print("Max element:", a.max())
print("Min element:", a.min())
