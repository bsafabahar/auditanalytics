# Audit Analytics: Data Science for the Accounting Profession
## Python Edition

> **Complete Python Package** - Converted from the original R package by J. Christopher Westland

![Audit Analytics](https://images-na.ssl-images-amazon.com/images/I/41SRfppKIyL._SX328_BO1,204,203,200_.jpg)

**ISSN:** 2197-5736, 2197-5744 (electronic)  
**ISBN:** 978-3-030-49090-4, 978-3-030-49091-1 (eBook)  
**DOI:** https://doi.org/10.1007/978-3-030-49091-1

## Overview

Information technology plays a pivotal role in financial control and audit. This Python package provides comprehensive tools for conducting statistically and legally defensible audits using modern data science techniques.

**Key Features:**
- ✅ Statistical sampling functions (discovery, attribute, acceptance)
- ✅ Risk assessment and planning tools
- ✅ Analytical review procedures
- ✅ Machine learning for audit analytics
- ✅ Data extraction and manipulation utilities
- ✅ Comprehensive Jupyter notebooks for each chapter
- ✅ Real-world datasets from the textbook

## Installation

### From source (recommended)

```bash
git clone https://github.com/bsafabahar/auditanalytics.git
cd auditanalytics
pip install -e .
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### For development

```bash
pip install -e ".[dev]"
```

## Quick Start

```python
import auditanalytics as aa
import pandas as pd

# Load audit data
data = aa.data.load_data('random_data.csv')

# Compute summary statistics
stats = aa.core.compute_summary_stats(data)
print(stats)

# Calculate discovery sample size
sample_size = aa.core.discovery_sample_size(confidence=0.95, intolerable_rate=0.05)
print(f"Required sample size: {sample_size}")

# Foot and agree a column
result = aa.core.foot_and_agree(data, 'amount_column', expected_total=100000)
print(f"Total: {result['total']}, Agrees: {result['agrees']}")
```

## Jupyter Notebooks

All chapter examples have been converted to Jupyter notebooks. To use them:

```bash
# Navigate to notebooks directory
cd notebooks

# Start Jupyter
jupyter notebook

# Or use Jupyter Lab
jupyter lab
```

### Available Notebooks

The package includes notebooks for all book chapters covering:

1. **Fundamentals of Auditing Financial Statements** - Basics of audit methodology
2. **Foundations of Audit Analytics** - Statistical foundations
3. **Analysis of Accounting Transactions** - Transaction analysis techniques
4. **Risk Assessment and Planning** - Risk assessment matrices
5. **Analytical Review: Technical Analysis** - Technical analysis tools
6. **Analytical Review: Intelligence Scanning** - Web scraping and data collection
7. **Design of Audit Programs** - Audit program planning
8. **Interim Compliance Tests** - Compliance testing procedures
9. **Substantive Tests** - Substantive testing methods
10. **Sarbanes-Oxley Engagements** - SOX compliance and machine learning
11. **Blockchains, Cybercrime and Forensics** - Security and forensics
12. **Special Engagements: Forecasts and Valuation** - Valuation techniques
13. **Simulated Transactions** - Transaction simulation for service organizations

## Package Structure

```
auditanalytics/
├── auditanalytics/          # Main package
│   ├── core/                # Core statistical functions
│   ├── analytics/           # Advanced analytics
│   ├── data/                # Data loading utilities
│   └── utils/               # Helper functions
├── notebooks/               # Jupyter notebooks
├── data/                    # CSV datasets
├── tests/                   # Unit tests
└── docs/                    # Documentation
```

## Requirements

- **Python:** 3.8 or higher
- **Core Libraries:** pandas, numpy, scipy, matplotlib, seaborn
- **Statistical:** statsmodels, scikit-learn
- **Notebooks:** jupyter, ipython

See `requirements.txt` for complete list.

## Data Files

The package includes 31+ datasets from the textbook, including:

- Audit journal entries
- Financial statement data
- SOX compliance data  
- Security breach datasets
- Industry benchmark data
- And many more...

## Library Mappings (R → Python)

This package maintains functionality from the R version using these equivalents:

- `dplyr` → `pandas`
- `ggplot2` → `matplotlib` + `seaborn` + `plotly`
- `tidyr` → `pandas`
- `readr` → `pandas`
- Statistical functions → `scipy.stats` + `statsmodels`
- `lubridate` → `datetime` + `dateutil`
- ML packages → `scikit-learn` + `tensorflow`/`pytorch`

## Development

### Running Tests

```bash
pytest tests/
```

### Code Quality

```bash
# Format code
black auditanalytics/

# Lint code
flake8 auditanalytics/

# Type checking
mypy auditanalytics/
```

## Book Information

**Title:** Audit Analytics: Data Science for the Accounting Profession  
**Author:** J. Christopher Westland  
**Publisher:** Springer  
**Year:** 2020

### Where to Buy

- [Springer](https://www.springer.com/gp/book/9783030490904)
- [Amazon](https://www.amazon.com/Audit-Analytics-Science-Accounting-Profession/dp/3030490904)
- [Waterstones](https://www.waterstones.com/book/audit-analytics/j-christopher-westland//9783030490904)

## Citation

If you use this package in your research, please cite:

```bibtex
@book{westland2020audit,
  title={Audit Analytics: Data Science for the Accounting Profession},
  author={Westland, J. Christopher},
  year={2020},
  publisher={Springer},
  doi={10.1007/978-3-030-49091-1},
  isbn={978-3-030-49091-1}
}
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the GNU General Public License v3.0 - see the [LICENSE.md](LICENSE.md) file for details.

## Acknowledgments

- Original R package by J. Christopher Westland
- Python conversion maintains scientific accuracy and functionality
- All algorithms and formulas verified against R implementation

## Support

For questions, issues, or contributions, please use the [GitHub issue tracker](https://github.com/bsafabahar/auditanalytics/issues).

---

**Note:** This is the official Python edition of the Audit Analytics package. The original R version is available at [westland/auditanalytics](https://github.com/westland/auditanalytics).
