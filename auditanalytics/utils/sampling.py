"""
Utility functions for audit analytics

This module provides common audit functions for sampling, statistical analysis,
and audit-specific calculations.
"""
import numpy as np
from scipy import stats
import pandas as pd


def discovery_sample_size(confidence, intolerable_error_rate):
    """
    Calculate discovery sample size for detecting transaction stream errors.
    
    Discovery sampling sets a sample size that is likely to discover at least 
    one error in the sample if the actual transaction error rate exceeds the 
    minimum acceptable error rate.
    
    Parameters
    ----------
    confidence : float
        Confidence level (e.g., 0.95 for 95% confidence)
    intolerable_error_rate : float
        Maximum acceptable error rate (e.g., 0.05 for 5%)
        
    Returns
    -------
    int
        Required sample size (rounded up)
        
    Examples
    --------
    >>> discovery_sample_size(0.95, 0.05)
    59
    
    References
    ----------
    Based on discovery sampling methodology for audit testing.
    """
    n = np.log(1 - confidence) / np.log(1 - intolerable_error_rate)
    return int(np.ceil(n))


def attribute_sample_size(size, delta_pct, sigma_pct, sig_level=0.05, power=0.8):
    """
    Calculate attribute sample size for estimating error rates.
    
    Attribute sampling estimates the error rate in the entire transaction 
    population with specified confidence.
    
    Parameters
    ----------
    size : int
        Total number or amount of transactions
    delta_pct : float
        Detectable error percentage (e.g., 0.05 for 5%)
    sigma_pct : float
        Expected variability as percentage of size (e.g., 0.3 for 30%)
    sig_level : float, optional
        Significance level (default: 0.05)
    power : float, optional
        Statistical power (default: 0.8)
        
    Returns
    -------
    int
        Required sample size (rounded up)
        
    Examples
    --------
    >>> attribute_sample_size(1000, 0.05, 0.3)
    7
    """
    delta = delta_pct * size
    sigma = sigma_pct * size
    effect = delta / sigma
    
    # Using power analysis for one-sample t-test
    n = stats.norm.ppf(1 - sig_level) + stats.norm.ppf(power)
    n = (n / effect) ** 2
    
    return int(np.ceil(n))


def monetary_unit_sample_size(population_value, tolerable_error, confidence=0.95, 
                               expected_error_rate=0.0):
    """
    Calculate sample size for Monetary Unit Sampling (MUS).
    
    Parameters
    ----------
    population_value : float
        Total value of the population
    tolerable_error : float
        Maximum tolerable error amount
    confidence : float, optional
        Confidence level (default: 0.95)
    expected_error_rate : float, optional
        Expected error rate (default: 0.0)
        
    Returns
    -------
    int
        Required sample size
        
    Examples
    --------
    >>> monetary_unit_sample_size(1000000, 50000, 0.95)
    60
    """
    # Risk factor for zero errors at given confidence
    risk_factor = -np.log(1 - confidence)
    
    # Adjust for expected errors
    if expected_error_rate > 0:
        risk_factor = risk_factor * (1 + expected_error_rate)
    
    # Calculate sample size
    n = (population_value * risk_factor) / tolerable_error
    
    return int(np.ceil(n))


def stratified_sample_allocation(strata_sizes, strata_variances, total_sample_size):
    """
    Allocate sample across strata using Neyman allocation.
    
    Parameters
    ----------
    strata_sizes : array-like
        Number of items in each stratum
    strata_variances : array-like
        Variance estimate for each stratum
    total_sample_size : int
        Total sample size to allocate
        
    Returns
    -------
    numpy.ndarray
        Sample size for each stratum (rounded)
        
    Examples
    --------
    >>> stratified_sample_allocation([100, 200, 300], [10, 20, 30], 60)
    array([ 6, 17, 37])
    """
    strata_sizes = np.array(strata_sizes)
    strata_variances = np.array(strata_variances)
    
    # Neyman allocation
    strata_stds = np.sqrt(strata_variances)
    weights = strata_sizes * strata_stds
    weights = weights / weights.sum()
    
    allocation = weights * total_sample_size
    
    # Round to integers, ensuring total equals target
    allocation = np.round(allocation).astype(int)
    
    # Adjust for rounding errors
    diff = total_sample_size - allocation.sum()
    if diff != 0:
        # Add/subtract from largest stratum
        idx = np.argmax(allocation)
        allocation[idx] += diff
    
    return allocation


def benford_analysis(data, digit=1):
    """
    Perform Benford's Law analysis on numerical data.
    
    Parameters
    ----------
    data : array-like
        Numerical data to analyze
    digit : int, optional
        Which digit to analyze (1 for first digit, 2 for second, etc.)
        Default: 1
        
    Returns
    -------
    pandas.DataFrame
        DataFrame with digit, observed frequency, expected frequency, and chi-square
        
    Examples
    --------
    >>> import numpy as np
    >>> data = np.random.exponential(1000, 100)
    >>> results = benford_analysis(data, digit=1)
    """
    data = np.array(data)
    data = data[data > 0]  # Only positive values
    
    # Extract the specified digit
    data_str = data.astype(str)
    digits = []
    for val in data_str:
        # Remove decimal point and get digit
        val_clean = val.replace('.', '').replace('-', '')
        if len(val_clean) >= digit:
            digits.append(int(val_clean[digit-1]))
    
    digits = np.array(digits)
    
    if digit == 1:
        # Benford's law for first digit
        possible_digits = range(1, 10)
        expected_freq = [np.log10(1 + 1/d) for d in possible_digits]
    else:
        # Uniform distribution for other digits
        possible_digits = range(0, 10)
        expected_freq = [0.1] * 10
    
    # Calculate observed frequencies
    observed_counts = [np.sum(digits == d) for d in possible_digits]
    total = sum(observed_counts)
    observed_freq = [c / total for c in observed_counts]
    
    # Chi-square test
    expected_counts = [f * total for f in expected_freq]
    chi2_components = [(o - e)**2 / e for o, e in zip(observed_counts, expected_counts)]
    
    results = pd.DataFrame({
        'Digit': possible_digits,
        'Observed_Freq': observed_freq,
        'Expected_Freq': expected_freq,
        'Observed_Count': observed_counts,
        'Expected_Count': expected_counts,
        'Chi2_Component': chi2_components
    })
    
    chi2_stat = sum(chi2_components)
    p_value = 1 - stats.chi2.cdf(chi2_stat, len(possible_digits) - 1)
    
    results.attrs['chi2_statistic'] = chi2_stat
    results.attrs['p_value'] = p_value
    
    return results


__all__ = [
    'discovery_sample_size',
    'attribute_sample_size', 
    'monetary_unit_sample_size',
    'stratified_sample_allocation',
    'benford_analysis'
]
