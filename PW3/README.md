
## Session 1: Heart Disease Dataset

### 1. Data inspection

The Heart Disease dataset contains 303 rows and 14 columns. The dataset includes information such as age, cholesterol level, resting blood pressure, and maximum heart rate.

The continuous variables selected for analysis were:
- Age (`age`)
- Cholesterol (`chol`)
- Resting blood pressure (`trestbps`)
- Maximum heart rate (`thalach`)

### 2. Distribution of continuous variables

Histograms were created to examine the distributions of the four continuous variables. They help us understand how the values are spread and whether the distributions are symmetric or skewed.

The histograms are saved in `distributions.png`.

### 3. Normality test

The Shapiro-Wilk test was used to check whether each continuous variable follows a normal distribution. The significance level was set to 0.05.

The results were:

| Variable | Shapiro-Wilk statistic | p-value | Conclusion |
|---|---:|---:|---|
| Age | 0.9865 | 0.006069 | Not normally distributed |
| Cholesterol | 0.9473 | < 0.000001 | Not normally distributed |
| Resting blood pressure | 0.9665 | 0.000002 | Not normally distributed |
| Maximum heart rate | 0.9765 | 0.000070 | Not normally distributed |

All p-values are below 0.05. Therefore, the Shapiro-Wilk test rejects the null hypothesis of normality for all four variables.

### 2. Distribution of continuous variables

Histograms were created to visualize the distributions of the four continuous variables. Skewness was also calculated to help describe their shapes.

- Age: The distribution is approximately symmetric, with a slight negative skew (−0.208).
- Cholesterol: The distribution is positively skewed (1.130), with a tail extending towards higher values. The maximum value of 564 is much higher than the third quartile of 275.
- Resting blood pressure: The distribution is positively skewed (0.703), meaning that it has a longer tail towards higher values.
- Maximum heart rate: The distribution is negatively skewed (−0.535), meaning that it has a longer tail towards lower values.
### 3. Are the variables normally distributed?

The Shapiro-Wilk test was used to assess whether the four continuous variables follow a normal distribution. The significance level was set to 0.05.

| Variable | Shapiro-Wilk statistic | p-value | Verdict |
|---|---:|---:|---|
| Age | 0.9865 | 0.006069 | Not normally distributed |
| Cholesterol | 0.9473 | < 0.000001 | Not normally distributed |
| Resting blood pressure | 0.9665 | 0.000002 | Not normally distributed |
| Maximum heart rate | 0.9765 | 0.000070 | Not normally distributed |

All four p-values are below 0.05. Therefore, the null hypothesis of normality is rejected for all four variables.

Age is relatively symmetric based on its skewness, but the Shapiro-Wilk test still indicates a statistically significant departure from normality. Cholesterol and resting blood pressure show positive skewness, while maximum heart rate shows negative skewness. These results will help guide the choice of statistical methods in Session 2.
## Session 2: Draw conclusions

### 4. Is the effect real?

The maximum heart rate (`thalach`) was compared between healthy individuals and individuals with heart disease. Since the normality tests in Session 1 indicated departures from normality, the Mann-Whitney U test was used to compare the two groups.

The healthy group contained 164 individuals, while the heart disease group contained 139 individuals.

The mean maximum heart rate was 158.38 for the healthy group, with a 95% confidence interval of [155.42, 161.34]. For the heart disease group, the mean was 139.26, with a 95% confidence interval of [135.47, 143.05].

The Mann-Whitney U statistic was 16989.50, with a p-value of 1.86101 × 10⁻¹³. Since the p-value is below 0.05, the null hypothesis is rejected. There is strong statistical evidence that the distributions of maximum heart rate differ between the two groups.

The plot `thalach_comparison.png` shows the group means and their 95% confidence intervals. The intervals do not overlap, which agrees with the conclusion that the group means differ. However, the Mann-Whitney test compares distributions rather than means directly.

### 5. Do two things move together?

The relationship between age and maximum heart rate was investigated using Spearman's rank correlation.

The Spearman correlation coefficient was −0.3916, with a p-value of 1.51086 × 10⁻¹². This indicates a moderate negative association between age and maximum heart rate. In general, older individuals tend to have lower maximum heart rates.

The scatter plot `age_thalach_scatter.png` visualizes this relationship. The association is statistically significant, but it does not prove that age alone causes the change in maximum heart rate.
## Dataset 2: Chemical-Exposure Mystery

### 6. The naive analysis

The Pearson correlation coefficient was used to measure the association between each chemical and malignancy.

| Chemical | Pearson correlation (r) | p-value |
|---|---:|---:|
| Benzene | 0.3847 | 1.28 × 10⁻³⁶ |
| Cadmium | 0.8800 | < 0.001 |

Both chemicals showed positive associations with malignancy. However, cadmium had a much stronger correlation (r = 0.8800) than benzene (r = 0.3847). Based on this analysis alone, cadmium appeared to be the more likely cause.

### 7. Look again

To investigate the possible influence of pollution, the data were restricted to patients with a pollution index between 40 and 60. This group contained 199 patients.

| Chemical | Pearson correlation (r) | p-value |
|---|---:|---:|
| Benzene | 0.7016 | 8.08 × 10⁻³¹ |
| Cadmium | 0.3157 | 5.57 × 10⁻⁶ |

After restricting the pollution index, the association between cadmium and malignancy became much weaker, decreasing from 0.8800 to 0.3157. In contrast, the association between benzene and malignancy became stronger, increasing from 0.3847 to 0.7016.

These results suggest that the strong overall association between cadmium and malignancy may partly be explained by its relationship with pollution. Benzene maintains a strong positive association within the selected pollution range.

Therefore, benzene appears to be the more likely driver of malignancy in this synthetic dataset, while cadmium appears more suspicious in the initial analysis than it does after accounting for pollution. However, this analysis alone cannot prove causation, and age has not yet been controlled for.
## Bonus: Category Unpredictability

The `target` column was selected to measure how balanced the categories are. The proportions were calculated using `value_counts(normalize=True)`.

| Category | Proportion |
|---|---:|
| target = 0 | 0.5413 (54.13%) |
| target = 1 | 0.4587 (45.87%) |

The entropy was calculated using the formula:

H(X) = -Σ p(x) log₂ p(x)

The calculated entropy was 0.9951 bits. Since the maximum entropy for two categories is 1 bit, this result indicates that the two categories are fairly balanced. Therefore, guessing the `target` category based only on its overall distribution is relatively unpredictable.

Entropy measures the balance of category proportions, not the accuracy of a predictive model.
