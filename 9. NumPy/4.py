import numpy as np

x = np.array([6, 2, 0, 3, 0, 0, 5, 7, 0])
max_element = np.max(x[1:][x[:-1] == 0])
print("Max element after zero:", max_element)