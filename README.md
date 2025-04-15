# 🧠 Customer Segmentation Dashboard

This project demonstrates a full customer segmentation workflow using unsupervised machine learning (K-Means), enriched with exploratory data analysis (EDA), dimensionality reduction (PCA), and interactive dashboard deployment via Streamlit.

---

## 📦 Dataset Preview

| id | age | gender | income | spending_score | membership_years | purchase_frequency | preferred_category | last_purchase_amount |
|----|-----|--------|--------|----------------|-------------------|---------------------|---------------------|----------------------|
| 1  | 38  | Female | 99342  | 90             | 3                 | 24                  | Groceries           | 113.53               |
| 2  | 21  | Female | 78852  | 60             | 2                 | 42                  | Sports              | 41.93                |

This dataset contains demographic and purchasing behavior data for 1,000 customers.

---

## 📊 EDA & Clustering with Python

### 1. Age Distribution

```python
sns.histplot(df['age'], kde=True, bins=30)
plt.title('Age Distribution')
```

📌 **Insight:** Customer ages range from early 20s to 60s with a peak around 30–40. Helpful for generational marketing strategies.

![1_Distribution of Age](https://github.com/user-attachments/assets/6c4b9526-facf-462f-a057-cb5ffb7ce9d3)


---

### 2. Income Distribution

```python
sns.histplot(df['income'], kde=True, bins=30)
plt.title('Income Distribution')
```

📌 **Insight:** The distribution is right-skewed. Most customers earn below 100,000 EUR, but some high-income outliers exist.

![2_Distribution of income](https://github.com/user-attachments/assets/a20de3e5-41bc-4ffb-b518-572b4241c7b1)


---

### 3. Spending Score Distribution

```python
sns.histplot(df['spending_score'], kde=True, bins=30)
plt.title('Spending Score Distribution')
```

📌 **Insight:** Spending behavior varies widely. Some customers spend little despite income, suggesting potential for targeting.

![3_Distribution of Spending_score](https://github.com/user-attachments/assets/5bd53495-5fed-418b-b333-a10f6548df1a)


---

### 4. Gender Distribution

```python
sns.countplot(x='gender', data=df)
plt.title('Gender Distribution')
```

📌 **Insight:** Balanced gender distribution with a small group identifying as “Other.” Enables inclusive segmentation.

![7_Gender Distribution](https://github.com/user-attachments/assets/e1cf07e9-d6b3-45f9-b1c1-dd58f727c6fb)


---

### 5. Preferred Product Category

```python
sns.countplot(x='preferred_category', data=df)
plt.title('Preferred Product Category')
plt.xticks(rotation=45)
```

📌 **Insight:** Groceries, Clothing, and Electronics are most popular. Books and Automotive are niche markets.

![8_Preferred Product Category Distribution](https://github.com/user-attachments/assets/32a3887e-ada8-4b6d-89b0-6ba7eb2868c6)


---

### 6. Income vs Spending Score by Gender

```python
sns.scatterplot(data=df, x='income', y='spending_score', hue='gender')
plt.title('Income vs Spending Score by Gender')
```

📌 **Insight:** No strong correlation between income and spending. Some low-income customers spend more than high-income ones.

![9_Income VS Spending Score By Gender](https://github.com/user-attachments/assets/55f2ac99-ed33-4d59-a485-cca936acaf20)


---

### 7. Elbow Method for Optimal Clusters

```python
inertia = []
for k in range(1, 11):
    kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
    kmeans.fit(data_scaled)
    inertia.append(kmeans.inertia_)
```

📌 **Insight:** The elbow point appears at **k = 4**, indicating that four customer segments balance complexity and variance explained.

![10_Elbow Method for Optimal K](https://github.com/user-attachments/assets/b4de1bfe-0e6b-4737-9341-5b1aa5dc2799)


---

### 8. PCA Visualization of Clusters

```python
pca = PCA(n_components=2)
components = pca.fit_transform(data_scaled)
sns.scatterplot(x=components[:, 0], y=components[:, 1], hue=cluster_labels)
```

📌 **Insight:** The PCA projection shows good separation between clusters, validating the K-Means model.

![11_Customer Segments Visuliazed in 2D (PCA)](https://github.com/user-attachments/assets/c4b2df9b-971a-4297-ac1f-ff866e2a447f)

---

## 📋 Cluster Summary Table

| Cluster | Avg Age | Income | Spending Score | Top Category | Gender | Strategy |
|---------|---------|--------|----------------|---------------|--------|----------|
| 0       | 56      | 79k    | 49             | Home & Garden | Other  | Loyalty campaigns, home improvement bundles |
| 1       | 30      | 97k    | 48             | Home & Garden | Male   | Smart home marketing, frequent buyer perks |
| 2       | 54      | 97k    | 52             | Sports        | Female | Re-engagement campaigns, seasonal promos   |
| 3       | 33      | 81k    | 52             | Electronics   | Male   | Premium launches, tech-focused ads         |

---

## ▶️ Run Locally

```bash
git clone https://github.com/KonlavachMengsuwan/customer-segmentation-dashboard.git
cd customer-segmentation-dashboard
pip install -r requirements.txt
streamlit run app.py
```

---

## 📬 Author

Konlavach Mengsuwan  
---

## 📝 License

MIT License
