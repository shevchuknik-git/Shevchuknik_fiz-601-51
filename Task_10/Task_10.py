from math import *
g = 9.81
R = 6.4e6
h = 1e6

r = R + h
v = sqrt(g * R**2 / r)

v_km_s = v / 1000

omega = v / r 

print(f"Радиус Земли (R): {R:.2e} м")
print(f"Высота орбиты (h): {h:.2e} м")
print(f"Радиус орбиты (r = R + h): {r:.2e} м")
print(f"Линейная скорость (v): {v:.2f} м/с")
print(f"Линейная скорость (v): {v_km_s:.2f} км/с")
print(f"Угловая скорость (ω): {omega:.6f} рад/с")