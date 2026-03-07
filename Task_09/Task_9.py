from math import *
G = 6.67e-11
M = 5.97e24
R = 6.371e6
H = 3.2e6

r = R + H

v = sqrt(G * M / r)

v_km_s = v / 1000

print(f"Радиус Земли (R): {R:.2e} м")
print(f"Высота орбиты (H): {H:.2e} м")
print(f"Радиус орбиты (r = R + H): {r:.2e} м")
print(f"Линейная скорость (v): {v:.2f} м/с")
print(f"Линейная скорость (v): {v_km_s:.2f} км/с")