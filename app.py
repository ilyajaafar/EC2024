import streamlit as st
import pandas as pd
import plotly.express as px
st.set_page_config(
    page_title="Scientific Visualization"
)

st.header("Scientific Visualization", divider="gray")


# --- Streamlit Application Start ---

st.title("Arts Faculty Gender Distribution Dashboard 📊")
st.markdown("These interactive charts visualize the gender breakdown for students in the 'Arts' faculty.")

# 1. Setup Dummy DataFrame (MUST have 'Faculty' and 'Gender' columns)
# This simulates loading your 'df' DataFrame.
data = {
    'Faculty': ['Arts'] * 70 + ['Science'] * 30,
    'Gender': ['Female'] * 50 + ['Male'] * 15 + ['Other'] * 5 + ['Male'] * 30
}
df = pd.DataFrame(data)
# --------------------------------------------------------------------------

# Filter the DataFrame for Arts Faculty, as done in your original code
arts_df = df[df['Faculty'] == 'Arts'].copy()

# --- 1. Count Plot (Bar Chart) using Plotly Express ---

st.header("1. Gender Distribution in Arts Faculty (Bar Chart)")

# Plotly Express automatically aggregates the counts for the Count Plot equivalent
fig_bar = px.bar(
    arts_df,
    x='Gender',
    title='Distribution of Gender in Arts Faculty',
    labels={'Gender': 'Gender', 'count': 'Count'}, # Customize axis labels
    color='Gender' # Optional: Color bars by gender
)

# Streamlit Display for Plotly figure
st.plotly_chart(fig_bar, use_container_width=True)

st.divider()

# --- 2. Pie Chart using Plotly Express ---

st.header("2. Gender Distribution in Arts Faculty (Pie Chart)")

# Calculate the value counts (counts of each gender) for the Pie Chart
gender_counts_arts = arts_df['Gender'].value_counts().reset_index()
gender_counts_arts.columns = ['Gender', 'Count'] # Rename columns for Plotly

fig_pie = px.pie(
    gender_counts_arts,
    values='Count',
    names='Gender',
    title='Distribution of Gender in Arts Faculty',
    hole=0.3 # Optional: Makes it a donut chart
)

# Streamlit Display for Plotly figure
st.plotly_chart(fig_pie, use_container_width=True)
