import matplotlib
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

matplotlib.use('TkAgg')

N = 250

# Начални позиции на звездите
r = np.random.rand(N) * 12 + 5
theta = np.random.rand(N) * 2 * np.pi
x = r * np.cos(theta)
y = r * np.sin(theta)

# Различни цветове за звездите
colors = np.random.choice(["white", "yellow", "orange", "lightblue", "red"], N)

fig, ax = plt.subplots(figsize=(6, 6))
ax.set_facecolor("black")
ax.set_xlim(-20, 20)
ax.set_ylim(-20, 20)
ax.set_xticks([])
ax.set_yticks([])
ax.set_title("Черна дупка + пулсар", color="white")

# Черна дупка
black_hole = plt.Circle((0, 0), 2.5, color="black", zorder=3)
ax.add_artist(black_hole)

# Акреционен диск
ring_theta = np.linspace(0, 2 * np.pi, 300)
ring_r = 4.5
ax.plot(ring_r * np.cos(ring_theta), ring_r * np.sin(ring_theta),
        color="orange", linewidth=2, alpha=0.8)

# Звезди
scat = ax.scatter(x, y, s=5, c=colors)

# Пулсар (специална звезда)
pulsar, = ax.plot([10], [0], 'o', color="deepskyblue", markersize=32)


def update(frame):
    # Пулсация (синусоидално)
    size = 8 + 6 * (0.5 + 0.5 * np.sin(frame * 0.3))
    pulsar.set_markersize(size)
    return scat, pulsar


ani = FuncAnimation(fig, update, frames=500, interval=50, blit=True)
plt.show()
