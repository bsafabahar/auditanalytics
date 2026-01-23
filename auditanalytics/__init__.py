"""
Audit Analytics: Data Science for the Accounting Profession
Python implementation of audit analytics tools

This package provides tools and datasets for conducting statistical audits
of financial statements using modern data science techniques.
"""

__version__ = "0.1.0"
__author__ = "J. Christopher Westland"
__email__ = "westland@uic.edu"

from .data import load_dataset, list_datasets
from .utils import (
    discovery_sample_size,
    attribute_sample_size,
    monetary_unit_sample_size,
    stratified_sample_allocation,
    benford_analysis
)

__all__ = [
    'load_dataset', 
    'list_datasets',
    'discovery_sample_size',
    'attribute_sample_size',
    'monetary_unit_sample_size',
    'stratified_sample_allocation',
    'benford_analysis',
    '__version__'
]
