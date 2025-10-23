# Lead Service Line Prediction and Analysis | CEE 690

**Group:** Ex Machina  
**Members:** Alec Henderson, Nathan De Jesus, Michael Jiang

## Overview

This project aims to predict and analyze the presence of lead in water service lines using machine learning techniques. Service lines are pipes connecting main water lines to individual buildings, and many installed between the 1950s-1980s contain lead, posing significant public health risks.

## Problem Statement

As mandated by the EPA's Lead and Copper Rule Revisions (LCRR) finalized in 2021, water systems must maintain complete inventories of all service lines, categorizing them as:

- Lead
- Galvanized Requiring Replacement
- Non-lead
- Unknown

Physically verifying service line materials through excavation is time-consuming and expensive. This project leverages historical data and machine learning to predict lead service line locations, helping communities identify health risks and comply with federal regulations.

## Project Structure

```
.
├── README.md
├── main.ipynb           # Main analysis notebook
├── data/                # Dataset directory
│   └── raw/            # Raw data files
│   └── processed/      # Processed/cleaned data
├── models/             # Saved model files
├── results/            # Output visualizations and reports
└── requirements.txt    # Python dependencies
```

## Data Sources

### Primary Dataset

- **New York State Lead Service Line Inventory**: Publicly available dataset containing locality, street addresses, coordinates, service line installation/replacement dates, lead connector presence, service line materials, and detection methods.

### Supplementary Data (Planned)

- Home builder information
- Construction dates
- Property characteristics via APIs (Zillow, ATTOM)

**Note:** API access may be limited due to cost constraints.

## Methodology

### Preprocessing

- Convert non-numerical data to numerical values using label encoding
- Normalization and feature scaling
- Feature engineering from housing and installation data

### Machine Learning Approaches

1. **t-SNE Dimensionality Reduction** (Alec Henderson)
   - Unsupervised exploration of data patterns
   - Visualization of correlations with pipe materials
2. **Support Vector Machines (SVM)** (Nathan De Jesus)
   - Classification of service line materials
3. **Random Forests** (Michael Jiang)
   - Ensemble method for prediction and feature importance analysis

### Performance Metric

Model accuracy in identifying lead service lines.

## Getting Started

### Prerequisites

```bash
Python 3.8+
Jupyter Notebook
```

### Installation

```bash
# Clone the repository
git clone [repository-url]
cd [repository-name]

# Install dependencies
pip install -r requirements.txt

# Launch Jupyter Notebook
jupyter notebook main.ipynb
```

### Required Libraries

- pandas
- numpy
- scikit-learn
- matplotlib
- seaborn

## Workflow

1. **Data Collection**: Gather NY State LSL inventory and supplementary property data
2. **Data Preprocessing**: Clean, encode, and normalize features
3. **Exploratory Analysis**: Use t-SNE for pattern visualization
4. **Model Training**: Implement SVM and Random Forest classifiers
5. **Evaluation**: Compare model performance and accuracy
6. **Analysis**: Interpret results and identify high-risk areas

## Team Responsibilities

| Task                          | Team Member(s)  |
| ----------------------------- | --------------- |
| Data Preprocessing & Analysis | All Members     |
| t-SNE Implementation          | Alec Henderson  |
| SVM Implementation            | Nathan De Jesus |
| Random Forest Implementation  | Michael Jiang   |

## References

1. [New York State Lead Service Line Inventory](https://health.data.ny.gov/Health/New-York-State-Lead-Service-Line-Inventory/j63k-4n92/about_data)
2. [Garden City NY Lead Data](https://www.gardencityny.net/480/Lead-Your-Water)
3. [Blue Conduit](https://blueconduit.com/)
4. [EPA Lead and Copper Rule Revisions](https://www.epa.gov/ground-water-and-drinking-water/revised-lead-and-copper-rule)
5. [The Search for Lead Pipes in Flint, Michigan](https://arxiv.org/pdf/1806.10692)

## Project Goals

- Accurately predict lead service line locations using historical data
- Reduce costs associated with physical verification
- Support public health initiatives and regulatory compliance
- Provide actionable insights for water system management

## Contributing

This is an academic project. For questions or suggestions, please contact the team members.

## License

This project is for educational purposes for Data Science and Machine Learning Applications for Duke MEMS Master's program for Fall of 2025.

---

_Last Updated: October 2025_
