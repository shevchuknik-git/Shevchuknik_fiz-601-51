from math import * 

R = 0.1
v_5rev = 0.1
t = 20

phi = 5 * 2 * pi

omega = v_5rev / R
epsilon = omega**2 / (2 * phi)

a_tau = epsilon * R

v_t = a_tau * t

a_n = v_t**2 / R

print(f"Радиус окружности (R): {R} м")
print(f"Скорость после 5 оборотов (v): {v_5rev} м/с")
print(f"Время (t): {t} с")
print(f"Угол поворота за 5 оборотов (φ): {phi:.2f} рад")
print(f"Угловое ускорение (ε): {epsilon:.6f} рад/с²")
print(f"Тангенциальное ускорение (a_τ): {a_tau:.6f} м/с²")
print(f"Скорость через {t} с (v_t): {v_t:.6f} м/с")
print(f"Нормальное ускорение (a_n): {a_n:.6f} м/с²")
print(f"Нормальное ускорение (a_n) в см/с²: {a_n*100:.2f} см/с²")