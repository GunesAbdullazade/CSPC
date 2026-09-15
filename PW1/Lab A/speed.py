import time

from decay import simulate_loop, simulate


N0 = 200000
lam = 0.1
dt = 0.05
steps = 200
seed = 0

start = time.perf_counter()
simulate_loop(N0, lam, dt, steps, seed)
loop_time = time.perf_counter() - start

start = time.perf_counter()
simulate(N0, lam, dt, steps, seed)
numpy_time = time.perf_counter() - start

print(f"Pure Python time: {loop_time:.6f} seconds")
print(f"NumPy time: {numpy_time:.6f} seconds")
print(f"NumPy is {loop_time / numpy_time:.2f} times faster")
