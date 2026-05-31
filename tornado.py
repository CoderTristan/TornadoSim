import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

N = 800

angles = np.random.rand(N) * 2 * np.pi
heights = np.random.rand(N) * 10
radii = np.random.rand(N) * 2 + 0.2
speeds = np.random.rand(N) * 0.1 + 0.02

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

scatter = ax.scatter([], [], [], s=5, c='cyan')

ax.set_xlim(-3, 3)
ax.set_ylim(-3, 3)
ax.set_zlim(0, 10)

def update(frame):
    global angles, heights, radii

    angles += speeds

    heights += 0.02

    heights = np.where(heights > 10, 0, heights)

    x = radii * np.cos(angles)
    y = radii * np.sin(angles)
    z = heights

    scatter._offsets3d = (x, y, z)
    return scatter,

ani = FuncAnimation(fig, update, frames=1000, interval=20)
plt.show()
