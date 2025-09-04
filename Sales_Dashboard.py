import pandas as pd

# Load CSV
df = pd.read_csv("Train.csv")

# Make sure to remove leading/trailing whitespace from dates
df['Order Date'] = df['Order Date'].astype(str).str.strip()

# Convert with dayfirst=True, NO 'format'
df['Order Date'] = pd.to_datetime(df['Order Date'], dayfirst=True, errors='raise')

# Show result
print("✅ Date parsing successful!")
print(df['Order Date'].head())

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

start_date = st.date_input("Start Date", min_value=min_date.date(), max_value=max_date.date(), value=min_date.date())
end_date = st.date_input("End Date", min_value=min_date.date(), max_value=max_date.date(), value=max_date.date())

# Filter data by date
mask = (df['Order Date'] >= pd.to_datetime(start_date)) & (df['Order Date'] <= pd.to_datetime(end_date))
filtered_df = df.loc[mask]

# Example plot
if not filtered_df.empty:
    fig = px.histogram(filtered_df, x='Order Date', title="Orders Over Time")
    st.plotly_chart(fig)
else:
    st.warning("No data available for selected date range.")

import fileinput

file_path = r"C:\Users\Chava\Sales Dashboard\Data\Sales_Dashboard.py"

# Replace all 'null' with 'None'
with fileinput.FileInput(file_path, inplace=True, backup=".bak") as file:
    for line in file:
        print(line.replace("null", "None"), end="")


print("✅ Finished! A backup of the original file was saved with .bak extension.")

import pandas as pd

# Load dataset
df = pd.read_csv("Train.csv")

# Inspect
print(df.head())
print(df.info())
print(df.describe())

import pandas as pd

# Load CSV
df = pd.read_csv("Train.csv")

# Make sure to remove leading/trailing whitespace from dates
df['Order Date'] = df['Order Date'].astype(str).str.strip()

# Convert with dayfirst=True, NO 'format'
df['Order Date'] = pd.to_datetime(df['Order Date'], dayfirst=True, errors='raise')

# Show result
print("✅ Date parsing successful!")
print(df['Order Date'].head())

import pandas as pd

# Read the CSV correctly
df = pd.read_csv("Train.csv")

# Convert 'Order Date' column to datetime
df['Order Date'] = pd.to_datetime(df['Order Date'], format="%d/%m/%Y")

import matplotlib.pyplot as plt

df.groupby(df['Order Date'].dt.to_period('M'))['Sales'].sum().plot(kind='line')
plt.title("Monthly Sales Trend")
plt.show()

top_products = df.groupby('Product Name')['Sales'].sum().nlargest(10)
top_products.plot(kind='bar')
plt.title("Top 10 Products by Sales")
plt.show()

df.groupby('Category')['Sales'].sum().plot(kind='pie', autopct='%1.1f%%')
plt.title("Sales by Category")
plt.show()

