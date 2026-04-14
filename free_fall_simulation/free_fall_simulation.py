import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

g = -9.81
dt = 0.05
y0 = 100
v0 = 0

t = 0
y = y0
v = v0

t_values = [t]
y_values = [y]
v_values = [v]

while y > 0:
    v = v + g * dt
    y = y + v * dt
    t = t + dt

    t_values.append(t)
    y_values.append(y)
    v_values.append(v)

fig, ax = plt.subplots()

ax.set_xlim(0, max(t_values))
ax.set_ylim(0, max(y_values))

line, = ax.plot([], [], 'b-', linewidth=2, label='Высота')
point, = ax.plot([], [], 'ro')

ax.set_title('Свободное падение')
ax.set_xlabel('Время (с)')
ax.set_ylabel('Высота (м)')
ax.grid(True)
ax.legend()

def update(frame):
    if frame == 0:
        return line, point

    line.set_data(t_values[:frame], y_values[:frame])

    point.set_data([t_values[frame]], [y_values[frame]])

    return line, point

ani = FuncAnimation(fig, update, frames=len(t_values), interval=50)

plt.show()