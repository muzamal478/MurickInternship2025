# Data Analysis on Adult.csv

## Overview
This folder contains the data analysis solution for Task 2 of the AI & ML Internship at Murick Technologies. The analysis uses the Adult.csv dataset to predict income (>50K or ≤50K) through preprocessing, exploratory data analysis (EDA), and visualizations. The code is implemented in a Jupyter Notebook using Python, Pandas, Seaborn, and Matplotlib.

## Files
- `adult_analysis.ipynb`: Jupyter Notebook with data loading, preprocessing, EDA, and findings.
- `adult.csv`: UCI Adult Income dataset (optional, not included in repo due to size; download from [UCI](https://archive.ics.uci.edu/ml/datasets/adult)).

## Installation
1. Ensure Python 3.9+ is installed.
2. Clone the repository:
   ```bash
   git clone https://github.com/muzamal478/MurickInternship2025.git
   cd MurickInternship2025/Data_Analysis_Adult
   ```
3. Install dependencies:
   ```bash
   pip install pandas numpy seaborn matplotlib scikit-learn
   ```
4. Download `adult.csv` from [UCI](https://archive.ics.uci.edu/ml/datasets/adult) and place in the folder.

## Usage
Run the Jupyter Notebook:
```bash
jupyter notebook adult_analysis.ipynb
```
Follow the cells to execute data loading, preprocessing, EDA, and visualizations.

## Key Findings
- Income distribution: ~76% earn ≤50K, ~24% earn >50K.
- Strong correlations: Education level, occupation, and hours worked influence higher income.
- Missing values handled via mode imputation for categorical features.
- Visualizations: Age distribution, education vs. income, and occupation trends.

## Author
Muzamil Asghar  
LinkedIn: [https://www.linkedin.com/in/muzamalasgharofficial/](https://www.linkedin.com/in/muzamalasgharofficial/)  
GitHub: [https://github.com/muzamal478](https://github.com/muzamal478)

## License
MIT License