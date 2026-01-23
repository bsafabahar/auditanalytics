"""
Example usage of the auditanalytics package

This script demonstrates the main features of the auditanalytics Python package.
"""

import auditanalytics as aa
import pandas as pd
import numpy as np

def main():
    print("=" * 70)
    print("AUDIT ANALYTICS PACKAGE - DEMONSTRATION")
    print("=" * 70)
    
    # 1. Package Information
    print(f"\nPackage Version: {aa.__version__}")
    print(f"Author: {aa.__author__}")
    
    # 2. List Available Datasets
    print("\n" + "=" * 70)
    print("AVAILABLE DATASETS")
    print("=" * 70)
    datasets = aa.list_datasets()
    print(f"Total datasets: {len(datasets)}")
    print("\nFirst 10 datasets:")
    for ds in sorted(datasets)[:10]:
        print(f"  - {ds}")
    
    # 3. Load and Analyze a Dataset
    print("\n" + "=" * 70)
    print("DATASET ANALYSIS - Enrollment Data")
    print("=" * 70)
    enrollment = aa.load_dataset('ch1_enrollment')
    print(enrollment)
    print("\nSummary Statistics:")
    print(enrollment.describe())
    
    # 4. Demonstrate Audit Utility Functions
    print("\n" + "=" * 70)
    print("AUDIT SAMPLING CALCULATIONS")
    print("=" * 70)
    
    # Discovery Sampling
    print("\n1. Discovery Sample Size:")
    print("   - Confidence: 95%")
    print("   - Intolerable Error Rate: 5%")
    n_discovery = aa.discovery_sample_size(0.95, 0.05)
    print(f"   - Required Sample Size: {n_discovery}")
    
    # Attribute Sampling
    print("\n2. Attribute Sample Size:")
    print("   - Population: 1000 transactions")
    print("   - Detectable Error: 5%")
    print("   - Expected Variability: 30%")
    n_attribute = aa.attribute_sample_size(1000, 0.05, 0.3)
    print(f"   - Required Sample Size: {n_attribute}")
    
    # Monetary Unit Sampling
    print("\n3. Monetary Unit Sampling (MUS):")
    print("   - Population Value: $1,000,000")
    print("   - Tolerable Error: $50,000")
    print("   - Confidence: 95%")
    n_mus = aa.monetary_unit_sample_size(1000000, 50000, 0.95)
    print(f"   - Required Sample Size: {n_mus}")
    
    # Stratified Sampling
    print("\n4. Stratified Sample Allocation:")
    print("   - Strata sizes: [100, 200, 300]")
    print("   - Strata variances: [10, 20, 30]")
    print("   - Total sample size: 60")
    allocation = aa.stratified_sample_allocation([100, 200, 300], [10, 20, 30], 60)
    print(f"   - Allocation: {allocation.tolist()}")
    
    # Benford's Law Analysis
    print("\n5. Benford's Law Analysis:")
    print("   - Generating sample financial data...")
    # Generate realistic financial data using exponential distribution
    np.random.seed(42)
    financial_data = np.random.exponential(1000, 500)
    results = aa.benford_analysis(financial_data)
    print(f"   - Chi-square statistic: {results.attrs['chi2_statistic']:.4f}")
    print(f"   - P-value: {results.attrs['p_value']:.4f}")
    if results.attrs['p_value'] > 0.05:
        print("   - Result: Data conforms to Benford's Law ✓")
    else:
        print("   - Result: Data does NOT conform to Benford's Law (potential red flag)")
    
    # 5. Load and Analyze Financial Data
    print("\n" + "=" * 70)
    print("FINANCIAL DATA ANALYSIS")
    print("=" * 70)
    try:
        bank_data = aa.load_dataset('ch_2_bank_fin')
        print("\nBank Financial Data:")
        print(f"Shape: {bank_data.shape}")
        print(f"\nColumns: {bank_data.columns.tolist()}")
        print(f"\nFirst few rows:")
        print(bank_data.head())
    except Exception as e:
        print(f"Note: {e}")
    
    print("\n" + "=" * 70)
    print("DEMONSTRATION COMPLETE")
    print("=" * 70)
    print("\nFor more examples, see the Jupyter notebooks in:")
    print("  auditanalytics/notebooks/")
    print("\nDocumentation: https://github.com/bsafabahar/auditanalytics")
    print("=" * 70)

if __name__ == "__main__":
    main()
