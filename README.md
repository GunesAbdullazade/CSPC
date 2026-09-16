# CSPS PW1 LAB A work

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