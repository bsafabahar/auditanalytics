"""
Utility module for audit analytics functions.

This module provides common utility functions used across the audit analytics package.
"""

import pandas as pd
import numpy as np
from pathlib import Path


def get_data_path(filename):
    """
    Get the absolute path to a data file in the data directory.
    
    Parameters:
    -----------
    filename : str
        Name of the data file
        
    Returns:
    --------
    str
        Absolute path to the data file
    """
    # Get the package directory
    package_dir = Path(__file__).parent.parent
    data_dir = package_dir / "data"
    
    # Return the full path
    return str(data_dir / filename)


def load_csv(filename, **kwargs):
    """
    Load a CSV file from the data directory.
    
    Parameters:
    -----------
    filename : str
        Name of the CSV file
    **kwargs : dict
        Additional arguments to pass to pandas.read_csv()
        
    Returns:
    --------
    pd.DataFrame
        Loaded dataframe
    """
    filepath = get_data_path(filename)
    return pd.read_csv(filepath, **kwargs)


def foot_total(df, column):
    """
    Calculate the total (foot) of a column in a dataframe.
    
    This is the audit term for summing a column.
    
    Parameters:
    -----------
    df : pd.DataFrame
        The dataframe
    column : str
        Name of the column to foot
        
    Returns:
    --------
    float
        The sum of the column
    """
    return df[column].sum()
