"""
PW2 Lab B Part 3 -- fit a reaction's rate constant to measured data.
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize

# TODO 1: read kinetics.csv
data = np.loadtxt("kinetics.csv", delimiter=",", skiprows=1)

t = data[:, 0]
C = data[:, 1]

C0 = C[0]


# TODO 2: total error
def total_error(k):
    k = k[0]
    C_model = C0 * np.exp(-k * t)
    return np.sum((C - C_model)**2)


# TODO 3: minimize the error
result = minimize(
    total_error,
    x0=[0.5],
    method="SLSQP",
    bounds=[(0, 5)]
)

k_fitted = result.x[0]

print("Fitted k:", k_fitted)


# TODO 4: plot measured data and fitted curve
C_fitted = C0 * np.exp(-k_fitted * t)

plt.figure()
plt.scatter(t, C, label="Measured data")
plt.plot(t, C_fitted, label="Fitted curve")

plt.xlabel("Time")
plt.ylabel("Concentration")
plt.title("First-order reaction rate fitting")
plt.legend()
plt.tight_layout()

plt.savefig("kinetics.png")
plt.show()
