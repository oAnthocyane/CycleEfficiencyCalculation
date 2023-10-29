import scipy.integrate as integrate
import math

# Константы
p0 = 100_000
dp = 10_000
V0 = 1
alpha = 2
beta = 100_000
v_min = 0.331033
v_max = 1.66897

def pV1(v):
    """Функция для первой кривой."""
    return p0 + dp * math.cos(2 * math.pi * alpha * (v - V0))

def pV2(v):
    """Функция для второй кривой."""
    return 0.5 * p0 + beta * (v - V0)**2

# Интегрирование функций
A1 = integrate.quad(pV1, v_min, v_max)[0]
A2 = integrate.quad(pV2, v_max, v_min)[0]

# Общая площадь под кривыми
A = A1 + A2

# КПД
n = A / A1 * 100

print(n)

