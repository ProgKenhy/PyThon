import numpy as np

a = np.arange(16).reshape(4, 4)
a[[1, 3]] = a[[3, 1]]

print(a)
