import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig, ax = plt.subplots()

ratio = np.linspace((0, 1), (5, 5), num=100)
t = np.arange(0, 2 * np.pi, 0.01)
x = np.sin(t)
y = np.sin(t)

line, = ax.plot(x, y)


def init():
    line.set_data([], [])
    return line,


def update(num):
    print(num)
    line.set_data(np.sin(num[0] * t), np.sin(num[1] * t))
    return line,


ani = animation.FuncAnimation(fig, update, frames=np.linspace((0, 1), (4, 4), num=50),
                              init_func=init, blit=True)

plt.show()
