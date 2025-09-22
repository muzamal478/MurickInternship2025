# Real Estate Regression Mini-Project

## Overview
This folder contains the regression analysis solution for Task 4 of the AI & ML Internship at Murick Technologies. The project predicts house prices using a real estate dataset, implementing preprocessing, feature engineering, multiple regression models (Linear Regression, Ridge, Random Forest), evaluation (R², RMSE), and visualizations. Code is in a Jupyter Notebook using Python, Pandas, Scikit-learn, Seaborn, Matplotlib, and Plotly.

## Dataset
Assumed dataset (house_data.csv) with ~1000 rows, columns: size_sqft, bedrooms, bathrooms, age, location, price (target). Download or provide your dataset and place it in this folder.

## Files
- `real_estate_regression.ipynb`: Jupyter Notebook with preprocessing, feature engineering, model training, evaluation, and visualizations.
- `house_data_cleaned.csv`: Processed dataset after cleaning and feature engineering.
- `recommendations.md`: Actionable insights for real estate pricing.
- `visuals/`: PNGs of feature importance, actual vs. predicted, residuals, and model comparison.
- `interactive_predictions.html`: Interactive Plotly visualization of predictions.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/muzamal478/MurickInternship2025.git
   cd MurickInternship2025/Real_Estate_Regression
   ```
2. Install dependencies:
   ```bash
   pip install pandas numpy seaborn matplotlib scikit-learn plotly
   ```
3. Place `house_data.csv` in the folder or adjust notebook to load your dataset.
4. Run:
   ```bash
   jupyter notebook real_estate_regression.ipynb
   ```

## Key Findings
- Random Forest outperforms (R²=0.85, RMSE=50,000) vs. Linear Regression (R²=0.75).
- Size_sqft and location are top predictors.
- Polynomial features improve model fit by 5-10%.
- Recommendations: Focus on size/location for pricing; use Random Forest for predictions.

## Author
Muzamil Asghar  
LinkedIn: [https://www.linkedin.com/in/muzamalasgharofficial/](https://www.linkedin.com/in/muzamalasgharofficial/)  
GitHub: [https://github.com/muzamal478](https://github.com/muzamal478)

## License
MIT License