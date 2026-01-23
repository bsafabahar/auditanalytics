"""
Tests for core statistics functions.
"""

import pytest
import pandas as pd
import numpy as np
from auditanalytics.core.statistics import (
    foot_and_agree,
    compute_summary_stats,
    test_normality,
    detect_outliers
)


class TestFootAndAgree:
    """Test footing and agreeing functions."""
    
    def test_basic_footing_series(self):
        """Test basic footing with pandas Series."""
        data = pd.Series([100, 200, 300])
        result = foot_and_agree(data)
        
        assert result['total'] == 600
        assert 'agrees' not in result
    
    def test_footing_dataframe(self):
        """Test footing with DataFrame."""
        df = pd.DataFrame({'amount': [100, 200, 300]})
        result = foot_and_agree(df, 'amount')
        
        assert result['total'] == 600
    
    def test_agreeing_match(self):
        """Test agreeing when totals match."""
        data = pd.Series([100, 200, 300])
        result = foot_and_agree(data, expected_total=600)
        
        assert result['total'] == 600
        assert result['agrees'] is True
        assert result['difference'] == 0
    
    def test_agreeing_mismatch(self):
        """Test agreeing when totals don't match."""
        data = pd.Series([100, 200, 300])
        result = foot_and_agree(data, expected_total=650)
        
        assert result['total'] == 600
        assert result['agrees'] is False
        assert result['difference'] == -50
    
    def test_missing_column_raises(self):
        """Test that missing column raises error."""
        df = pd.DataFrame({'amount': [100, 200, 300]})
        
        with pytest.raises(ValueError):
            foot_and_agree(df)  # No column specified


class TestComputeSummaryStats:
    """Test summary statistics computation."""
    
    @pytest.fixture
    def sample_data(self):
        """Create sample data for testing."""
        return pd.DataFrame({
            'amount': [100, 200, 300, 400, 500],
            'category': ['A', 'B', 'A', 'B', 'A']
        })
    
    def test_basic_summary(self, sample_data):
        """Test basic summary statistics."""
        result = compute_summary_stats(sample_data, describe_type='pandas')
        
        assert isinstance(result, pd.DataFrame)
        assert 'amount' in result.columns
        assert 'count' in result.index
        assert 'mean' in result.index
    
    def test_extended_summary(self, sample_data):
        """Test extended summary statistics."""
        result = compute_summary_stats(sample_data, describe_type='extended')
        
        assert isinstance(result, pd.DataFrame)
        assert 'amount' in result.columns
        assert 'skewness' in result.index
        assert 'kurtosis' in result.index
    
    def test_grouped_summary(self, sample_data):
        """Test grouped summary statistics."""
        result = compute_summary_stats(sample_data, group_by='category')
        
        assert isinstance(result, pd.DataFrame)
        assert len(result) == 2  # Two groups


class TestNormalityTests:
    """Test normality testing functions."""
    
    def test_normal_data(self):
        """Test with normal data."""
        # Generate normal data
        np.random.seed(42)
        data = np.random.normal(0, 1, 1000)
        
        result = test_normality(data, method='shapiro')
        
        assert 'statistic' in result
        assert 'p_value' in result
        assert 'is_normal' in result
        assert isinstance(result['is_normal'], bool)
    
    def test_non_normal_data(self):
        """Test with non-normal data."""
        # Generate exponential (non-normal) data
        np.random.seed(42)
        data = np.random.exponential(1, 1000)
        
        result = test_normality(data, method='shapiro')
        
        # Exponential should not be normal
        assert result['is_normal'] is False
    
    def test_ks_test(self):
        """Test Kolmogorov-Smirnov test."""
        np.random.seed(42)
        data = np.random.normal(0, 1, 100)
        
        result = test_normality(data, method='ks')
        
        assert result['method'] == 'Kolmogorov-Smirnov'
        assert 'p_value' in result


class TestOutlierDetection:
    """Test outlier detection functions."""
    
    def test_iqr_method(self):
        """Test IQR outlier detection."""
        # Data with obvious outliers
        data = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 100])
        
        result = detect_outliers(data, method='iqr', threshold=1.5)
        
        assert result['n_outliers'] > 0
        assert 100 in result['outlier_values']
    
    def test_zscore_method(self):
        """Test Z-score outlier detection."""
        # Data with outliers
        np.random.seed(42)
        data = np.random.normal(0, 1, 100)
        data = np.append(data, [10, -10])  # Add outliers
        
        result = detect_outliers(data, method='zscore', threshold=3)
        
        assert result['n_outliers'] >= 2
    
    def test_no_outliers(self):
        """Test when there are no outliers."""
        # Normal data without extreme values
        np.random.seed(42)
        data = np.random.normal(0, 1, 100)
        
        result = detect_outliers(data, method='iqr', threshold=3)
        
        # Should have few or no outliers with high threshold
        assert result['n_outliers'] < 5


if __name__ == '__main__':
    pytest.main([__file__, '-v'])
