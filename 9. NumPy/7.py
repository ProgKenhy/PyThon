import numpy as np

url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
iris = np.genfromtxt(url, delimiter=',', dtype='object')

uniq_values, counter = np.unique(iris[:, -1], return_counts=True)

print("Уникальные значения:", uniq_values)
print("Количество каждого значения:", counter)
