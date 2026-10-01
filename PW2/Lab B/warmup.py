import numpy as np
from scipy.optimize import newton, minimize

# ---------- 2A: easy convex function ----------

def f(x):
    return (x - 3)**2 + 1

def df(x):
    return 2 * (x - 3)

def d2f(x):
    return 2.0

x0 = 0.0

# (1) Gradient Descent
x = x0
lr = 0.1

for i in range(10000):
    step = lr * df(x)
    x = x - step

    if abs(step) < 1e-8:
        break

print("2A Gradient Descent:", x, f(x))

# (2) Newton
x_newton = newton(df, x0, fprime=d2f)
print("2A Newton:", x_newton, f(x_newton))

# (3) SLSQP
result = minimize(f, x0, method="SLSQP")
print("2A SLSQP:", result.x[0], result.fun)

# ---------- 2B: harder landscape ----------

def g(x):
    return x**4 - 3*x**2 + x + 5

def dg(x):
    return 4*x**3 - 6*x + 1

def d2g(x):
    return 12*x**2 - 6

# ---------- 2B: harder landscape ----------

for x0 in [0.0, 2.0]:

    print("\n2B starting point:", x0)

    # (1) Gradient Descent
    x = x0
    lr = 0.01

    for i in range(100000):
        step = lr * dg(x)
        x = x - step

        if abs(step) < 1e-8:
            break

    print("Gradient Descent:", x, g(x))
    print("d2g:", d2g(x))

    # (2) Newton
    x_newton = newton(dg, x0, fprime=d2g)

    print("Newton:", x_newton, g(x_newton))
    print("d2g:", d2g(x_newton))

    if d2g(x_newton) > 0:
        print("Newton found a minimum")
    elif d2g(x_newton) < 0:
        print("Newton found a maximum")
    else:
        print("Newton found a stationary inflection point")

    # (3) SLSQP
    result = minimize(g, x0, method="SLSQP")

    print("SLSQP:", result.x[0], result.fun)
    print("d2g:", d2g(result.x[0]))
