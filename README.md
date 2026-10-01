# CSPC

## PW1 --- Lab A

### Tests

All three tests pass successfully with `pytest -v`.

- Test for the initial value of the simulation: PASS
- Test for negative decay rate raising `ValueError`: PASS
- Test for the average simulation result being close to the theoretical value: PASS

### Speed comparison

The simulation was run with 200000 atoms.

- Pure Python loop: 9.863218 seconds
- NumPy simulation: 0.000369 seconds
- Speed-up: 26760.77 times faster with NumPy

### Conclusion

The tests confirm that the simulation works correctly, including handling an invalid negative decay rate. The speed comparison shows that the NumPy implementation is much faster than the pure-Python loop for a large number of atoms. This demonstrates why vectorized NumPy operations are useful for computational simulations.

## PW1 --- Lab B

### Result

The observed decay data shows that the particle count decreases over time. The decrease is approximately exponential, which is consistent with the expected radioactive decay behavior.

From the figure, the observed data is close to the analytical decay law \(N(t)=N_0e^{-\lambda t}\) with \(\lambda=0.3\). The points do not match the analytical curve exactly, but the overall trend is very similar, so the observed data reasonably matches the analytical law.

The Snakemake pipeline connects the observed CSV data to the generated figure and runs `plot.py` only when the required output is missing or needs to be updated.

## PW2 --- Lab A

### Result

The noisy position data was used to calculate velocity and acceleration by numerical differentiation.

- Mean acceleration: **-8.58 m/s²**
- Acceleration standard deviation: **28.72 m/s²**
- Largest difference after recovering the position: **0.785 m**

### Analysis

The acceleration data is very noisy because numerical differentiation amplifies measurement noise. This effect becomes even stronger when taking the derivative twice: first to obtain velocity and then to obtain acceleration.

The noisy acceleration was then integrated to recover velocity and position. The recovered position was close to the original measured position, with a maximum difference of **0.785 m**, which is within the expected approximately **1 m** range.

### Conclusion

This lab demonstrates that differentiation amplifies noise, while integration tends to reduce its effect. The results also show that the original motion can be reasonably recovered by integrating the calculated acceleration.

## PW2 --- Lab B

### Part 2 — Optimization methods

Three optimization methods were compared: Gradient Descent, Newton's method, and SLSQP.

For the simple convex function, all three methods converged to the same minimum at approximately x = 3, with f(x) = 1.

For the harder function, the methods did not always converge to the same stationary point. The result depended on the starting point and the optimization method. Gradient Descent and SLSQP found local minima, while Newton's method could converge to a maximum depending on the starting point.

### Part 3 — Reaction rate fitting

The first-order reaction model C(t) = C0 exp(-kt) was fitted to the measured concentration data using SLSQP optimization.

- Fitted rate constant: k = 0.2618

The fitted value is close to the expected value of approximately 0.25, and the fitted curve follows the measured data.

### Part 4 — Chemical equilibrium

For the reaction H2 + I2 ⇌ 2HI, the equilibrium extent was found using Newton's root-finding method and SLSQP minimization.

- Newton: x = 0.65946
- SLSQP: x = 0.65946

The two methods give essentially the same equilibrium extent.

The equilibrium amounts are:

- H2: 0.3405 mol
- I2: 0.3405 mol
- HI: 1.3189 mol

### Part 5 — Titration equivalence point

The titration data was analyzed by calculating the pH slope using np.gradient.

- Equivalence point: 50.0 mL

The pH curve shows a sharp jump near 50 mL, and the slope reaches its maximum at the same volume.

