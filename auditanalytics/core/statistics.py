"""
Statistical functions for audit data analysis.

This module provides functions for computing summary statistics,
footing (totaling), and agreeing data in audit procedures.
"""

import pandas as pd
import numpy as np
from typing import Union, Dict, Any, Optional
from scipy import stats


def foot_and_agree(data: Union[pd.DataFrame, pd.Series],
                   column: Optional[str] = None,
                   expected_total: Optional[float] = None) -> Dict[str, Any]:
    """
    Foot (sum) a dataset and optionally agree it to client's records.

    In auditing, 'footing' means summing a column of numbers, and 'agreeing'
    means comparing that sum to the client's reported total.

    Parameters
    ----------
    data : pd.DataFrame or pd.Series
        Data to foot
    column : str, optional
        Column name to sum if data is DataFrame
    expected_total : float, optional
        Client's reported total for agreement

    Returns
    -------
    dict
        Dictionary containing:
        - 'total': computed total
        - 'agrees': True if total matches expected (if provided)
        - 'difference': difference from expected (if provided)

    Examples
    --------
    >>> df = pd.DataFrame({'amount': [100, 200, 300]})
    >>> foot_and_agree(df, 'amount', 600)
    {'total': 600, 'agrees': True, 'difference': 0}
    """
    # Extract the data to sum
    if isinstance(data, pd.DataFrame):
        if column is None:
            raise ValueError("Column name required when data is DataFrame")
        values = data[column]
    else:
        values = data

    # Compute the total
    total = float(values.sum())

    result = {'total': total}

    # Check agreement if expected total provided
    if expected_total is not None:
        difference = total - expected_total
        agrees = bool(np.abs(difference) < 1e-10)  # Account for floating point precision
        result['agrees'] = agrees
        result['difference'] = difference

    return result


def compute_summary_stats(data: pd.DataFrame,
                         group_by: Optional[str] = None,
                         describe_type: str = 'pandas') -> Union[pd.DataFrame, Dict]:
    """
    Compute comprehensive summary statistics for audit data.

    Parameters
    ----------
    data : pd.DataFrame
        Input data
    group_by : str, optional
        Column name to group by for group-wise statistics
    describe_type : str, optional
        Type of description: 'pandas', 'extended', or 'all'
        (default: 'pandas')

    Returns
    -------
    pd.DataFrame or dict
        Summary statistics

    Examples
    --------
    >>> df = pd.DataFrame({'amount': [100, 200, 300], 'type': ['A', 'B', 'A']})
    >>> compute_summary_stats(df)
    """
    if group_by is not None:
        # Group-wise statistics
        return data.groupby(group_by).describe()

    if describe_type == 'pandas':
        return data.describe()

    elif describe_type == 'extended':
        # More detailed statistics
        stats_dict = {}
        for col in data.select_dtypes(include=[np.number]).columns:
            col_data = data[col].dropna()
            stats_dict[col] = {
                'count': len(col_data),
                'mean': col_data.mean(),
                'std': col_data.std(),
                'min': col_data.min(),
                'q25': col_data.quantile(0.25),
                'median': col_data.median(),
                'q75': col_data.quantile(0.75),
                'max': col_data.max(),
                'skewness': col_data.skew(),
                'kurtosis': col_data.kurtosis(),
                'sum': col_data.sum(),
            }
        return pd.DataFrame(stats_dict)

    elif describe_type == 'all':
        # Comprehensive statistics similar to R's Hmisc::describe
        result = {}
        for col in data.columns:
            col_data = data[col]
            col_stats = {
                'n': len(col_data),
                'missing': col_data.isna().sum(),
                'unique': col_data.nunique(),
            }

            if pd.api.types.is_numeric_dtype(col_data):
                col_data_clean = col_data.dropna()
                col_stats.update({
                    'mean': col_data_clean.mean(),
                    'std': col_data_clean.std(),
                    'min': col_data_clean.min(),
                    'q05': col_data_clean.quantile(0.05),
                    'q25': col_data_clean.quantile(0.25),
                    'median': col_data_clean.median(),
                    'q75': col_data_clean.quantile(0.75),
                    'q95': col_data_clean.quantile(0.95),
                    'max': col_data_clean.max(),
                })

            result[col] = col_stats

        return pd.DataFrame(result).T

    else:
        raise ValueError(f"Unknown describe_type: {describe_type}")


def test_normality(data: Union[pd.Series, np.ndarray],
                   method: str = 'shapiro') -> Dict[str, Any]:
    """
    Test data for normality.

    Parameters
    ----------
    data : pd.Series or np.ndarray
        Data to test
    method : str, optional
        Test method: 'shapiro', 'ks', or 'anderson' (default: 'shapiro')

    Returns
    -------
    dict
        Test results including statistic and p-value
    """
    if isinstance(data, pd.Series):
        data = data.dropna().values

    if method == 'shapiro':
        stat, p_value = stats.shapiro(data)
        return {
            'method': 'Shapiro-Wilk',
            'statistic': stat,
            'p_value': p_value,
            'is_normal': bool(p_value > 0.05)
        }

    elif method == 'ks':
        stat, p_value = stats.kstest(data, 'norm')
        return {
            'method': 'Kolmogorov-Smirnov',
            'statistic': stat,
            'p_value': p_value,
            'is_normal': bool(p_value > 0.05)
        }

    elif method == 'anderson':
        result = stats.anderson(data)
        return {
            'method': 'Anderson-Darling',
            'statistic': result.statistic,
            'critical_values': result.critical_values,
            'significance_levels': result.significance_level
        }

    else:
        raise ValueError(f"Unknown method: {method}")


def detect_outliers(data: Union[pd.Series, np.ndarray],
                   method: str = 'iqr',
                   threshold: float = 1.5) -> Dict[str, Any]:
    """
    Detect outliers in data.

    Parameters
    ----------
    data : pd.Series or np.ndarray
        Data to analyze
    method : str, optional
        Detection method: 'iqr', 'zscore', or 'modified_zscore'
        (default: 'iqr')
    threshold : float, optional
        Threshold for outlier detection (default: 1.5 for IQR)

    Returns
    -------
    dict
        Outlier information including indices and values
    """
    if isinstance(data, pd.Series):
        values = data.dropna().values
        index = data.dropna().index
    else:
        values = data[~np.isnan(data)]
        index = np.arange(len(values))

    if method == 'iqr':
        q1 = np.percentile(values, 25)
        q3 = np.percentile(values, 75)
        iqr = q3 - q1
        lower_bound = q1 - threshold * iqr
        upper_bound = q3 + threshold * iqr
        outliers_mask = (values < lower_bound) | (values > upper_bound)

    elif method == 'zscore':
        z_scores = np.abs(stats.zscore(values))
        outliers_mask = z_scores > threshold

    elif method == 'modified_zscore':
        median = np.median(values)
        mad = np.median(np.abs(values - median))
        modified_z_scores = 0.6745 * (values - median) / mad
        outliers_mask = np.abs(modified_z_scores) > threshold

    else:
        raise ValueError(f"Unknown method: {method}")

    return {
        'method': method,
        'n_outliers': outliers_mask.sum(),
        'outlier_indices': index[outliers_mask].tolist(),
        'outlier_values': values[outliers_mask].tolist(),
        'outlier_mask': outliers_mask
    }
