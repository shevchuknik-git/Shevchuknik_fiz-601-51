from math import *

t = 0.5
g = 9.81
k = 1.5

vy = g * t

vx_squared = vy**2 / (k**2 - 1)
vx = sqrt(vx_squared)

print(f"Горизонтальная скорость броска vx = {vx:.2f} м/с")