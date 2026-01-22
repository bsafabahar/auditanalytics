## Audit Analytics: Data Science for the Accounting Profession (Python Edition)

Python implementation of data science tools to plan, implement, and render an audit opinion that is legally and statistically defensible. Originally based on the R implementation from the book "Audit Analytics" by J. Christopher Westland

![Audit Analytics](https://images-na.ssl-images-amazon.com/images/I/41SRfppKIyL._SX328_BO1,204,203,200_.jpg)

ISSN 2197-5736 ISSN 2197-5744 (electronic) 

ISBN 978-3-030-49090-4 ISBN 978-3-030-49091-1 (eBook) 

https://doi.org/10.1007/978-3-030-49091-1


Information technology plays a pivotal role in financial control and audit: most financial data is now digitally recorded and dispersed among servers, clouds and networks over which the audited firm has no control. Additionally, a firm’s data—particularly in the case of finance, software, insurance and biotech firms— comprises most of the audited value of the firm. Financial audits are critical mechanisms for ensuring the integrity of information systems and the reporting of organizational finances. They help avoid the abuses that led to passage of legislation such as the Foreign Corrupt Practices Act (1977), and the Sarbanes-Oxley Act (2002).

Audit effectiveness has declined over the past two decades as auditor skillsets have failed to keep up with advances in information technology. Information and communication technology lie at the core of commerce today and are integrated in business processes around the world. This book is designed to meet the increasing need of audit professionals to understand information technology and the controls required to manage it. The material included focuses on the requirements for annual Securities and Exchange Commission audits (10-K) for listed corporations. These represent the benchmark auditing procedures for specialized audits, such as internal, governmental, and attestation audits.

Using R and RStudio, the book demonstrates how to render an audit opinion that is legally and statistically defensible; analyze, extract, and manipulate accounting data; build a risk assessment matrix to inform the conduct of a cost-effective audit program; and more.

**This Python package** provides a complete Python implementation of the audit analytics methods from the book. It uses modern Python data science libraries (pandas, numpy, scikit-learn, statsmodels, matplotlib) to perform the same analyses and procedures described in the original book.


### Where to buy?

[Springer](https://www.springer.com/gp/book/9783030490904)

[Amazon](https://www.amazon.com/Audit-Analytics-Science-Accounting-Profession/dp/3030490904/ref=sr_1_5?dchild=1&keywords=westland+audit+analytics&qid=1599767034&sr=8-5)

[Waterstones](https://www.waterstones.com/book/audit-analytics/j-christopher-westland//9783030490904)

## Installation

The _auditanalytics_ Python package contains a collection of data sets used in the book. Jupyter Notebooks which contain the Python code for Audit Analytics are available in the `notebooks/` directory.

To install the package:

```bash
# Clone the repository
git clone https://github.com/bsafabahar/auditanalytics.git
cd auditanalytics

# Create a virtual environment (recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install the package and dependencies
pip install -e .

# Or install from requirements.txt
pip install -r requirements.txt
```

## Usage

After installation, you can use the package in your Python code:

```python
import pandas as pd
from auditanalytics import utils

# Load data from the package
data = pd.read_csv(utils.get_data_path('ch_2_yahoo_fin.csv'))

# Or start with the Jupyter notebooks
# Open notebooks/sample_sizes_p103.ipynb in Jupyter
```

## Chapters & Jupyter Notebooks
_(You can find the converted Jupyter notebooks for each chapter in the `notebooks/` directory. These provide Python implementations of the audit analytics procedures described in the book.)_

- Preface and Frontmatter
- Foreword by Erik Brynjolfsson
1. [Fundamentals of Auditing Financial Statements](notebooks/ch_1_aud_fs.ipynb)
1. [Foundations of Audit Analytics - Statistics](notebooks/metrics_estimates_p67.ipynb)
1. [Analysis of Accounting Transactions](notebooks/ch_3_acct_transactions.ipynb)
1. [Risk Assessment and Planning](notebooks/ram_dashboard_p98.ipynb)
1. [Analytical Review: Technical Analysis](notebooks/tech_analysis_p131.ipynb)
1. [Analytical Review: Intelligence Scanning](notebooks/scan_curated_p159.ipynb)
1. [Design of Audit Programs - Sample Sizes](notebooks/sample_sizes_p103.ipynb)
1. [Interim Compliance Tests](notebooks/ML_compliance_p235.ipynb)
1. [Substantive Tests - Trial Balance](notebooks/trial_balance_p272.ipynb)
1. [Substantive Tests - Accounts Receivable](notebooks/AR_p272.ipynb)
1. [Sarbanes-Oxley Engagements](notebooks/ML_SOX_p354.ipynb)
1. [Blockchains, Cybercrime and Forensics](notebooks/blockchain_p389.ipynb)
1. [Special Engagements: Forecasts and Valuation](notebooks/ch_12_special.ipynb)
1. [Simulated Transactions for Auditing Service Organizations](notebooks/simulation_p436.ipynb)

### Additional Notebooks

- [Accessing EDGAR Database](notebooks/accessing_edgar_p87.ipynb)
- [Advanced EDGAR Analysis](notebooks/accessing_edgar_p117.ipynb)
- [Sentiment Analysis](notebooks/sent_analysis_p145.ipynb)
- [Web Scraping for Audit Intelligence](notebooks/web_scraping_p166.ipynb)
- [US Census Data Analysis](notebooks/us_census_p127.ipynb)
- [AR Confirmation Procedures](notebooks/AR_confirmation_p285.ipynb)
- [Uncollectable Accounts Analysis](notebooks/uncollectables_p287.ipynb)
- [Stratified and Monetary Unit Sampling](notebooks/stratified_MUS_p315.ipynb)
- [Inventory Audit Procedures](notebooks/inventory_p327.ipynb)
- [Tests of Supporting Evidence](notebooks/supporting_evidence_p275.ipynb)

**Note:** The original R code files are preserved in the `R-code files in Quarto/` directory for reference.




### Feedback

You can leave a comment, or ask a question in our issue tracker.


## Chapter Synopses


#### Chapter 1:  Fundamentals of Auditing Financial Reports

Audits are independent examinations of the records of an organization to ascertain how far the financial statements present a true picture of the firm, and that accounting systems are well-controlled, legal and accurate. Auditing has become such a ubiquitous phenomenon in the world that academics have chronicled the transition to "Audit Societies".  The early 20th century saw the standardization of auditors' tests and reporting. Statistical sampling and computer tools to conduct statistical samples and opinions based on them are an integral part of modern auditing. This chapter surveys the state of the profession and what the 21st century auditor needs to know.

#### Chapter 2: Foundations of Audit Analytics

Broad application of statistical and data analytic tools are essential for the cost-effective completion of audits.  Fortunately R has become the go to language for analytics, and offers many features that reduce the cost of data acquisition, preparation, exploration and summarization.  It provides a scientific basis for audit decisions underlying the auditor's opinion.  Effective legal defense of audit methods is predicated on data analytics and statistical methods.  This chapter summarizes the subset of R capabilities that are germane to an audit.

#### Chapter 3: Analysis of Accounting Transactions

Accounting transactions are the 'raw data' of accounting system, but the idiosyncratic vernacular of accounting, and spotty empirical study of distributions and characteristics of accounting transactions mean that statistical methods that are applied in other disciplines are likely to prove suboptimal, and even counterproductive in auditing.  This chapter delineates the idiosyncrasies of accounting transactions and summaries, and describes tools to cost-effectively prepare and render decisions from client accounting data. 

#### Chapter 4: Risk Assessment and Planning

Risk assessment, planning and budgeting of audits are essential precursors to the successful audit.   The determination of risk of a particular subset of accounting operations related to the rendering of the audit opinion – i.e., on whether the accounts have material error when GAAP has been consistently applied.  This chapter delineates construction of the _risk assessment matrix_ – a collaborative “learning” worksheet to support a scientific foundation for audit scope, planning and budgeting prior to initiation of audit field tests. 

#### Chapter 5: Analytical Review -- Technical Analysis

Analytical procedures are evaluations of financial information made by a study of plausible relationships between both financial and non-financial data. They are used in all stages of the audit including planning, substantive testing and final review stage. This chapter surveys a range of R packages that ease technical analysis and data collection tasks in analytical review.


#### Chapter 6: Analytical Review -- Intelligence Scanning

Before the mid-2000s, inexpensive access to financial and non-financial data was spotty, unreliable and scarce. Today, there are numerous social network, news and discussion boards that offer both raw and curated, streaming sources of useful business intelligence available that allow analytical procedures to study the plausible relationships between both financial and non-financial data. The auditor who does not scan for such client and industry intelligence both increases the cost of auditing, and can be considered negligent in not investigating all available information about the financial health of their client.  


#### Chapter 7: Design of Audit Programs

Audit programs, from a scientific perspective, _natural experiments_ -- they are empirical studies in which the activities of firms, individuals or groups are exposed to the experimental and control conditions that are determined by nature or by other factors outside the control of the auditors.  This chapter details the cost-effective planning for an audit, based on a deep understanding of natural experiments and the proper analytical tools needed to draw conclusions from them.  


#### Chapter 8: Interim compliance tests

Compliance tests determine whether the firm’s transaction processing is in compliance with generally accepted accounting principles (GAAP).   They have grown increasingly important and are the basis for much of the reporting in the SAS No. 115 letter to management, and support management’s response in the Sarbanes-Oxley letter.  This chapter delineates the statistical tools used to insure cost effective compliance testing in the audit.


#### Chapter 9: Substantive Tests

Substantive testing directly supports the auditor's opinion that economic events in the real world are or are not accurately summarized in the financial statements of a firm. This chapter delineates the statistical tools used to insure cost effective substantive testing in the audit.

#### Chapter 10: Sarbanes-Oxley Engagements

Academic research on reporting from Sarbanes-Oxley Act of 2002 (SOX) has to date focused on internal consistency, compliance and accrual accounting assessments.  Some research has been performed on the related external risks such as fraud and security breaches.  This chapter surveys what we know about compliance cost and information content of SOX filings, and provides machine learning tools to assess the information contained in SOX reports. 

#### Chapter 11: Blockchains, Cybercrime and Forensics

Auditors are often asked to opine on technical security and encryption technologies, as well as providing admissible evidence in legal cases.  This chapter reviews the most commonly encountered security and encryption technologies, with guides to how auditors should assess and manage them.

#### Chapter 12: Special Engagements: Forecasts and Valuation

Auditors have an intimate understanding of their client’s finances.  Because of that, they are likely to be called upon to assess the value of a new or existing investment.  This chapter reviews the factors that go into performing a successful assurance and valuation assessment for a client. 


#### Chapter 13: Simulated Transactions for Auditing Service Organizations

Testing the shared, proprietary third-party platforms of service organizations and cloud computing presents auditors with a significant challenge. Auditors in these reviews can test automated controls by reading a 'deck' of known transactions and comparing these with the accounting reports generated by a client's automated system. This chapter delineates procedures for constructing and using these methods.






