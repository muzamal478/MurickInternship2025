# Student Performance Prediction Platform

## Overview
Capstone project for Murick Technologies AI & ML Internship. Predicts student grades (G3) using a dataset with 33 features (school, sex, age, ..., G3). Features regression (XGBoost, R²=0.85), classification (88% accuracy), and a Streamlit app with dashboards, predictions, analytics, and reports. Fixed scatter plot error by using unscaled absences.

## Dataset
Kaggle Student Performance Dataset: https://www.kaggle.com/datasets/larsen0966/student-performance-data-set (649 rows, 33 columns).

## Files
- `models_analysis.ipynb`: Preprocessing, regression/classification models, tuning, visualizations.
- `app.py`: Streamlit app with 8 pages (dashboard, predictions, analytics, etc.).
- `student_data_cleaned.csv`: Preprocessed data.
- `requirements.txt`: Dependencies.
- `visuals/`: PNGs and HTML plots.
- `interactive_dashboard.html`: Interactive Plotly scatter plot.

## Installation
```bash
git clone https://github.com/muzamal478/MurickInternship2025.git
cd MurickInternship2025/Student_Performance_Prediction
pip install -r requirements.txt
jupyter notebook models_analysis.ipynb
streamlit run app.py
```

## Key Findings
- XGBoost: R²=0.85, RMSE=1.4.
- Classification: 88% accuracy for Poor/Average/Good/Excellent.
- Top features: G2 (35%), G1 (25%), studytime (15%).
- Insights: Urban students outperform rural by 10%; parental education boosts grades 15%.

## Author
Muzamil Asghar  
LinkedIn: https://www.linkedin.com/in/muzamalasgharofficial/  
GitHub: https://github.com/muzamal478

## License
MIT