# 🧠 Customer Segmentation Dashboard

This repository showcases a complete customer segmentation project using unsupervised machine learning (**K-Means clustering**) and Python. It walks through the entire process — from EDA and visualization to clustering and deploying a web dashboard using **Streamlit**.

---

## 📦 Dataset Preview

The dataset includes demographic and behavioral features of 1,000 customers.

| id | age | gender | income | spending_score | membership_years | purchase_frequency | preferred_category | last_purchase_amount |
|----|-----|--------|--------|----------------|-------------------|---------------------|---------------------|----------------------|
| 1  | 38  | Female | 99342  | 90             | 3                 | 24                  | Groceries           | 113.53               |
| 2  | 21  | Female | 78852  | 60             | 2                 | 42                  | Sports              | 41.93                |

---

## 🛠️ Python Code and Visuals

### 1. 📊 Age Distribution

```python
sns.histplot(df['age'], kde=True, bins=30)
plt.title('Age Distribution')
```

![1_Distribution of Age](https://github.com/user-attachments/assets/ef79960a-a219-4a8b-b988-c79b19f6b581)

---

### 2. 💰 Income Distribution

```python
sns.histplot(df['income'], kde=True, bins=30)
plt.title('Income Distribution')
```

![2_Distribution of income](https://github.com/user-attachments/assets/981049bb-9352-425a-b7a9-7b099592f8fc)

---

### 3. 💳 Spending Score Distribution

```python
sns.histplot(df['spending_score'], kde=True, bins=30)
plt.title('Spending Score Distribution')
```

![3_Distribution of Spending_score](https://github.com/user-attachments/assets/b5f7092c-5a5f-4685-baa6-2091297579fa)

---

### 4. 👥 Gender Distribution

```python
sns.countplot(x='gender', data=df)
plt.title('Gender Distribution')
```

![7_Gender Distribution](https://github.com/user-attachments/assets/47dde408-9a6f-49ce-9b0e-754de401aa49)

---

### 5. 🛍️ Preferred Product Category

```python
sns.countplot(x='preferred_category', data=df)
plt.title('Preferred Product Category')
plt.xticks(rotation=45)
```

![8_Preferred Product Category Distribution](https://github.com/user-attachments/assets/d43bbee8-909e-497c-8f15-d95f4a4cb5b6)

---

### 6. 📉 Income vs Spending Score by Gender

```python
sns.scatterplot(data=df, x='income', y='spending_score', hue='gender')
plt.title('Income vs Spending Score by Gender')
```

![9_Income VS Spending Score By Gender](https://github.com/user-attachments/assets/dd8ddb33-e7b5-4120-a4a0-169121812453)

---

### 7. 🔍 Elbow Method for Optimal Clusters (K)

```python
inertia = []
for k in range(1, 11):
    kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
    kmeans.fit(data_scaled)
    inertia.append(kmeans.inertia_)
```

![10_Elbow Method for Optimal K](https://github.com/user-attachments/assets/cd46c2a4-bbf7-4b33-bb89-662ff17c1a0b)

---

### 8. 🧠 Clusters in 2D (PCA)

```python
pca = PCA(n_components=2)
components = pca.fit_transform(data_scaled)
sns.scatterplot(x=components[:, 0], y=components[:, 1], hue=cluster_labels)
```

![11_Customer Segments Visuliazed in 2D (PCA)](https://github.com/user-attachments/assets/37180ecc-d114-4a81-ba98-28059b1499d1)

---

## 📋 Cluster Summary Table

| Cluster | Avg Age | Income | Spending Score | Top Category | Gender |
|---------|---------|--------|----------------|---------------|--------|
| 0       | 56      | 79k    | 49             | Home & Garden | Other  |
| 1       | 30      | 97k    | 48             | Home & Garden | Male   |
| 2       | 54      | 97k    | 52             | Sports        | Female |
| 3       | 33      | 81k    | 52             | Electronics   | Male   |

---

## ▶️ Run the App Locally

```bash
git clone https://github.com/your-username/customer-segmentation-dashboard.git
cd customer-segmentation-dashboard
pip install -r requirements.txt
streamlit run app.py
```

---

## 📬 Author

Konlavach Mengsuwan  
📧 [YourEmail@example.com]  
🌐 [LinkedIn or Website]  

---

## 📝 License

MIT License
