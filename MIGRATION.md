# Migration Guide: R to Python

This guide helps users transition from the R version of auditanalytics to the Python version.

## Installation

### R (Old)
```r
devtools::install_github("westland/auditanalytics")
```

### Python (New)
```bash
pip install -e .
# or
pip install -r requirements.txt
```

## Loading the Package

### R (Old)
```r
library(auditanalytics)
```

### Python (New)
```python
import auditanalytics as aa
import pandas as pd
import numpy as np
```

## Loading Datasets

### R (Old)
```r
data <- read.csv("path/to/ch1_enrollment.csv")
```

### Python (New)
```python
data = aa.load_dataset('ch1_enrollment')
```

## Basic Statistics

### R (Old)
```r
summary(data)
mean(data$column)
sd(data$column)
```

### Python (New)
```python
data.describe()
data['column'].mean()
data['column'].std()
```

## Data Manipulation

### R (Old - dplyr)
```r
library(dplyr)
result <- data %>%
  filter(amount > 1000) %>%
  select(customer, amount) %>%
  group_by(customer) %>%
  summarize(total = sum(amount))
```

### Python (New - pandas)
```python
result = (data
    .query('amount > 1000')
    [['customer', 'amount']]
    .groupby('customer')
    .agg({'amount': 'sum'})
)
```

## Plotting

### R (Old - ggplot2)
```r
library(ggplot2)
ggplot(data, aes(x=x, y=y)) +
  geom_point() +
  geom_smooth(method="lm") +
  theme_minimal()
```

### Python (New - seaborn/matplotlib)
```python
import seaborn as sns
import matplotlib.pyplot as plt

sns.set_style('whitegrid')
sns.regplot(data=data, x='x', y='y')
plt.show()
```

## Statistical Tests

### R (Old)
```r
# T-test
t.test(x, y)

# Correlation
cor.test(x, y)

# Linear regression
model <- lm(y ~ x, data=data)
summary(model)
```

### Python (New)
```python
from scipy import stats
import statsmodels.formula.api as smf

# T-test
stats.ttest_ind(x, y)

# Correlation
stats.pearsonr(x, y)

# Linear regression
model = smf.ols('y ~ x', data=data).fit()
print(model.summary())
```

## Audit-Specific Functions

### Discovery Sample Size

**R (Old)**
```r
confidence <- 0.95
n <- (log(1-confidence))/log(1-0.05)
```

**Python (New)**
```python
n = aa.discovery_sample_size(confidence=0.95, intolerable_error_rate=0.05)
```

### Attribute Sample Size

**R (Old)**
```r
library(pwr)
size <- 1000
Delta <- 0.05 * size
sigma <- 0.3 * size
effect <- Delta/sigma
sample <- pwr.t.test(d=effect, sig.level=0.05, power=0.8, 
                     type="one.sample", alternative="greater")
```

**Python (New)**
```python
n = aa.attribute_sample_size(size=1000, delta_pct=0.05, sigma_pct=0.3)
```

### Monetary Unit Sampling

**Python (New - not available in R version)**
```python
n = aa.monetary_unit_sample_size(
    population_value=1000000,
    tolerable_error=50000,
    confidence=0.95
)
```

### Benford's Law Analysis

**Python (New - not available in R version)**
```python
results = aa.benford_analysis(financial_data, digit=1)
print(f"Chi-square: {results.attrs['chi2_statistic']:.4f}")
print(f"P-value: {results.attrs['p_value']:.4f}")
```

## Notebooks

### R (Old)
- R Markdown (.Rmd files)
- Run in RStudio

### Python (New)
- Jupyter Notebooks (.ipynb files)
- Run with: `jupyter notebook`
- Located in: `auditanalytics/notebooks/`

## Key Differences

1. **Indexing**: R uses 1-based indexing, Python uses 0-based indexing
2. **Missing Values**: R uses `NA`, Python uses `NaN` or `None`
3. **Assignment**: R uses `<-` or `=`, Python uses `=`
4. **Packages**: R uses `library()`, Python uses `import`
5. **Piping**: R uses `%>%`, Python uses method chaining or line continuation

## Common Pitfalls

### 1. Integer Division
- **R**: `/` always returns float
- **Python**: Use `//` for integer division, `/` for float division

### 2. Array/Vector Subsetting
- **R**: `data[data$x > 5, ]`
- **Python**: `data[data['x'] > 5]` or `data.query('x > 5')`

### 3. NA/NaN Handling
- **R**: `is.na()`, `na.omit()`
- **Python**: `isna()`, `dropna()`, `fillna()`

### 4. Column Selection
- **R**: `data$column` or `data[, "column"]`
- **Python**: `data['column']` or `data.column`

## Additional Resources

- Python pandas documentation: https://pandas.pydata.org/docs/
- Statsmodels documentation: https://www.statsmodels.org/
- Seaborn gallery: https://seaborn.pydata.org/examples/index.html
- SciPy stats: https://docs.scipy.org/doc/scipy/reference/stats.html

## Getting Help

- GitHub Issues: https://github.com/bsafabahar/auditanalytics/issues
- Python documentation: https://docs.python.org/3/
- Stack Overflow: Tag questions with `python` and `audit`
