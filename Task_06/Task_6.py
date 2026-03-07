from math import *

omega = 20
N = 10
omega_0 = 0

phi = N * 2 * pi

epsilon = omega**2 / (2 * phi)

print(f"Количество оборотов (N): {N} об")
print(f"Конечная угловая скорость (ω): {omega} рад/с")
print(f"Полный угол поворота (φ): {phi:.2f} рад")
print(f"Угловое ускорение (ε): {epsilon:.3f} рад/с²")
print(f"Угловое ускорение (ε) с точностью до π: {10/pi} рад/с²")