import scipy.integrate as integrate
import math

# Инициализация констант
p0 = 100000
dp = 10000
V0 = 1
alpha = 2
b = 100000

def pV1(v):
  """Функция для первой кривой."""
  return p0 + dp * math.cos(2 * math.pi * alpha * (v - V0))

def pV2(v):
  """Функция для второй кривой."""
  return 0.5 * p0 + b * (v - V0)**2

# Пределы интегрирования
V_min, V_max = 0.331033, 1.66897

# Расчет интегралов
integral_f1 = integrate.quad(pV1, V_min, V_max)[0]
integral_f2 = integrate.quad(pV2, V_max, V_min)[0]

# Расчет A
A = integral_f1 + integral_f2

# Расчет Q1
Q1 = integral_f1 + 1.5 * (pV1(V_max) * V_max - pV1(V_min) * V_min)

# Расчет эффективности n
n = A / Q1 * 100

# Вывод результата
print(f"Эффективность: {n:.2f}%")

