import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import mannwhitneyu, spearmanr, t

# Load the dataset
df = pd.read_csv("Heart_disease_cleveland_new.csv")

# Split maximum heart rate into two groups
healthy = df.loc[df["target"] == 0, "thalach"].dropna()
disease = df.loc[df["target"] == 1, "thalach"].dropna()

# Task 4: Compare the two groups
print("TASK 4: Maximum heart rate comparison")
print(f"Healthy group size: {len(healthy)}")
print(f"Disease group size: {len(disease)}")

# Calculate means and 95% confidence intervals
for name, group in [("Healthy", healthy), ("Disease", disease)]:
    mean = group.mean()
    sem = group.sem()
    margin = t.ppf(0.975, len(group) - 1) * sem
    print(
        f"{name}: mean = {mean:.2f}, "
        f"95% CI = ({mean - margin:.2f}, {mean + margin:.2f})"
    )

# Mann-Whitney U test
u_stat, p_value = mannwhitneyu(
    healthy, disease, alternative="two-sided"
)
print(f"Mann-Whitney U statistic: {u_stat:.2f}")
print(f"p-value: {p_value:.6g}")

# Plot group means with 95% confidence intervals
groups = [healthy, disease]
labels = ["Healthy", "Heart disease"]
means = [group.mean() for group in groups]
errors = [
    t.ppf(0.975, len(group) - 1) * group.sem()
    for group in groups
]

plt.figure(figsize=(7, 5))
plt.bar(labels, means, yerr=errors, capsize=8)
plt.ylabel("Maximum heart rate (thalach)")
plt.title("Mean maximum heart rate by group (95% CI)")
plt.tight_layout()
plt.savefig("thalach_comparison.png")
plt.close()

# Task 5: Relationship between age and maximum heart rate
correlation, corr_p = spearmanr(df["age"], df["thalach"])

print("\nTASK 5: Relationship between age and maximum heart rate")
print(f"Spearman correlation: {correlation:.4f}")
print(f"p-value: {corr_p:.6g}")

# Scatter plot
plt.figure(figsize=(7, 5))
plt.scatter(df["age"], df["thalach"], alpha=0.7)
plt.xlabel("Age")
plt.ylabel("Maximum heart rate (thalach)")
plt.title("Age vs maximum heart rate")
plt.tight_layout()
plt.savefig("age_thalach_scatter.png")
plt.close()

print("\nPlots saved:")
print("thalach_comparison.png")
print("age_thalach_scatter.png")
