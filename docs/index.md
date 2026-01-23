# Audit Analytics - Python Edition Documentation

## Overview

Welcome to the Python edition of Audit Analytics: Data Science for the Accounting Profession. This package provides comprehensive tools for conducting statistically and legally defensible audits using modern Python data science libraries.

## Quick Links

- [Installation Guide](installation.md)
- [API Reference](api/index.md)
- [Tutorial Notebooks](../notebooks/)
- [GitHub Repository](https://github.com/bsafabahar/auditanalytics)

## Package Modules

### Core Module (`auditanalytics.core`)

The core module contains fundamental statistical sampling and analysis functions:

#### Sampling Functions
- `discovery_sample_size()` - Calculate sample size for discovery sampling
- `attribute_sample_size()` - Calculate sample size for attribute sampling
- `acceptance_sample_size()` - Calculate sample size for acceptance sampling

#### Statistical Functions
- `foot_and_agree()` - Foot (sum) and agree totals to client records
- `compute_summary_stats()` - Compute comprehensive summary statistics
- `test_normality()` - Test data for normality
- `detect_outliers()` - Detect outliers using various methods

### Data Module (`auditanalytics.data`)

Functions for loading and managing audit data:

- `load_csv()` - Load CSV files with audit-friendly defaults
- `load_data()` - Load data from package data directory
- `save_data()` - Save DataFrames to CSV
- `load_excel()` - Load Excel files
- `list_available_data()` - List all available datasets

### Analytics Module (`auditanalytics.analytics`)

Advanced analytics functions for specialized audit procedures (in development).

### Utils Module (`auditanalytics.utils`)

Utility functions and helpers (in development).

## Getting Started

### Basic Usage Example

```python
import auditanalytics as aa
import pandas as pd

# Load audit data
data = aa.data.load_data('random_data.csv')

# Compute summary statistics
stats = aa.core.compute_summary_stats(data)
print(stats)

# Calculate sample size
sample_size = aa.core.discovery_sample_size(
    confidence=0.95,
    intolerable_rate=0.05
)
print(f"Required sample size: {sample_size}")

# Foot and agree a column
result = aa.core.foot_and_agree(
    data, 
    'amount_column', 
    expected_total=100000
)
print(f"Total: {result['total']}, Agrees: {result['agrees']}")
```

## Jupyter Notebooks

The package includes comprehensive Jupyter notebooks demonstrating all functionality:

- **Chapter 2: Metrics and Estimates** - Basic audit statistics
- **Chapter 4: Sample Sizes** - Statistical sampling methods
- (More notebooks coming soon)

## Data Files

The package includes 31+ real-world datasets from the textbook covering:

- Audit journal entries
- Financial statement data
- SOX compliance datasets
- Security breach data
- Industry benchmarks
- And more...

## Library Equivalents (R to Python)

| R Package | Python Equivalent |
|-----------|------------------|
| dplyr | pandas |
| ggplot2 | matplotlib + seaborn + plotly |
| tidyr | pandas |
| readr | pandas |
| Statistical functions | scipy.stats + statsmodels |
| lubridate | datetime + dateutil |
| ML packages | scikit-learn + tensorflow/pytorch |

## Support

For questions or issues:
- [GitHub Issues](https://github.com/bsafabahar/auditanalytics/issues)
- Email: westland@uic.edu

## Citation

```bibtex
@book{westland2020audit,
  title={Audit Analytics: Data Science for the Accounting Profession},
  author={Westland, J. Christopher},
  year={2020},
  publisher={Springer},
  doi={10.1007/978-3-030-49091-1}
}
```

## License

GNU General Public License v3.0 - See [LICENSE.md](../LICENSE.md)
