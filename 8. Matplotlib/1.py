import matplotlib.pyplot as plt
import numpy as np
import scipy.special as sp

fig, ax = plt.subplots(figure=(10, 10), layout="tight")
fig.suptitle("Полиномы Лежандра", size=20)

x = np.linspace(-1, 1)
deg = 7

for i in range(1, deg + 1):
    y = sp.legendre(i)(x)
    ax.plot(x, y, label=f"n = {i}")
ax.legend(loc='lower right')
plt.show()
