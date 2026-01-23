"""Data loading utilities for Audit Analytics package"""
import pandas as pd
import os
from pathlib import Path

def load_dataset(name):
    """
    Load a dataset by name from the package data directory.
    
    Parameters
    ----------
    name : str
        Name of the dataset (without .csv extension)
        
    Returns
    -------
    pandas.DataFrame
        The loaded dataset
        
    Examples
    --------
    >>> df = load_dataset('ch1_enrollment')
    >>> df = load_dataset('random_data')
    """
    # Get the path to the data directory
    current_dir = Path(__file__).parent
    data_path = current_dir / f'{name}.csv'
    
    if not data_path.exists():
        raise FileNotFoundError(f"Dataset '{name}' not found. Available datasets can be listed by checking the data directory.")
    
    return pd.read_csv(data_path)

def list_datasets():
    """
    List all available datasets in the package.
    
    Returns
    -------
    list
        List of available dataset names (without .csv extension)
    """
    current_dir = Path(__file__).parent
    csv_files = list(current_dir.glob('*.csv'))
    return [f.stem for f in csv_files]

__all__ = ['load_dataset', 'list_datasets']
