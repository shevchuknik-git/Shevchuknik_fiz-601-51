A = 3
B = 2
C = 1

def s(t):
    return A + B * t + C * t**2

def v(t):
    return B + 2 * C * t

a = 2

def avg_velocity(t1, t2):
    return (s(t2) - s(t1)) / (t2 - t1)

t_intervals = [(0, 1), (1, 2), (2, 3)]

for i, (t1, t2) in enumerate(t_intervals, 1):
    v_avg = avg_velocity(t1, t2)
    print(f"Средняя скорость за {i}-ю секунду: {v_avg}  м/с")
    print(f"Средняя скорость за {i}-ю секунду: {a} м/с²")
