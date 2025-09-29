# ML Classification Project - Heart Disease Prediction

## Overview
Task 5 of the AI & ML Internship at Murick Technologies. This project builds classification models on the Heart Disease Dataset to predict cardiovascular disease presence. Includes preprocessing, feature engineering, training Logistic Regression, Random Forest, and SVM models, evaluation (accuracy, F1, ROC-AUC), feature importance, visualizations, and comparisons.

## Dataset
Heart Disease Dataset (303 rows, 13 features: age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal; target: 0=no disease, 1=disease).

## Files
- `heart_classification.ipynb`: Jupyter Notebook with complete analysis.
- `heart_data_cleaned.csv`: Processed dataset.
- `recommendations.md`: Actionable insights for medical applications.
- `visuals/`: PNGs (target_distribution.png, feature_importance.png, confusion_matrix.png, roc_curve.png, model_comparison.png).
- `interactive_roc.html`: Interactive ROC curve (Plotly).

## Installation
1. Clone: `git clone https://github.com/muzamal478/MurickInternship2025.git`
2. Navigate: `cd MurickInternship2025/ML_Classification_Project`
3. Install: `pip install pandas numpy seaborn matplotlib scikit-learn plotly imbalanced-learn`
4. Run: `jupyter notebook heart_classification.ipynb`

## Usage
Execute notebook cells for preprocessing, modeling, evaluation, and visualizations.

## Key Findings
- Random Forest: 92% accuracy, F1=0.93, AUC=0.95.
- Top features: cp (chest pain), thalach (max heart rate), ca (major vessels).
- Comparisons: Random Forest outperforms Logistic Regression (88%) and SVM (90%).

## Author
Muzamil Asghar  
LinkedIn: [https://www.linkedin.com/in/muzamalasgharofficial/](https://www.linkedin.com/in/muzamalasgharofficial/)  
GitHub: [https://github.com/muzamal478](https://github.com/muzamal478)

## License
MIT