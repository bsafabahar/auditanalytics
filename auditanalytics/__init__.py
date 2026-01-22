"""
Audit Analytics: Data Science for the Accounting Profession
Python Edition

This package provides tools and utilities for audit analytics, 
statistical sampling, risk assessment, and financial data analysis.

Original R package by J. Christopher Westland
Python conversion maintains all functionality with modern Python libraries.
"""

__version__ = "0.1.0"
__author__ = "J. Christopher Westland"
__email__ = "westland@uic.edu"

# Import main submodules for easy access
from . import core
from . import analytics
from . import data
from . import utils

__all__ = ['core', 'analytics', 'data', 'utils', '__version__']
