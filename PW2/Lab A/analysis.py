import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import cumulative_trapezoid

data = np.loadtxt("freefall.csv", delimiter="\t", skiprows=1)

t = data[:, 0]
y = data[:, 1]

v = np.gradient(y, t)
a = np.gradient(v, t)

print("Mean acceleration:", np.mean(a), "m/s^2")
print("Acceleration std:", np.std(a), "m/s^2")

v_recovered = cumulative_trapezoid(a, t, initial=0) + v[0]

y_recovered = cumulative_trapezoid(v_recovered, t, initial=0) + y[0]

difference = np.abs(y_recovered - y)

print("Largest difference:", np.max(difference), "m")

fig, axes = plt.subplots(3, 1, sharex=True, figsize=(8, 10))

axes[0].plot(t, y)
axes[0].set_ylabel("Position (m)")

axes[1].plot(t, v)
axes[1].set_ylabel("Velocity (m/s)")

axes[2].plot(t, a)
axes[2].axhline(-9.81, linestyle="--", label="-9.81 m/s²")
axes[2].set_ylabel("Acceleration (m/s²)")
axes[2].set_xlabel("Time (s)")
axes[2].legend()

plt.tight_layout()
plt.savefig("motion.png")
# Bonus: 2D trajectory

trajectory = np.loadtxt("trajectory.csv", delimiter="\t", skiprows=1)

t2 = trajectory[:, 0]
x = trajectory[:, 1]
y2 = trajectory[:, 2]

vx = np.gradient(x, t2)
vy = np.gradient(y2, t2)

speed = np.sqrt(vx**2 + vy**2)

plt.figure()
plt.plot(x, y2)
plt.xlabel("x (m)")
plt.ylabel("y (m)")
plt.title("2D Trajectory")
plt.savefig("trajectory.png")

plt.figure()
plt.plot(t2, speed)
plt.xlabel("Time (s)")
plt.ylabel("Speed (m/s)")
plt.title("Speed vs Time")
plt.savefig("speed.png")
print("BONUS WORKED")
