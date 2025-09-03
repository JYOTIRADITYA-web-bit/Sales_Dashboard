{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 44,
   "id": "d69ef222-8314-4653-9c01-0b57db3d0b0b",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "✅ Date parsing successful!\n",
      "0   2017-11-08\n",
      "1   2017-11-08\n",
      "2   2017-06-12\n",
      "3   2016-10-11\n",
      "4   2016-10-11\n",
      "Name: Order Date, dtype: datetime64[ns]\n"
     ]
    }
   ],
   "source": [
    "import pandas as pd\n",
    "\n",
    "# Load CSV\n",
    "df = pd.read_csv(\"Train.csv\")\n",
    "\n",
    "# Make sure to remove leading/trailing whitespace from dates\n",
    "df['Order Date'] = df['Order Date'].astype(str).str.strip()\n",
    "\n",
    "# Convert with dayfirst=True, NO 'format'\n",
    "df['Order Date'] = pd.to_datetime(df['Order Date'], dayfirst=True, errors='raise')\n",
    "\n",
    "# Show result\n",
    "print(\"✅ Date parsing successful!\")\n",
    "print(df['Order Date'].head())\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 46,
   "id": "686bf5e0-f90f-40d2-9a62-a677d151479a",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "2025-09-02 20:40:55.303 WARNING streamlit.runtime.scriptrunner_utils.script_run_context: Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-09-02 20:40:55.402 \n",
      "  \u001b[33m\u001b[1mWarning:\u001b[0m to view this Streamlit app on a browser, run it with the following\n",
      "  command:\n",
      "\n",
      "    streamlit run C:\\Users\\Chava\\AppData\\Local\\Programs\\Python\\Python313\\Lib\\site-packages\\ipykernel_launcher.py [ARGUMENTS]\n",
      "2025-09-02 20:40:55.403 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-09-02 20:40:55.405 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-09-02 20:40:55.409 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-09-02 20:40:55.411 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-09-02 20:40:55.413 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-09-02 20:40:55.416 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-09-02 20:40:55.417 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-09-02 20:40:55.418 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-09-02 20:40:55.419 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-09-02 20:40:55.419 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-09-02 20:40:55.420 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-09-02 20:40:55.421 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-09-02 20:40:55.421 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-09-02 20:40:55.422 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-09-02 20:40:56.087 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-09-02 20:40:56.089 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-09-02 20:40:56.091 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-09-02 20:40:56.092 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-09-02 20:40:56.094 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n"
     ]
    }
   ],
   "source": [
    "import pandas as pd\n",
    "import streamlit as st\n",
    "import plotly.express as px\n",
    "\n",
    "# Load and parse dates correctly\n",
    "df = pd.read_csv(\"Train.csv\")\n",
    "df['Order Date'] = df['Order Date'].astype(str).str.strip()\n",
    "df['Order Date'] = pd.to_datetime(df['Order Date'], dayfirst=True)\n",
    "\n",
    "# Optional: formatted date string for display only\n",
    "df['Order Date (Formatted)'] = df['Order Date'].dt.strftime('%m/%d/%Y')\n",
    "\n",
    "# Streamlit app\n",
    "st.title(\"📊 Sales Dashboard\")\n",
    "\n",
    "# Date filter\n",
    "min_date = df['Order Date'].min()\n",
    "max_date = df['Order Date'].max()\n",
    "\n",
    "start_date = st.date_input(\"Start Date\", min_value=min_date.date(), max_value=max_date.date(), value=min_date.date())\n",
    "end_date = st.date_input(\"End Date\", min_value=min_date.date(), max_value=max_date.date(), value=max_date.date())\n",
    "\n",
    "# Filter data by date\n",
    "mask = (df['Order Date'] >= pd.to_datetime(start_date)) & (df['Order Date'] <= pd.to_datetime(end_date))\n",
    "filtered_df = df.loc[mask]\n",
    "\n",
    "# Example plot\n",
    "if not filtered_df.empty:\n",
    "    fig = px.histogram(filtered_df, x='Order Date', title=\"Orders Over Time\")\n",
    "    st.plotly_chart(fig)\n",
    "else:\n",
    "    st.warning(\"No data available for selected date range.\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 48,
   "id": "e84549d7-3473-4055-afc0-34c7d817ec33",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "✅ Finished! A backup of the original file was saved with .bak extension.\n"
     ]
    }
   ],
   "source": [
    "import fileinput\n",
    "\n",
    "file_path = r\"C:\\Users\\Chava\\Sales Dashboard\\Data\\Sales_Dashboard.py\"\n",
    "\n",
    "# Replace all 'null' with 'None'\n",
    "with fileinput.FileInput(file_path, inplace=True, backup=\".bak\") as file:\n",
    "    for line in file:\n",
    "        print(line.replace(\"null\", \"None\"), end=\"\")\n",
    "\n",
    "\n",
    "print(\"✅ Finished! A backup of the original file was saved with .bak extension.\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 49,
   "id": "6ee0773d-6b47-4965-8807-334837e5a9cd",
   "metadata": {},
   "outputs": [
    {
     "ename": "SyntaxError",
     "evalue": "invalid syntax (3136570444.py, line 1)",
     "output_type": "error",
     "traceback": [
      "  \u001b[36mCell\u001b[39m\u001b[36m \u001b[39m\u001b[32mIn[49]\u001b[39m\u001b[32m, line 1\u001b[39m\n\u001b[31m    \u001b[39m\u001b[31mstreamlit run C:\\Users\\Chava\\AppData\\Local\\Programs\\Python\\Python313\\Lib\\site-packages\\ipykernel_launcher.py [ARGUMENTS]\u001b[39m\n              ^\n\u001b[31mSyntaxError\u001b[39m\u001b[31m:\u001b[39m invalid syntax\n"
     ]
    }
   ],
   "source": [
    "streamlit run C:\\Users\\Chava\\AppData\\Local\\Programs\\Python\\Python313\\Lib\\site-packages\\ipykernel_launcher.py [ARGUMENTS]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "ce8310c3-af34-482f-a64e-11ffe1655146",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.13.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
