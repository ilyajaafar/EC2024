import streamlit as st
import pandas as pd
import plotly.express as px


# Example dummy data (for testing only)
data = {
    'Faculty': ['Arts', 'Arts', 'Science', 'Arts', 'Engineering', 'Arts', 'Science', 'Arts'],
    'Gender': ['Male', 'Female', 'Female', 'Male', 'Male', 'Female', 'Female', 'Male'],
    'Bachelor  Academic Year in EU': ['Year 1', 'Year 2', 'Year 1', 'Year 3', 'Year 2', 'Year 3', 'Year 4', 'Year 2'],
    'S.S.C (GPA)': [3.5, 4.0, 3.8, 3.2, 3.0, 4.5, 3.7, 4.2]
}
df = pd.DataFrame(data)

st.title("📊 Data Visualization Dashboard")

# ================================
# 1️⃣ Gender distribution (Arts Faculty)
# ================================
st.header("1️⃣ Gender Distribution in Arts Faculty")

arts_df = df[df['Faculty'] == 'Arts'].copy()

# --- Bar Chart ---
gender_counts = arts_df['Gender'].value_counts().reset_index()
gender_counts.columns = ['Gender', 'Count']

fig_bar = px.bar(
    gender_counts,
    x='Gender',
    y='Count',
    color='Gender',
    title='Distribution of Gender in Arts Faculty (Bar)',
    text='Count'
)
fig_bar.update_traces(textposition='outside')
st.plotly_chart(fig_bar, use_container_width=True)

# --- Pie Chart ---
fig_pie = px.pie(
    gender_counts,
    names='Gender',
    values='Count',
    title='Distribution of Gender in Arts Faculty (Pie)',
    hole=0  # 0 = normal pie, 0.5 = donut
)
st.plotly_chart(fig_pie, use_container_width=True)

# ================================
# 2️⃣ Bachelor Academic Year Distribution
# ================================
st.header("2️⃣ Distribution of Bachelor Academic Year in EU")

bachelor_counts = df['Bachelor  Academic Year in EU'].value_counts().sort_index().reset_index()
bachelor_counts.columns = ['Academic Year', 'Count']

# --- Horizontal Bar Chart ---
fig_year_bar = px.bar(
    bachelor_counts,
    x='Count',
    y='Academic Year',
    orientation='h',
    color='Academic Year',
    title='Distribution of Bachelor Academic Year in EU (Bar)'
)
st.plotly_chart(fig_year_bar, use_container_width=True)

# --- Pie Chart ---
fig_year_pie = px.pie(
    bachelor_counts,
    names='Academic Year',
    values='Count',
    title='Distribution of Bachelor Academic Year in EU (Pie)',
    hole=0
)
st.plotly_chart(fig_year_pie, use_container_width=True)

# ================================
# 3️⃣ Distribution of S.S.C (GPA)
# ================================
st.header(" 3️⃣ Distribution of S.S.C (GPA)")

# Create histogram with density (KDE-like) overlay
fig = px.histogram(
    df,
    x='S.S.C (GPA)',
    nbins=10,  # adjust number of bins if needed
    marginal='box',  # adds a small boxplot on top (optional)
    title='Distribution of S.S.C (GPA)',
    opacity=0.8
)

# Add a smooth density curve (KDE) using Plotly's density option
fig.update_traces(marker_line_width=1, marker_l


