import numpy as np
import random
import matplotlib.pyplot as plt
import scipy.integrate as spi


def f(x):
    return x**2 + 15 * x + 19


a = 0
b = 2

n = 10000

x_values = np.linspace(a, b, 400)
y_values = f(x_values)

points_under_curve = 0
for _ in range(n):
    x = random.uniform(a, b)
    y = random.uniform(0, max(y_values))
    if y <= f(x):
        points_under_curve += 1

area = (b - a) * (max(y_values) * points_under_curve / n)

plt.figure(figsize=(10, 6))
plt.plot(x_values, y_values, "b-", label="f(x) = x^2 + 15x + 19")
plt.fill_between(x_values, y_values, color="gray", alpha=0.3, label="Площа під кривою")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.title("Графік функції та площа під кривою за методом Монте-Карло")
plt.legend()
plt.grid(True)
plt.show()

print("Площа під кривою:", area)

result, error = spi.quad(f, a, b)
print("Інтеграл: ", result)
