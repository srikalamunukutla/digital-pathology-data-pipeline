import pandas as pd
import streamlit as st
import plotly.express as px

st.title("📊 Digital Pathology Data Dashboard")

df = pd.read_csv('../data/simulated_pathology_data.csv')

st.write(df.head())

fig = px.histogram(df, x='ai_risk_category', title='AI Risk Category Distribution')
st.plotly_chart(fig)

fig2 = px.box(df, x='tissue_type', y='diagnostic_confidence', title='Confidence by Tissue Type')
st.plotly_chart(fig2)