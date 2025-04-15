# 🧠 Customer Segmentation Dashboard

This project presents an end-to-end customer segmentation analysis using unsupervised machine learning (**K-Means clustering**). It includes a complete exploratory data analysis (EDA), clustering with dimensionality reduction, business insight extraction, and an interactive **Streamlit dashboard**.

---

## 📊 Features

- Detailed exploratory data analysis (EDA)
- Visual insights into customer demographics and behaviors
- K-Means clustering with PCA for dimensionality reduction
- Cluster profiling and business-oriented interpretation
- Interactive dashboard using Streamlit
- Exportable labeled dataset

---

## 📁 Project Structure

```
customer-segmentation-dashboard/
├── app.py
├── data/
│   └── customer_segments_labeled.csv
├── summary/
│   └── customer_segmentation_summary.md
├── visuals/
│   ├── eda_age_distribution.png
│   ├── eda_income_distribution.png
│   ├── eda_spending_score.png
│   ├── gender_distribution.png
│   ├── category_distribution.png
│   ├── income_vs_spending_by_gender.png
│   ├── elbow_plot.png
│   └── pca_cluster_plot.png
├── README.md
└── requirements.txt
```

---

## 🔍 Exploratory Data Analysis (EDA)

### 📈 Age Distribution
![Age Distribution](visuals/eda_age_distribution.png)
- Customers range from early 20s to over 60 years old.
- Slight concentration in the 20–40 age range, important for lifestyle targeting.

### 💰 Income Distribution
![Income Distribution](visuals/eda_income_distribution.png)
- Right-skewed distribution with most customers earning less than 100,000 EUR.
- Helps in designing price tiers and promotional strategies.

### 💳 Spending Score Distribution
![Spending Score](visuals/eda_spending_score.png)
- Bimodal tendency suggests at least two spending behavior types—ideal for clustering.

---

## 🧑‍🤝‍🧑 Categorical Feature Distribution

### 👥 Gender Distribution
![Gender Distribution](visuals/gender_distribution.png)
- A balanced mix of male and female customers.
- A smaller group identifies as "Other".

### 🛍️ Preferred Product Category
![Preferred Product Category](visuals/category_distribution.png)
- Popular categories include Groceries, Clothing, and Electronics.
- Less interest in Automotive and Books—useful for product placement.

---

## 📉 Behavioral Relationship Plots

### 💡 Income vs Spending Score by Gender
![Income vs Spending Score by Gender](visuals/income_vs_spending_by_gender.png)
- Shows that income does not always correlate with spending.
- Some low-income, high-spending customers suggest emotional or urgent purchases.
- Gender-wise behavior is distributed evenly.

---

## 🔢 Optimal Cluster Selection

### 🔍 Elbow Method for K
![Elbow Plot](visuals/elbow_plot.png)
- Elbow occurs around k = 3 or 4.
- We selected **k = 4** for meaningful and interpretable segmentation.

---

## 🎯 Final Clusters

### 📌 Customer Segments Visualized in 2D (PCA)
![PCA Clustering](visuals/pca_cluster_plot.png)
- PCA reduces multi-dimensional data into 2 components.
- Clusters appear well-separated in 2D space, validating K-Means.

---

## 🧪 Segment Profiles & Business Insights

| Cluster | Traits                                     | Top Category      | Gender | Strategy                                    |
|---------|---------------------------------------------|-------------------|--------|---------------------------------------------|
| 0       | Older, loyal, high spenders                 | Home & Garden     | Other  | Gardening campaigns, loyalty offers         |
| 1       | Young, mid-income, frequent buyers          | Home & Garden     | Male   | Smart home bundles, subscription offers     |
| 2       | Mature, lower frequency, sports-focused     | Sports            | Female | Re-engagement emails, loyalty programs      |
| 3       | Young tech-savvy, highest purchase frequency| Electronics       | Male   | Premium products, early access deals        |

---

## ▶️ Run Locally

```bash
git clone https://github.com/your-username/customer-segmentation-dashboard.git
cd customer-segmentation-dashboard
pip install -r requirements.txt
streamlit run app.py
```

---

## 📸 Dashboard Preview

*(Insert screenshot here of Streamlit interface if available)*

---

## 📬 Author

Konlavach Mengsuwan  
📧 [YourEmail@example.com]  
🌐 [LinkedIn or Website]  

---

## 📝 License

MIT License
