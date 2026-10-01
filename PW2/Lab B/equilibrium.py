import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import newton, minimize

K = 15

def k_imbalance(x):
    return (2 * x)**2 / ((1 - x) * (1 - x)) - K

x_newton = newton(k_imbalance, 0.5)

def squared_imbalance(x):
    return k_imbalance(x[0])**2

result = minimize(
    squared_imbalance,
    x0=[0.5],
    method="SLSQP",
    bounds=[(0, 0.999999)]
)

x_slsqp = result.x[0]

print("Newton x:", x_newton)
print("SLSQP x:", x_slsqp)

n_H2 = 1 - x_newton
n_I2 = 1 - x_newton
n_HI = 2 * x_newton

print("Equilibrium H2:", n_H2, "mol")
print("Equilibrium I2:", n_I2, "mol")
print("Equilibrium HI:", n_HI, "mol")

x_values = np.linspace(0, 0.99, 300)

plt.figure()
plt.plot(x_values, 1 - x_values, label="H2")
plt.plot(x_values, 1 - x_values, label="I2")
plt.plot(x_values, 2 * x_values, label="HI")
plt.axvline(x_newton, linestyle="--", label="Equilibrium")

plt.xlabel("Reaction extent x")
plt.ylabel("Amount (mol)")
plt.title("H2 + I2 ⇌ 2 HI")
plt.legend()
plt.tight_layout()
plt.savefig("equilibrium.png")
plt.show()
