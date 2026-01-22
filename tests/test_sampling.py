"""
Tests for core sampling functions.
"""

import pytest
import numpy as np
from auditanalytics.core.sampling import (
    discovery_sample_size,
    attribute_sample_size,
    attribute_sample_size_amount,
    acceptance_sample_size
)


class TestDiscoverySampling:
    """Test discovery sampling calculations."""
    
    def test_basic_discovery_sample(self):
        """Test basic discovery sample size calculation."""
        n = discovery_sample_size(confidence=0.95, intolerable_rate=0.05)
        assert isinstance(n, int)
        assert n > 0
        assert n == 59  # Expected value for these parameters
    
    def test_higher_confidence(self):
        """Test that higher confidence requires larger sample."""
        n1 = discovery_sample_size(confidence=0.90, intolerable_rate=0.05)
        n2 = discovery_sample_size(confidence=0.95, intolerable_rate=0.05)
        n3 = discovery_sample_size(confidence=0.99, intolerable_rate=0.05)
        
        assert n1 < n2 < n3
    
    def test_lower_intolerable_rate(self):
        """Test that lower intolerable rate requires larger sample."""
        n1 = discovery_sample_size(confidence=0.95, intolerable_rate=0.10)
        n2 = discovery_sample_size(confidence=0.95, intolerable_rate=0.05)
        n3 = discovery_sample_size(confidence=0.95, intolerable_rate=0.01)
        
        assert n1 < n2 < n3


class TestAttributeSampling:
    """Test attribute sampling calculations."""
    
    def test_basic_attribute_sample(self):
        """Test basic attribute sample size calculation."""
        result = attribute_sample_size(
            size=1000,
            delta_rate=0.05,
            sigma_rate=300
        )
        
        assert isinstance(result, dict)
        assert 'occurrence' in result
        assert isinstance(result['occurrence'], int)
        assert result['occurrence'] > 0
    
    def test_attribute_sample_amount(self):
        """Test attribute sample size for monetary amounts."""
        n = attribute_sample_size_amount(
            total_amount=100000,
            mean_transaction=50,
            delta_rate=0.05,
            sigma=30
        )
        
        assert isinstance(n, int)
        assert n > 0
        assert n > 100  # Should be reasonably large


class TestAcceptanceSampling:
    """Test acceptance sampling calculations."""
    
    def test_basic_acceptance_sample(self):
        """Test basic acceptance sample size calculation."""
        n = acceptance_sample_size(
            account_balance=100000,
            mean_transaction=50,
            delta_rate=0.05,
            sigma=30
        )
        
        assert isinstance(n, int)
        assert n > 0
    
    def test_acceptance_equals_attribute(self):
        """Test that acceptance sampling equals attribute sampling for amounts."""
        n1 = acceptance_sample_size(
            account_balance=100000,
            mean_transaction=50,
            delta_rate=0.05,
            sigma=30
        )
        
        n2 = attribute_sample_size_amount(
            total_amount=100000,
            mean_transaction=50,
            delta_rate=0.05,
            sigma=30
        )
        
        assert n1 == n2


class TestEdgeCases:
    """Test edge cases and error handling."""
    
    def test_zero_intolerable_rate_raises(self):
        """Test that zero intolerable rate is handled."""
        with pytest.raises(ValueError):
            discovery_sample_size(confidence=0.95, intolerable_rate=0.0)
    
    def test_confidence_boundary(self):
        """Test confidence level boundaries."""
        # Very low confidence
        n1 = discovery_sample_size(confidence=0.70, intolerable_rate=0.05)
        assert n1 > 0
        
        # Very high confidence
        n2 = discovery_sample_size(confidence=0.999, intolerable_rate=0.05)
        assert n2 > n1


if __name__ == '__main__':
    pytest.main([__file__, '-v'])
