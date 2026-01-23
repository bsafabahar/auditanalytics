"""
Basic smoke tests for the auditanalytics package
"""
try:
    import pytest
    HAS_PYTEST = True
except ImportError:
    HAS_PYTEST = False
    
import pandas as pd
import auditanalytics as aa
from auditanalytics.data import load_dataset, list_datasets


def test_version():
    """Test that version is set correctly"""
    assert hasattr(aa, '__version__')
    assert aa.__version__ == "0.1.0"


def test_load_dataset():
    """Test loading a dataset"""
    df = load_dataset('ch1_enrollment')
    assert isinstance(df, pd.DataFrame)
    assert len(df) > 0


def test_list_datasets():
    """Test listing datasets"""
    datasets = list_datasets()
    assert isinstance(datasets, list)
    assert len(datasets) > 0
    assert 'ch1_enrollment' in datasets


def test_dataset_not_found():
    """Test that loading non-existent dataset raises error"""
    if HAS_PYTEST:
        with pytest.raises(FileNotFoundError):
            load_dataset('nonexistent_dataset')
    else:
        try:
            load_dataset('nonexistent_dataset')
            assert False, "Should have raised FileNotFoundError"
        except FileNotFoundError:
            pass  # Expected


if __name__ == '__main__':
    # Run basic tests without pytest
    print("Running smoke tests...")
    
    print("✓ Test version")
    test_version()
    
    print("✓ Test load_dataset")
    test_load_dataset()
    
    print("✓ Test list_datasets")
    test_list_datasets()
    
    print("✓ Test dataset not found")
    test_dataset_not_found()
    
    print("\n✓ All tests passed!")
