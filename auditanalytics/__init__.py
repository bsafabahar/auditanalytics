"""
Audit Analytics: Data Science for the Accounting Profession
Python implementation of audit analytics tools

This package provides tools and datasets for conducting statistical audits
of financial statements using modern data science techniques.
"""

__version__ = "0.1.0"
__author__ = "J. Christopher Westland"
__email__ = "westland@uic.edu"

from .data import load_dataset

__all__ = ['load_dataset', '__version__']
