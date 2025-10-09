import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Customer Segmentation Dashboard", layout="wide")

st.title("Customer Segmentation Dashboard - Murick Internship")

@st.cache_data
def load_data():
    try:
        rfm = pd.read_csv('rfm_data.csv')
        if 'Segment' not in rfm.columns:
            st.error("Segment column missing in rfm_data.csv. Please run the notebook to generate it.")
            return None
        return rfm
    except FileNotFoundError:
        st.error("rfm_data.csv not found. Ensure notebook is executed first.")
        return None

rfm = load_data()
if rfm is None:
    st.stop()

st.header("RFM Distribution")
col1, col2, col3 = st.columns(3)
with col1:
    fig1 = px.histogram(rfm, x='Recency', nbins=20, title="Recency")
    st.plotly_chart(fig1, use_container_width=True)
with col2:
    fig2 = px.histogram(rfm, x='Frequency', nbins=20, title="Frequency")
    st.plotly_chart(fig2, use_container_width=True)
with col3:
    fig3 = px.histogram(rfm, x='Monetary', nbins=20, title="Monetary")
    st.plotly_chart(fig3, use_container_width=True)

st.header("3D Customer Segments")
fig_3d = px.scatter_3d(rfm, x='Recency', y='Frequency', z='Monetary', color='Segment',
                       title='Customer Segments in 3D', opacity=0.7)
st.plotly_chart(fig_3d, use_container_width=True)

st.header("Segment Characteristics")
segment_stats = rfm.groupby('Segment')[['Recency', 'Frequency', 'Monetary']].mean().reset_index()
fig_stats = px.bar(segment_stats, x='Segment', y=['Recency', 'Frequency', 'Monetary'],
                   title='Average RFM by Segment', barmode='group')
st.plotly_chart(fig_stats, use_container_width=True)

st.header("Marketing Recommendations")
st.markdown("""
- **Champions**: Exclusive offers, VIP perks (20% off).
- **Loyal**: Upsell premium products, referral bonuses.
- **At-Risk**: Reactivation emails with discounts.
- **Lost**: Win-back campaigns with 30% off first purchase.
""")