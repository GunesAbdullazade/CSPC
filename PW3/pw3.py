import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import shapiro

# Load the teacher's Heart Disease dataset
df = pd.read_csv("Heart_disease_cleveland_new.csv")


# TASK 1: Load and inspect the data

print("TASK 1: DATA INSPECTION")

print("\nShape:")
print(df.shape)

print("\nFirst rows:")
print(df.head())

print("\nColumn names:")
print(df.columns.tolist())

print("\nData types:")
print(df.dtypes)

print("\nMissing values:")
print(df.isnull().sum())

print("\nDuplicate rows:")
print(df.duplicated().sum())


# TASK 2: Descriptive statistics

print("\nTASK 2: DESCRIPTIVE STATISTICS")

continuous_vars = ["age", "chol", "trestbps", "thalach"]

print("\nContinuous variables:")
print(df[continuous_vars].head())

print("\nDescriptive statistics:")
print(df[continuous_vars].describe())

print("\nSkewness:")
print(df[continuous_vars].skew())


# TASK 3: Test for normality

print("\nTASK 3: NORMALITY TEST")

for column in continuous_vars:
    statistic, p_value = shapiro(df[column].dropna())

    print(f"\nVariable: {column}")
    print(f"Shapiro-Wilk statistic: {statistic:.4f}")
    print(f"p-value: {p_value:.6g}")

    if p_value < 0.05:
        print("Conclusion: The data do not follow a normal distribution.")
    else:
        print("Conclusion: There is insufficient evidence to reject normality.")


# Create distribution plots

df[continuous_vars].hist(
    bins=15,
    figsize=(10, 8),
    edgecolor="black"
)

plt.suptitle("Distributions of Continuous Variables")
plt.tight_layout()
plt.savefig("distributions.png", dpi=300)
plt.close()

print("\nDistribution plot saved as distributions.png")

print("\nAll tasks completed successfully.")
# BONUS: How unpredictable is a category?

print("\nBONUS: CATEGORY UNPREDICTABILITY")

# Calculate category proportions
proportions = df["target"].value_counts(normalize=True)

print("\nTarget proportions:")
print(proportions)

# Calculate entropy in bits
entropy = -(proportions * __import__("math").log2(1)).sum() if False else 0

import numpy as np

entropy = -(proportions * np.log2(proportions)).sum()

print(f"\nEntropy: {entropy:.4f} bits")

if entropy < 0.5:
    print("The category is quite imbalanced and relatively predictable.")
else:
    print("The categories are fairly balanced and relatively unpredictable.")
# TASK 6: Chemical dataset analysis

print("\nTASK 6: CHEMICAL DATASET ANALYSIS")

chem = pd.read_excel("chemicals_cancer (1).csv")

print("\nDataset shape:")
print(chem.shape)

print("\nFirst rows:")
print(chem.head())

print("\nMissing values:")
print(chem.isnull().sum())

print("\nPearson correlations with malignancy:")

from scipy.stats import pearsonr

for column in ["benzene", "cadmium", "pollution_index", "age"]:
    r, p = pearsonr(chem[column], chem["malignancy"])
    print(f"{column}: r={r:.4f}, p={p:.6g}")

print("\nCorrelation matrix:")
print(chem.corr(numeric_only=True).round(3))


# TASK 7: Multiple linear regression

print("\nTASK 7: MULTIPLE LINEAR REGRESSION")

import statsmodels.api as sm

X = chem[["benzene", "cadmium", "pollution_index", "age"]]
X = sm.add_constant(X)

y = chem["malignancy"]

model = sm.OLS(y, X).fit()

print(model.summary())

print("\nR-squared:", round(model.rsquared, 4))

print("\nRegression coefficients:")
print(model.params.round(4))

print("\nP-values:")
print(model.pvalues.round(6))


# Chemical analysis conclusion

print("\nINTERPRETATION")
print(
    "Cadmium and pollution index are strongly correlated. "
    "After adjusting for benzene, pollution index, and age, "
    "cadmium is not statistically significant in this model. "
    "These associations do not prove causation."
)
