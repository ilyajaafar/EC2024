import streamlit as st
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(
    page_title="Scientific Visualization"
)

st.header("Scientific Visualization", divider="gray")

# --- Start of Streamlit App ---

st.title("Gender Distribution Analysis")
st.subheader("Distribution of Gender in Arts Faculty")

# NOTE: In a real application, you would load your 'df' DataFrame here.
# For demonstration, we'll create a dummy DataFrame that matches the structure 
# the original code expects (columns 'Faculty' and 'Gender').

data = {
    'Faculty': ['Arts'] * 50 + ['Science'] * 50,
    'Gender': ['Female'] * 30 + ['Male'] * 20 + ['Female'] * 15 + ['Male'] * 35
}
df = pd.DataFrame(data)
# --------------------------------------------------------------------------


# 1. Data Filtering
arts_df = df[df['Faculty'] == 'Arts'].copy() # Filter for Arts faculty and create a copy

# 2. Count Calculation
gender_counts = arts_df['Gender'].value_counts()

# 3. Matplotlib Figure Generation
# Create the figure object explicitly to pass to st.pyplot()
fig, ax = plt.subplots(figsize=(6, 6))

ax.pie(
    gender_counts, 
    labels=gender_counts.index, 
    autopct='%1.1f%%', 
    startangle=90
)

ax.set_title('Distribution of Gender in Arts Faculty')
ax.axis('equal') # Equal aspect ratio ensures that pie is drawn as a circle.


# 4. Streamlit Display
st.pyplot(fig)

# --- Start of Streamlit App ---

st.title("Gender Distribution Analysis")
st.subheader("Count Plot of Gender")

# NOTE: In a real application, you would load your 'df' DataFrame here.
# For demonstration, we'll create a dummy DataFrame that matches the structure 
# the original code expects (column 'Gender').

data = {
    'Gender': ['Female'] * 60 + ['Male'] * 40 + ['Other'] * 5,
    'Age': [20] * 105
}
df = pd.DataFrame(data)
# --------------------------------------------------------------------------


# 1. Matplotlib Figure Generation
# Create the figure and axes objects explicitly to pass the figure to st.pyplot()
fig, ax = plt.subplots(figsize=(8, 6))

# Use Seaborn to create the count plot on the defined axes (ax)
sns.countplot(data=df, x='Gender', ax=ax)

# Set the title and labels using Matplotlib's axes object
ax.set_title('Distribution of Gender')
ax.set_xlabel('Gender')
ax.set_ylabel('Count')


# 2. Streamlit Display
st.pyplot(fig)
