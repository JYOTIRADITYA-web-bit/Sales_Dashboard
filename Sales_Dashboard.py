import pandas as pd
import streamlit as st
import plotly.express as px

# Load and parse dates correctly
df = pd.read_csv("Train.csv")
st.write("Columns in dataset:", df.columns.tolist())

df['Order Date'] = df['Order Date'].astype(str).str.strip()
df['Order Date'] = pd.to_datetime(df['Order Date'], dayfirst=True)

# Streamlit app settings
st.set_page_config(page_title="Sales Dashboard", page_icon="📊", layout="wide")
st.title("📊 Sales Dashboard")

# --- Date filter ---
min_date = df['Order Date'].min()
max_date = df['Order Date'].max()

col1, col2 = st.columns(2)
with col1:
    start_date = st.date_input("Start Date", min_value=min_date.date(),
                               max_value=max_date.date(), value=min_date.date())
with col2:
    end_date = st.date_input("End Date", min_value=min_date.date(),
                             max_value=max_date.date(), value=max_date.date())

mask = (df['Order Date'] >= pd.to_datetime(start_date)) & (df['Order Date'] <= pd.to_datetime(end_date))
filtered_df = df.loc[mask]

# --- Extra filters for Segment and Region ---
if 'Segment' in df.columns:
    segment_options = ["All"] + sorted(df['Segment'].dropna().unique().tolist())
    selected_segment = st.selectbox("Select Segment", segment_options)
    if selected_segment != "All":
        filtered_df = filtered_df[filtered_df['Segment'] == selected_segment]

if 'Region' in df.columns:
    region_options = ["All"] + sorted(df['Region'].dropna().unique().tolist())
    selected_region = st.selectbox("Select Region", region_options)
    if selected_region != "All":
        filtered_df = filtered_df[filtered_df['Region'] == selected_region]

# --- KPIs ---
st.subheader("📌 Key Metrics")
col1, col2 = st.columns(2)
with col1:
    st.metric("Total Orders", len(filtered_df))
with col2:
    if 'Sales' in filtered_df.columns:
        st.metric("Total Sales", f"${filtered_df['Sales'].sum():,.2f}")

# --- Charts ---
if not filtered_df.empty:
    # Orders over time
    fig_orders = px.histogram(filtered_df, x='Order Date', title="Orders Over Time")
    st.plotly_chart(fig_orders, use_container_width=True)

    # Monthly sales trend
    monthly_sales = (
        filtered_df
        .groupby(filtered_df['Order Date'].dt.to_period("M"))['Sales']
        .sum()
        .reset_index()
    )
    monthly_sales['Order Date'] = monthly_sales['Order Date'].dt.to_timestamp()
    fig_monthly = px.line(monthly_sales, x='Order Date', y='Sales',
                          title="📈 Monthly Sales Trend")
    st.plotly_chart(fig_monthly, use_container_width=True)

    # Sales by Segment
    if 'Segment' in filtered_df.columns:
        fig_seg = px.bar(filtered_df.groupby('Segment')['Sales'].sum().reset_index(),
                         x='Segment', y='Sales', title="Sales by Segment")
        st.plotly_chart(fig_seg, use_container_width=True)

    # Sales by Region
    if 'Region' in filtered_df.columns:
        fig_region = px.bar(filtered_df.groupby('Region')['Sales'].sum().reset_index(),
                            x='Region', y='Sales', title="Sales by Region")
        st.plotly_chart(fig_region, use_container_width=True)
else:

   
 
