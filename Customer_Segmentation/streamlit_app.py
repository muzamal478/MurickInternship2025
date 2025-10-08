import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

st.title("Customer Segmentation Dashboard - Murick Internship")

@st.cache_data
def load_data():
    rfm = pd.read_csv('rfm_data.csv')
    return rfm

rfm = load_data()

st.header("RFM Distribution")
col1, col2, col3 = st.columns(3)
fig1 = px.histogram(rfm, x='Recency', nbins=20)
st.plotly_chart(fig1, use_container_width=True)

fig2 = px.histogram(rfm, x='Frequency', nbins=20)
st.plotly_chart(fig2, use_container_width=True)

fig3 = px.histogram(rfm, x='Monetary', nbins=20)
st.plotly_chart(fig3, use_container_width=True)

st.header("3D Clusters")
fig_3d = px.scatter_3d(rfm, x='Recency', y='Frequency', z='Monetary', color='Segment',
                       title='Customer Segments in 3D')
st.plotly_chart(fig_3d, use_container_width=True)

st.header("Segment Characteristics")
segment_stats = rfm.groupby('Segment')[['Recency', 'Frequency', 'Monetary']].mean().reset_index()
fig_stats = px.bar(segment_stats, x='Segment', y=['Recency', 'Frequency', 'Monetary'],
                   title='Average RFM by Segment', barmode='group')
st.plotly_chart(fig_stats, use_container_width=True)

st.header("Recommendations")
st.write("""
- **Champions**: Reward with exclusive offers.
- **Loyal**: Upsell premium products.
- **At-Risk**: Send reactivation emails.
- **Lost**: Win-back with discounts.
""")

if st.button("Re-run Clustering"):
    st.cache_data.clear()
    st.rerun()