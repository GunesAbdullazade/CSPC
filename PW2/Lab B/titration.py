import numpy as np
import matplotlib.pyplot as plt

# TODO 1: read titration.csv
data = np.loadtxt("titration.csv", delimiter=",", skiprows=1)

V = data[:, 0]
pH = data[:, 1]

# TODO 2: calculate slope and find equivalence point
slope = np.gradient(pH, V)

equilibrium_index = np.argmax(slope)
equivalence_volume = V[equilibrium_index]

print("Equivalence point:", equivalence_volume, "mL")

# TODO 3: make two plots
fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# pH curve
axes[0].plot(V, pH)
axes[0].axvline(
    equivalence_volume,
    linestyle="--",
    label="Equivalence point"
)
axes[0].set_xlabel("Volume of base (mL)")
axes[0].set_ylabel("pH")
axes[0].set_title("Titration curve")
axes[0].legend()

# Slope curve
axes[1].plot(V, slope)
axes[1].axvline(
    equivalence_volume,
    linestyle="--",
    label="Maximum slope"
)
axes[1].set_xlabel("Volume of base (mL)")
axes[1].set_ylabel("dpH/dV")
axes[1].set_title("Slope of titration curve")
axes[1].legend()

plt.tight_layout()
plt.savefig("titration.png")
plt.show()
