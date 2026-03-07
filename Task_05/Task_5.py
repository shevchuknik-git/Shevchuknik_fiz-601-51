from math import *

v0 = 10
alpha = 45
t = 1
g = 9.81

v0x = v0 * cos(radians(alpha))
v0y = v0 * sin(radians(alpha))

vx = v0x 
vy = v0y - g * t

v = sqrt(vx**2 + vy**2)

beta = atan2(vy, vx)
cos_beta = cos(beta)

an = g* cos_beta

R = v**2 / an

print(f"Горизонтальная скорость (vx): {vx:.2f} м/с")
print(f"Вертикальная скорость (vy): {vy:.2f} м/с")
print(f"Полная скорость (v): {v:.2f} м/с")
print(f"Угол β: {degrees(beta):.2f} °")
print(f"Нормальное ускорение (an): {an:.2f} м/с²")
print(f"Радиус кривизны (R): {R:.2f} м")