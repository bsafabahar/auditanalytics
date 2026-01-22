"""Setup configuration for auditanalytics package."""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="auditanalytics",
    version="0.1.0",
    author="J. Christopher Westland",
    author_email="westland@uic.edu",
    description="Data Science for the Accounting Profession - Python Implementation",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/bsafabahar/auditanalytics",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Financial and Insurance Industry",
        "Intended Audience :: Science/Research",
        "Topic :: Office/Business :: Financial :: Accounting",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
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
        "jupyter>=1.0.0",
        "notebook>=6.4.0",
        "requests>=2.26.0",
        "beautifulsoup4>=4.10.0",
        "lxml>=4.6.0",
    ],
    extras_require={
        "dev": [
            "pytest>=7.0.0",
            "pytest-cov>=3.0.0",
            "black>=22.0.0",
            "flake8>=4.0.0",
        ],
    },
    package_data={
        "auditanalytics": ["data/*.csv"],
    },
    include_package_data=True,
)
