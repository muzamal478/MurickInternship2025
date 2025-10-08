# Customer Segmentation with RFM & K-Means

## Overview
Task 6 of Murick Technologies AI & ML Internship. Performs RFM analysis on Online Retail Dataset, applies K-Means clustering to identify segments (Champions, Loyal, At-Risk, Lost), evaluates with Elbow/Silhouette, visualizes clusters, provides marketing recs, and deploys interactive Streamlit app.

## Dataset
Online Retail (541K transactions, 2010-2011 UK e-commerce data: InvoiceNo, StockCode, Description, Quantity, InvoiceDate, UnitPrice, CustomerID, Country).

## Files
- `customer_segmentation.ipynb`: Jupyter Notebook for RFM, clustering, evaluation, visualizations.
- `rfm_data.csv`: Processed RFM data.
- `recommendations.md`: Marketing strategies per segment.
- `visuals/`: PNGs (rfm_distribution.png, elbow.png, silhouette.png, 3d_clusters.png).
- `streamlit_app.py`: Interactive Streamlit app with Plotly charts.
- `requirements.txt`: Dependencies.

## Installation & Setup
1. Clone: `git clone https://github.com/muzamal478/MurickInternship2025.git`
2. cd `MurickInternship2025/Customer_Segmentation`
3. Install: `pip install -r requirements.txt`
4. Run Notebook: `jupyter notebook customer_segmentation.ipynb`
5. Run App: `streamlit run streamlit_app.py`

## Key Findings
- Optimal K=4 (Silhouette=0.55).
- Segments: Champions (high RFM), Loyal (high FM), At-Risk (low R), Lost (low all).
- Champions: 15% customers, 40% revenue.

## Usage
- Notebook: End-to-end analysis.
- App: Interactive dashboards for segments.

## Author
Muzamil Asghar  
LinkedIn: https://www.linkedin.com/in/muzamalasgharofficial/  
GitHub: https://github.com/muzamal478

## License
MIT