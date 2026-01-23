"""
Tests for data loading functions.
"""

import pytest
import pandas as pd
import numpy as np
from pathlib import Path
import tempfile
import os

from auditanalytics.data.loaders import (
    load_csv,
    load_data,
    save_data,
    get_data_path,
    list_available_data
)


class TestLoadCSV:
    """Test CSV loading functions."""
    
    def test_load_csv_basic(self, tmp_path):
        """Test basic CSV loading."""
        # Create a temporary CSV file
        test_file = tmp_path / "test.csv"
        df = pd.DataFrame({'a': [1, 2, 3], 'b': [4, 5, 6]})
        df.to_csv(test_file, index=False)
        
        # Load it back
        loaded_df = load_csv(test_file)
        
        assert isinstance(loaded_df, pd.DataFrame)
        assert len(loaded_df) == 3
        assert list(loaded_df.columns) == ['a', 'b']
    
    def test_load_csv_not_found(self):
        """Test loading non-existent file."""
        with pytest.raises(FileNotFoundError):
            load_csv('/nonexistent/file.csv')
    
    def test_load_csv_with_kwargs(self, tmp_path):
        """Test CSV loading with additional kwargs."""
        # Create CSV with dates
        test_file = tmp_path / "test.csv"
        df = pd.DataFrame({
            'date': ['2020-01-01', '2020-01-02'],
            'value': [100, 200]
        })
        df.to_csv(test_file, index=False)
        
        # Load with date parsing
        loaded_df = load_csv(test_file, parse_dates=['date'])
        
        assert pd.api.types.is_datetime64_any_dtype(loaded_df['date'])


class TestSaveData:
    """Test data saving functions."""
    
    def test_save_data(self, tmp_path):
        """Test saving data to CSV."""
        df = pd.DataFrame({'a': [1, 2, 3], 'b': [4, 5, 6]})
        
        save_data(df, 'test.csv', data_dir=tmp_path)
        
        # Check file exists
        saved_file = tmp_path / 'test.csv'
        assert saved_file.exists()
        
        # Load and verify
        loaded_df = pd.read_csv(saved_file)
        pd.testing.assert_frame_equal(df, loaded_df)
    
    def test_save_creates_directory(self, tmp_path):
        """Test that save_data creates directory if needed."""
        df = pd.DataFrame({'a': [1, 2, 3]})
        new_dir = tmp_path / 'new_directory'
        
        save_data(df, 'test.csv', data_dir=new_dir)
        
        assert new_dir.exists()
        assert (new_dir / 'test.csv').exists()


class TestDataPath:
    """Test data path utilities."""
    
    def test_get_data_path(self):
        """Test getting data path."""
        path = get_data_path()
        
        assert isinstance(path, Path)
    
    def test_list_available_data(self):
        """Test listing available data files."""
        files = list_available_data()
        
        assert isinstance(files, list)
        # May or may not have files depending on environment


class TestLoadData:
    """Test the convenience load_data function."""
    
    def test_load_data_with_dir(self, tmp_path):
        """Test load_data with explicit directory."""
        # Create test file
        test_file = tmp_path / "test.csv"
        df = pd.DataFrame({'a': [1, 2, 3]})
        df.to_csv(test_file, index=False)
        
        # Load using load_data
        loaded_df = load_data('test.csv', data_dir=tmp_path)
        
        assert isinstance(loaded_df, pd.DataFrame)
        assert len(loaded_df) == 3
    
    def test_load_data_not_found(self):
        """Test load_data with non-existent file."""
        with pytest.raises(FileNotFoundError):
            load_data('nonexistent_file_12345.csv', data_dir='/tmp')


class TestIntegration:
    """Integration tests for data loading."""
    
    def test_save_and_load_roundtrip(self, tmp_path):
        """Test saving and loading data."""
        # Create original data
        original_df = pd.DataFrame({
            'id': [1, 2, 3, 4, 5],
            'amount': [100.5, 200.75, 300.25, 400.0, 500.5],
            'category': ['A', 'B', 'A', 'C', 'B']
        })
        
        # Save
        save_data(original_df, 'roundtrip.csv', data_dir=tmp_path)
        
        # Load
        loaded_df = load_data('roundtrip.csv', data_dir=tmp_path)
        
        # Verify
        pd.testing.assert_frame_equal(original_df, loaded_df)


if __name__ == '__main__':
    pytest.main([__file__, '-v'])
