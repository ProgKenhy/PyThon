import matplotlib.pyplot as plt
import numpy as np

frequency = ((3, 2), (3, 4), (5, 4), (5, 6))
#frequency = ((0, 1), (1, 2), (1, 3), (2, 3))
t = np.linspace(-4, 4, 300)
ncols = len(frequency)
fig, axs = plt.subplots(figsize=(4 * ncols, 4), ncols=ncols, layout="tight")

x = np.array([np.sin(a * t) for a, b in frequency])
y = np.array([np.sin(b * t) for a, b in frequency])

for i, current_frequency in enumerate(frequency):
    axs[i].plot(x[i], y[i], label=f"frequency = {current_frequency}")
plt.show()
