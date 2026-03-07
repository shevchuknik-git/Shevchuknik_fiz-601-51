v0_kmh = 54
a_mps2 = -0.5

v0_mps = v0_kmh * 1000 / 3600

t = -v0_mps / a_mps2

s = v0_mps * t + 0.5 * a_mps2 * t**2

print(f"Время до сотановки: {t} секунд")
print(f"Расстояние до остановки: {s} метров")