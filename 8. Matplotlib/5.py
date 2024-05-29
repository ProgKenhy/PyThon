import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(1, 10, 100)
y = np.linspace(1, 15, 150)
average = np.mean(x) + np.mean(y) / 2
x, y = np.meshgrid(x, y)
z = (x+y - average)**2



ncols = 2

fig, axs = plt.subplots(1, ncols=ncols, figsize=(8 * ncols, 8), subplot_kw={'projection': '3d'})

axs[0].plot_surface(x, y, z)
axs[0].set_xlabel('x')
axs[0].set_ylabel('y')
axs[0].set_zlabel('z')

axs[1].plot_surface(x, y, np.log(z))
axs[1].set_xlabel('x')
axs[1].set_ylabel('y')
axs[1].set_zlabel('Log(z)')

plt.show()
