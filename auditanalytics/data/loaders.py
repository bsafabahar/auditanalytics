"""
Data loading and handling functions.

This module provides utilities for loading CSV files and other
data sources commonly used in audit analytics.
"""

import pandas as pd
from pathlib import Path
from typing import Union, Optional


def load_csv(filepath: Union[str, Path],
             encoding: str = 'utf-8',
             **kwargs) -> pd.DataFrame:
    """
    Load CSV file with audit-friendly defaults.

    Parameters
    ----------
    filepath : str or Path
        Path to CSV file
    encoding : str, optional
        File encoding (default: 'utf-8')
    **kwargs
        Additional arguments passed to pd.read_csv

    Returns
    -------
    pd.DataFrame
        Loaded data

    Examples
    --------
    >>> df = load_csv('data/transactions.csv')
    >>> df = load_csv('data/journal.csv', parse_dates=['date'])
    """
    # Convert to Path object for easier handling
    filepath = Path(filepath)

    if not filepath.exists():
        raise FileNotFoundError(f"File not found: {filepath}")

    # Default kwargs for audit data
    default_kwargs = {
        'encoding': encoding,
        'low_memory': False,  # Read entire file for accurate type inference
    }

    # Merge with user-provided kwargs
    default_kwargs.update(kwargs)

    df = pd.read_csv(filepath, **default_kwargs)

    return df


def load_data(filename: str,
              data_dir: Optional[Union[str, Path]] = None,
              **kwargs) -> pd.DataFrame:
    """
    Load data file from the package data directory or specified location.

    This is a convenience function that looks for data in the package's
    data directory or a user-specified directory.

    Parameters
    ----------
    filename : str
        Name of the data file
    data_dir : str or Path, optional
        Directory containing data files. If None, looks in package data dir
    **kwargs
        Additional arguments passed to load_csv

    Returns
    -------
    pd.DataFrame
        Loaded data

    Examples
    --------
    >>> df = load_data('random_data.csv')
    >>> df = load_data('sox_data.csv', data_dir='/path/to/data')
    """
    # Determine data directory
    if data_dir is None:
        # Look for data in several possible locations
        possible_paths = [
            Path('data') / filename,  # Current directory
            Path('../data') / filename,  # Parent directory
            Path(__file__).parent.parent.parent / 'data' / filename,  # Package data
            Path.cwd() / 'data' / filename,  # CWD data directory
        ]

        for path in possible_paths:
            if path.exists():
                return load_csv(path, **kwargs)

        raise FileNotFoundError(
            f"Could not find {filename} in any standard data location. "
            f"Tried: {[str(p) for p in possible_paths]}"
        )
    else:
        filepath = Path(data_dir) / filename
        return load_csv(filepath, **kwargs)


def save_data(df: pd.DataFrame,
              filename: str,
              data_dir: Optional[Union[str, Path]] = None,
              **kwargs) -> None:
    """
    Save DataFrame to CSV file.

    Parameters
    ----------
    df : pd.DataFrame
        Data to save
    filename : str
        Output filename
    data_dir : str or Path, optional
        Output directory (default: 'data' in current directory)
    **kwargs
        Additional arguments passed to pd.to_csv
    """
    if data_dir is None:
        data_dir = Path('data')
    else:
        data_dir = Path(data_dir)

    # Create directory if it doesn't exist
    data_dir.mkdir(parents=True, exist_ok=True)

    filepath = data_dir / filename

    # Default kwargs
    default_kwargs = {
        'index': False,
        'encoding': 'utf-8',
    }
    default_kwargs.update(kwargs)

    df.to_csv(filepath, **default_kwargs)


def load_excel(filepath: Union[str, Path],
               sheet_name: Union[str, int] = 0,
               **kwargs) -> pd.DataFrame:
    """
    Load Excel file.

    Parameters
    ----------
    filepath : str or Path
        Path to Excel file
    sheet_name : str or int, optional
        Sheet name or index (default: 0)
    **kwargs
        Additional arguments passed to pd.read_excel

    Returns
    -------
    pd.DataFrame
        Loaded data
    """
    filepath = Path(filepath)

    if not filepath.exists():
        raise FileNotFoundError(f"File not found: {filepath}")

    return pd.read_excel(filepath, sheet_name=sheet_name, **kwargs)


def get_data_path() -> Path:
    """
    Get the path to the package data directory.

    Returns
    -------
    Path
        Path to data directory
    """
    # Try to find the data directory
    possible_paths = [
        Path('data'),
        Path('../data'),
        Path(__file__).parent.parent.parent / 'data',
    ]

    for path in possible_paths:
        if path.exists() and path.is_dir():
            return path.resolve()

    # If not found, return default
    return Path('data')


def list_available_data() -> list:
    """
    List all available data files in the data directory.

    Returns
    -------
    list
        List of available data filenames
    """
    data_dir = get_data_path()

    if not data_dir.exists():
        return []

    # List all CSV and Excel files
    csv_files = list(data_dir.glob('*.csv'))
    excel_files = list(data_dir.glob('*.xlsx')) + list(data_dir.glob('*.xls'))

    all_files = csv_files + excel_files

    return [f.name for f in sorted(all_files)]
