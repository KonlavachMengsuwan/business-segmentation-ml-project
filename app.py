import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
from sklearn.compose import ColumnTransformer

# Load dataset
@st.cache_data
def load_data():
    return pd.read_csv("data/customer_segments_labeled.csv")

# Preprocess data
def preprocess_data(df):
    categorical_cols = ['gender', 'preferred_category']
    numerical_cols = ['age', 'income', 'spending_score', 'membership_years', 'purchase_frequency', 'last_purchase_amount']
    
    preprocessor = ColumnTransformer([
        ('num', StandardScaler(), numerical_cols),
        ('cat', OneHotEncoder(drop='first'), categorical_cols)
    ])
    
    return preprocessor.fit_transform(df)

# Dimensionality reduction
def run_pca(data):
    pca = PCA(n_components=2, random_state=42)
    return pca.fit_transform(data)

# Streamlit layout
st.set_page_config(page_title="Customer Segmentation Dashboard", layout="wide")
st.title("🧠 Customer Segmentation Dashboard")

df = load_data()
st.sidebar.header("About")
st.sidebar.info("This dashboard presents customer segments based on demographic and behavioral data. Segmentation was performed using K-Means clustering.")

# Show raw data
if st.checkbox("Show raw data"):
    st.subheader("Raw Data")
    st.write(df.head())

# PCA Visualization
st.subheader("🧠 Customer Segments Visualized in 2D (PCA)")
processed_data = preprocess_data(df)
reduced_data = run_pca(processed_data)
df['PCA1'] = reduced_data[:, 0]
df['PCA2'] = reduced_data[:, 1]

fig, ax = plt.subplots(figsize=(10, 6))
sns.scatterplot(data=df, x='PCA1', y='PCA2', hue='cluster', palette='tab10', s=70, ax=ax)
plt.title("Customer Segments in 2D")
st.pyplot(fig)

# Cluster profile
st.subheader("📋 Cluster Summary Table")
profile_cols = ['age', 'income', 'spending_score', 'membership_years', 'purchase_frequency', 'last_purchase_amount']
summary = df.groupby('cluster')[profile_cols].mean().round(1)
summary['Top Category'] = df.groupby('cluster')['preferred_category'].agg(lambda x: x.mode()[0])
summary['Gender'] = df.groupby('cluster')['gender'].agg(lambda x: x.mode()[0])
st.dataframe(summary)

# Download segmented data
csv = df.to_csv(index=False).encode('utf-8')
st.download_button(
    label="📥 Download Segmented Dataset",
    data=csv,
    file_name='customer_segments_labeled.csv',
    mime='text/csv'
)

st.markdown("---")
st.caption("Developed by Konlavach Mengsuwan • Built with Streamlit")