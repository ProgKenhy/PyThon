import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(1, 10, 100)
y = np.linspace(1, 10, 100)




ncols = 2

fig, axs = plt.subplots(1, ncols=ncols, figsize=(8 * ncols, 8), subplot_kw={'projection': '3d'})

axs[0].plot(x, y, z)
axs[0].set_xlabel('x')
axs[0].set_ylabel('y')
axs[0].set_zlabel('z')

axs[1].plot(x, y, np.log(z))
axs[1].set_xlabel('x')
axs[1].set_ylabel('y')
axs[1].set_zlabel('Log(z)')

plt.show()
