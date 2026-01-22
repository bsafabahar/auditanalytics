from setuptools import setup, find_packages
from pathlib import Path

# Read the README file
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text(encoding='utf-8')

setup(
    name="auditanalytics",
    version="0.1.0",
    author="J. Christopher Westland",
    author_email="westland@uic.edu",
    description="Audit Analytics: Data Science for the Accounting Profession - Python Edition",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/bsafabahar/auditanalytics",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Financial and Insurance Industry",
        "Intended Audience :: Science/Research",
        "Topic :: Office/Business :: Financial :: Accounting",
        "Topic :: Scientific/Engineering :: Information Analysis",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
    install_requires=[
        "pandas>=1.3.0",
        "numpy>=1.21.0",
        "matplotlib>=3.4.0",
        "seaborn>=0.11.0",
        "scipy>=1.7.0",
        "statsmodels>=0.13.0",
        "scikit-learn>=1.0.0",
        "plotly>=5.0.0",
        "jupyter>=1.0.0",
        "openpyxl>=3.0.0",
        "python-dateutil>=2.8.0",
    ],
    extras_require={
        "dev": [
            "pytest>=7.0.0",
            "pytest-cov>=3.0.0",
            "flake8>=4.0.0",
            "black>=22.0.0",
            "mypy>=0.950",
            "ipython>=7.26.0",
        ],
        "docs": [
            "sphinx>=4.0.0",
            "sphinx-rtd-theme>=1.0.0",
            "nbsphinx>=0.8.0",
        ],
        "ml": [
            "tensorflow>=2.8.0",
            "torch>=1.11.0",
            "xgboost>=1.5.0",
        ],
        "web": [
            "requests>=2.26.0",
            "beautifulsoup4>=4.9.0",
            "selenium>=4.0.0",
        ],
    },
    include_package_data=True,
    package_data={
        "auditanalytics": ["data/*.csv", "data/*.xlsx"],
    },
    entry_points={
        "console_scripts": [
            "auditanalytics=auditanalytics.cli:main",
        ],
    },
)
