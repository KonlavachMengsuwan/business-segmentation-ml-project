import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans

# Load dataset
df = pd.read_csv("customer_segmentation_data.csv")

# -------------------
# Exploratory Data Analysis
# -------------------
sns.set(style="whitegrid")

# Numerical columns
numerical_columns = ['age', 'income', 'spending_score', 'membership_years', 'purchase_frequency', 'last_purchase_amount']

# Distribution plots
for col in numerical_columns:
    plt.figure(figsize=(6, 4))
    sns.histplot(df[col], kde=True, bins=30)
    plt.title(f"{col.capitalize()} Distribution")
    plt.tight_layout()
    plt.savefig(f"visuals/eda_{col}_distribution.png")
    plt.close()

# Gender distribution
plt.figure(figsize=(6, 4))
sns.countplot(data=df, x='gender')
plt.title("Gender Distribution")
plt.tight_layout()
plt.savefig("visuals/gender_distribution.png")
plt.close()

# Preferred Category
plt.figure(figsize=(10, 5))
sns.countplot(data=df, x='preferred_category', order=df['preferred_category'].value_counts().index)
plt.xticks(rotation=45)
plt.title("Preferred Product Category")
plt.tight_layout()
plt.savefig("visuals/category_distribution.png")
plt.close()

# Income vs Spending Score by Gender
plt.figure(figsize=(8, 6))
sns.scatterplot(data=df, x='income', y='spending_score', hue='gender')
plt.title("Income vs Spending Score by Gender")
plt.tight_layout()
plt.savefig("visuals/income_vs_spending_by_gender.png")
plt.close()

# -------------------
# Preprocessing
# -------------------
categorical_cols = ['gender', 'preferred_category']
numerical_cols = numerical_columns

preprocessor = ColumnTransformer([
    ('num', StandardScaler(), numerical_cols),
    ('cat', OneHotEncoder(drop='first'), categorical_cols)
])

data_scaled = preprocessor.fit_transform(df)

# -------------------
# Elbow Method
# -------------------
inertia = []
for k in range(1, 11):
    model = KMeans(n_clusters=k, random_state=42, n_init=10)
    model.fit(data_scaled)
    inertia.append(model.inertia_)

plt.figure(figsize=(8, 5))
plt.plot(range(1, 11), inertia, marker='o')
plt.title("Elbow Method for Optimal k")
plt.xlabel("Number of Clusters (k)")
plt.ylabel("Inertia")
plt.tight_layout()
plt.savefig("visuals/elbow_plot.png")
plt.close()

# -------------------
# K-Means Clustering (k=4)
# -------------------
kmeans = KMeans(n_clusters=4, random_state=42, n_init=10)
df['cluster'] = kmeans.fit_predict(data_scaled)

# -------------------
# PCA for 2D Visualization
# -------------------
pca = PCA(n_components=2)
components = pca.fit_transform(data_scaled)
df['PCA1'] = components[:, 0]
df['PCA2'] = components[:, 1]

plt.figure(figsize=(8, 6))
sns.scatterplot(data=df, x='PCA1', y='PCA2', hue='cluster', palette='tab10', s=70)
plt.title("Customer Segments Visualized in 2D (PCA)")
plt.tight_layout()
plt.savefig("visuals/pca_cluster_plot.png")
plt.close()

# -------------------
# Save labeled dataset
# -------------------
df.to_csv("customer_segments_labeled.csv", index=False)