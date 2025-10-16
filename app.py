import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np # Used for creating sample data
st.set_page_config(
    page_title="Scientific Visualization"
)

st.header("Scientific Visualization", divider="gray")


# --- Streamlit Application Start ---

# Set page configuration for a wider layout
st.set_page_config(layout="wide", page_title="Student Data Analysis Dashboard")
st.title("📊 Student Enrollment and Academic Performance Analysis")

# --- 1. Create a Sample DataFrame (Assuming your 'df' is loaded here) ---
# Replace this section with your actual data loading (e.g., df = pd.read_csv('your_data.csv'))
@st.cache_data
def load_data():
    np.random.seed(42)
    data = {
        'Faculty': np.random.choice(['Arts', 'Science', 'Engineering', 'Commerce'], 500, p=[0.4, 0.3, 0.2, 0.1]),
        'Gender': np.random.choice(['Male', 'Female', 'Other'], 500, p=[0.45, 0.50, 0.05]),
        'Bachelor Academic Year in EU': np.random.randint(1, 5, 500),
        'S.S.C (GPA)': np.round(np.random.normal(4.2, 0.5, 500), 1)
    }
    df_ = pd.DataFrame(data)
    # Ensure GPA is capped
    df_['S.S.C (GPA)'] = df_['S.S.C (GPA)'].apply(lambda x: min(5.0, max(3.0, x)))
    return df_

df = load_data()

# --- 2. Distribution of Gender in Arts Faculty (Bar & Pie) ---

st.header("1. Arts Faculty Gender Breakdown")
st.markdown("Analyzing gender distribution specifically within the **Arts** faculty.")

arts_df = df[df['Faculty'] == 'Arts'].copy()
col1, col2 = st.columns(2)

with col1:
    st.subheader('Bar Chart: Gender Counts')
    gender_counts = arts_df['Gender'].value_counts().reset_index()
    gender_counts.columns = ['Gender', 'Count']
    fig_bar = px.bar(
        gender_counts, x='Gender', y='Count', title='Gender Distribution in Arts Faculty',
        color='Gender', text='Count'
    )
    st.plotly_chart(fig_bar, use_container_width=True)

with col2:
    st.subheader('Pie Chart: Gender Proportion')
    fig_pie = px.pie(
        arts_df, names='Gender', title='Gender Proportion in Arts Faculty', hole=0.3
    )
    st.plotly_chart(fig_pie, use_container_width=True)

# --- 3. Distribution of Bachelor Academic Year (Horizontal Bar & Pie) ---

st.header("2. Bachelor Academic Year Distribution")
st.markdown("Visualizing student enrollment across academic years in the EU program.")

bachelor_academic_year_counts = df['Bachelor Academic Year in EU'].value_counts().sort_index().reset_index()
bachelor_academic_year_counts.columns = ['Academic_Year', 'Count']

col3, col4 = st.columns(2)

with col3:
    st.subheader('Horizontal Bar: Year Counts')
    fig_bar_year = px.bar(
        bachelor_academic_year_counts, x='Count', y='Academic_Year', orientation='h',
        title='Distribution of Bachelor Academic Year', text='Count', color='Academic_Year'
    )
    # Ensure years are ordered correctly on the Y-axis
    fig_bar_year.update_layout(yaxis={'categoryorder':'total ascending'})
    st.plotly_chart(fig_bar_year, use_container_width=True)

with col4:
    st.subheader('Pie Chart: Year Proportion')
    fig_pie_year = px.pie(
        df, names='Bachelor Academic Year in EU', title='Distribution of Bachelor Academic Year'
    )
    st.plotly_chart(fig_pie_year, use_container_width=True)

# --- 4. Distribution of S.S.C (GPA) (Line Plot) ---

st.header("3. S.S.C (GPA) Performance")
st.markdown("Tracking the frequency of different S.S.C (GPA) scores.")

# Calculate counts and sort by GPA
ssc_gpa_counts = df['S.S.C (GPA)'].value_counts().sort_index().reset_index()
ssc_gpa_counts.columns = ['GPA', 'Count']

st.subheader('Line Plot: S.S.C (GPA) Distribution')
fig_line = px.line(
    ssc_gpa_counts, x='GPA', y='Count', title='Distribution of S.S.C (GPA)', markers=True
)

# Apply styling for better readability (similar to the Matplotlib grid)
fig_line.update_traces(mode='lines+markers', line={'shape': 'linear'})
fig_line.update_xaxes(showgrid=True, tickangle=45)
fig_line.update_yaxes(showgrid=True)

st.plotly_chart(fig_line, use_container_width=True)
st.plotly_chart(fig_pie, use_container_width=True
