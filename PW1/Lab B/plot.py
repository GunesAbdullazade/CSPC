import numpy as np
import matplotlib.pyplot as plt

LAMBDA = 0.3

# TODO 1: Read the observed data
t, observed = np.loadtxt(
    "decay_observed.csv",
    delimiter=",",
    skiprows=1,
    unpack=True
)

# TODO 2: Build the analytical decay law
N0 = observed[0]
analytical = N0 * np.exp(-LAMBDA * t)

# TODO 3: Make the 1x2 subplot
fig, axes = plt.subplots(1, 2, sharex=True, sharey=True)

axes[0].scatter(t, observed)
axes[0].set_title("Observed data")
axes[0].set_xlabel("Time")
axes[0].set_ylabel("Count")

axes[1].plot(t, analytical)
axes[1].set_title("Analytical decay law")
axes[1].set_xlabel("Time")
axes[1].set_ylabel("Count")

plt.tight_layout()

# TODO 4: Save the figure
plt.savefig("figure.png", dpi=300)