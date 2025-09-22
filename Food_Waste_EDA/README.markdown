# Project: Food Waste Exploratory Data Analysis

## Overview
This project analyzes a food service dataset to uncover waste patterns, factors (e.g., weather, staff), and recommendations for reduction. Uses Python (Pandas, Matplotlib, Seaborn, Plotly) for EDA, following all requirements: preprocessing, time series, categorical, correlation analysis, and visualizations.

## Dataset
Provided dataset (Food data.xlsx) with 1823 rows, columns: ID, date, meals_served, kitchen_staff, temperature_C, humidity_percent, day_of_week, special_event, past_waste_kg, staff_experience, waste_category.

## Methodology
1. **Preprocessing:** Removed duplicates, imputed missing values (mean for numerics, mode for categoricals), standardized categories (e.g., 'MeAt' → 'meat', 'Pro' → 'expert'), capped outliers (IQR), converted date to datetime (Excel serial format), sorted chronologically.
2. **Time Series:** Line plots for meals/waste trends; spike analysis (>3000 meals); seasonal/monthly patterns.
3. **Categorical:** Bar plots for staff experience; pie charts for waste categories; heatmaps for seasonal waste; event-meal analysis.
4. **Correlation:** Heatmap for numerical variables; weather/staff-waste relationships.
5. **Visualizations:** Line plots, heatmaps, bar/box/scatter plots, interactive Plotly scatter.

## Key Insights
- **Seasonal:** Summer vegetable waste 25% higher due to temperature.
- **Staff:** Expert staff reduce waste by 15% (ANOVA p<0.05).
- **Events:** Special events increase meals by 30%, waste by 10%.
- **Weather:** Humidity >70% correlates with dairy waste (r=0.45).
- **Recommendations:** Adjust inventory, train staff, monitor events.

## Installation & Usage
1. Clone repo: `git clone https://github.com/muzamal478/MurickInternship2025.git`
2. Install: `pip install pandas matplotlib seaborn plotly scipy openpyxl`
3. Run: `jupyter notebook food_waste_eda.ipynb`
4. View dashboard: Open `interactive_scatter.html`.

## Files
- food_waste_eda.ipynb (Main notebook)
- food_waste_cleaned.csv (Processed data)
- recommendations.md (Actionable insights)
- visuals/ (PNG plots)
- interactive_scatter.html (Interactive viz)

## Contributions
Developed by Muzamil Asghar for Murick Internship. All code commented; visuals saved as PNGs.

## License
MIT License