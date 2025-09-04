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
st.set_page_config(page_title="Sales Dashboard", page_icon="📊", layout="wide")
st.title("📊 Sales Dashboard")

# Date filter
min_date = df['Order Date'].min()
max_date = df['Order Date'].max()

col1, col2 = st.columns(2)
with col1:
    start_date = st.date_input(
        "Start Date",
        min_value=min_date.date(),
        max_value=max_date.date(),
        value=min_date.date()
    )
with col2:
    end_date = st.date_input(
        "End Date",
        min_value=min_date.date(),
        max_value=max_date.date(),
        value=max_date.date()
    )

# Filter data by date
mask = (df['Order Date'] >= pd.to_datetime(start_date)) & (df['Order Date'] <= pd.to_datetime(end_date))
filtered_df = df.loc[mask]

# Show KPIs
st.subheader("📌 Key Metrics")
col1, col2 = st.columns(2)
with col1:
    st.metric("Total Orders", len(filtered_df))
with col2:
    if 'Sales' in filtered_df.columns:
        st.metric("Total Sales", f"${filtered_df['Sales'].sum():,.2f}")

# Charts
if not filtered_df.empty:
    # Orders over time
    fig_orders = px.histogram(filtered_df, x='Order Date', title="Orders Over Time")
    st.plotly_chart(fig_orders, use_container_width=True)

    # Monthly trend
    monthly_sales = (
        filtered_df
        .groupby(filtered_df['Order Date'].dt.to_period("M"))
        .size()
        .reset_index(name='Orders')
    )
    monthly_sales['Order Date'] = monthly_sales['Order Date'].dt.to_timestamp()
    fig_monthly = px.line(monthly_sales, x='Order Date', y='Orders', title="📈 Monthly Sales Trend")
    st.plotly_chart(fig_monthly, use_container_width=True)

    # Sales by Category
    if 'Category' in filtered_df.columns:
        fig_cat = px.bar(filtered_df, x='Category', title="Sales by Category")
        st.plotly_chart(fig_cat, use_container_width=True)

    # Sales by Region
    if 'Region' in filtered_df.columns:
        fig_region = px.bar(filtered_df, x='Region', title="Sales by Region")
        st.plotly_chart(fig_region, use_container_width=True)
else:
    st.warning("⚠️ No data available for selected date range.")
