"""
Statistical sampling functions for audit analytics.

This module implements discovery sampling, attribute sampling,
and acceptance sampling methods used in audit procedures.
"""

import numpy as np
from typing import Dict, Optional


def discovery_sample_size(confidence: float = 0.95,
                         intolerable_rate: float = 0.05) -> int:
    """
    Calculate discovery sample size for detecting out-of-control transaction streams.

    Discovery sampling sets a sample size that is likely to discover at least one error
    in the sample if the actual transaction error rate exceeds the minimum acceptable
    error-rate (out-of-control rate).

    Parameters
    ----------
    confidence : float, optional
        Confidence level (default: 0.95 for 95% confidence)
    intolerable_rate : float, optional
        Intolerable error rate threshold (default: 0.05 for 5%)

    Returns
    -------
    int
        Required sample size

    Examples
    --------
    >>> discovery_sample_size(0.95, 0.05)
    59

    Notes
    -----
    Formula: n = log(1 - confidence) / log(1 - intolerable_rate)

    Raises
    ------
    ValueError
        If intolerable_rate is 0 or 1, or if confidence is not in (0, 1)
    """
    if intolerable_rate <= 0 or intolerable_rate >= 1:
        raise ValueError("intolerable_rate must be between 0 and 1 (exclusive)")
    if confidence <= 0 or confidence >= 1:
        raise ValueError("confidence must be between 0 and 1 (exclusive)")

    n = np.log(1 - confidence) / np.log(1 - intolerable_rate)
    return int(np.ceil(n))


def attribute_sample_size(size: int,
                         delta_rate: float = 0.05,
                         sigma_rate: Optional[float] = None,
                         sig_level: float = 0.05,
                         power: float = 0.8,
                         alternative: str = "greater") -> Dict[str, int]:
    """
    Calculate attribute sample size for estimating transaction error rates.

    Uses Cohen's power analysis to determine sample size for detecting
    occurrence of errors in a population.

    Parameters
    ----------
    size : int
        Number of transactions in population
    delta_rate : float, optional
        Detectable error rate (default: 0.05 for 5%)
    sigma_rate : float, optional
        Variability estimate (default: ~1/3 of size)
    sig_level : float, optional
        Significance level (default: 0.05)
    power : float, optional
        Statistical power (default: 0.8)
    alternative : str, optional
        Alternative hypothesis: 'greater', 'less', or 'two-sided' (default: 'greater')

    Returns
    -------
    dict
        Dictionary with 'occurrence' and 'amount' sample sizes

    Examples
    --------
    >>> attribute_sample_size(1000, 0.05, 0.3*1000)
    {'occurrence': 11}
    """
    # Default sigma if not provided
    if sigma_rate is None:
        sigma_rate = 0.3 * size

    delta = delta_rate * size
    effect_size = delta / sigma_rate

    # Calculate degrees of freedom for t-test
    # Using approximation for one-sample t-test
    from scipy.stats import t as t_dist

    # Iterate to find sample size
    n = 10
    while n < 10000:
        df = n - 1
        t_alpha = t_dist.ppf(1 - sig_level, df) if alternative == 'greater' else \
                  t_dist.ppf(sig_level, df) if alternative == 'less' else \
                  t_dist.ppf(1 - sig_level/2, df)

        ncp = effect_size * np.sqrt(n)  # Non-centrality parameter

        # Calculate power
        if alternative == 'greater':
            calc_power = 1 - t_dist.cdf(t_alpha, df, ncp)
        elif alternative == 'less':
            calc_power = t_dist.cdf(t_alpha, df, ncp)
        else:
            calc_power = 1 - t_dist.cdf(t_alpha, df, ncp) + t_dist.cdf(-t_alpha, df, ncp)

        if calc_power >= power:
            break
        n += 1

    return {'occurrence': int(np.ceil(n))}


def attribute_sample_size_amount(total_amount: float,
                                 mean_transaction: float,
                                 delta_rate: float = 0.05,
                                 sigma: float = 30,
                                 sig_level: float = 0.05,
                                 power: float = 0.8,
                                 alternative: str = "greater") -> int:
    """
    Calculate attribute sample size for estimating monetary error amounts.

    Parameters
    ----------
    total_amount : float
        Total amount of transactions
    mean_transaction : float
        Average value of a transaction
    delta_rate : float, optional
        Detectable error rate (default: 0.05 for 5%)
    sigma : float, optional
        Transaction amount variability (default: 30)
    sig_level : float, optional
        Significance level (default: 0.05)
    power : float, optional
        Statistical power (default: 0.8)
    alternative : str, optional
        Alternative hypothesis (default: 'greater')

    Returns
    -------
    int
        Required sample size for amount testing

    Examples
    --------
    >>> attribute_sample_size_amount(100000, 50, 0.05, 30)
    1052
    """
    delta = delta_rate * mean_transaction
    effect_size = delta / sigma

    # Similar calculation as above
    from scipy.stats import t as t_dist

    n = 10
    while n < 10000:
        df = n - 1
        t_alpha = t_dist.ppf(1 - sig_level, df) if alternative == 'greater' else \
                  t_dist.ppf(sig_level, df) if alternative == 'less' else \
                  t_dist.ppf(1 - sig_level/2, df)

        ncp = effect_size * np.sqrt(n)

        if alternative == 'greater':
            calc_power = 1 - t_dist.cdf(t_alpha, df, ncp)
        elif alternative == 'less':
            calc_power = t_dist.cdf(t_alpha, df, ncp)
        else:
            calc_power = 1 - t_dist.cdf(t_alpha, df, ncp) + t_dist.cdf(-t_alpha, df, ncp)

        if calc_power >= power:
            break
        n += 1

    return int(np.ceil(n))


def acceptance_sample_size(account_balance: float,
                          mean_transaction: float,
                          delta_rate: float = 0.05,
                          sigma: float = 30,
                          sig_level: float = 0.05,
                          power: float = 0.8,
                          alternative: str = "greater") -> int:
    """
    Calculate acceptance sample size for substantive testing.

    Determines sample size to test whether account balance is
    'fairly stated' (does not contain material error).

    Parameters
    ----------
    account_balance : float
        Total account balance
    mean_transaction : float
        Average transaction value
    delta_rate : float, optional
        Materiality threshold rate (default: 0.05)
    sigma : float, optional
        Transaction variability (default: 30)
    sig_level : float, optional
        Significance level (default: 0.05)
    power : float, optional
        Statistical power (default: 0.8)
    alternative : str, optional
        Alternative hypothesis (default: 'greater')

    Returns
    -------
    int
        Required acceptance sample size

    Examples
    --------
    >>> acceptance_sample_size(100000, 50, 0.05, 30)
    1052

    Notes
    -----
    This uses the same calculation as attribute sampling for amounts,
    as both estimate monetary error with confidence intervals.
    """
    return attribute_sample_size_amount(
        account_balance,
        mean_transaction,
        delta_rate,
        sigma,
        sig_level,
        power,
        alternative
    )
