import numpy as np

data = np.random.normal(size=(10, 4))

print("Min:", data.max())
print("Max:", data.min())
print("Average:", data.sum() / (len(data) * len(data[0])))
print("Standard отклонение:", data.std())
first_five_rows = data[:5]
print("First five rows: \n", first_five_rows)