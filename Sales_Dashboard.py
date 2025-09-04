import pandas as pd
import streamlit as st
import plotly.express as px

# Load and parse dates correctly
df = pd.read_csv("Train.csv")
df['Order Date'] = df['Order Date'].astype(str).str.strip()
df['Order Date'] = pd.to_datetime(df['Order Date'], dayfirst=True)

# Optional: formatted date string for display only
df['Order Date (Formatted)'] = df['Order Date'].dt.strftime('%m/%d/%Y')

# Streamlit app
st.title("📊 Sales Dashboard")

# Date filter
min_date = df['Order Date'].min()
max_date = df['Order Date'].max()

start_date = st.date_input(
    "Start Date",
    min_value=min_date.date(),
    max_value=max_date.date(),
    value=min_date.date()
)
end_date = st.date_input(
    "End Date",
    min_value=min_date.date(),
    max_value=max_date.date(),
    value=max_date.date()
)

# Filter data by date
mask = (df['Order Date'] >= pd.to_datetime(start_date)) & (df['Order Date'] <= pd.to_datetime(end_date))
filtered_df = df.loc[mask]

# Example plot
if not filtered_df.empty:
    fig = px.histogram(filtered_df, x='Order Date', title="Orders Over Time")
    st.plotly_chart(fig)
else:
    st.warning("No data available for selected date range.")
