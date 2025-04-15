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
![Age Distribution]![1_Distribution of Age](https://github.com/user-attachments/assets/64bc05ce-4a11-45f7-a190-3ade16500045)

- Customers range from early 20s to over 60 years old.
- Slight concentration in the 20–40 age range, important for lifestyle targeting.

### 💰 Income Distribution
![Income Distribution]![2_Distribution of income](https://github.com/user-attachments/assets/e510f0bc-391f-4f3b-80fc-4a178d34ac75)

- Right-skewed distribution with most customers earning less than 100,000 EUR.
- Helps in designing price tiers and promotional strategies.

### 💳 Spending Score Distribution
![Spending Score]![3_Distribution of Spending_score](https://github.com/user-attachments/assets/0282831e-1d0f-4fba-97ca-2d2bf473b2db)

- Bimodal tendency suggests at least two spending behavior types—ideal for clustering.

---

## 🧑‍🤝‍🧑 Categorical Feature Distribution

### 👥 Gender Distribution
![Gender Distribution]![7_Gender Distribution](https://github.com/user-attachments/assets/d304719f-05d7-4684-87aa-638ff3f16260)

- A balanced mix of male and female customers.
- A smaller group identifies as "Other".

### 🛍️ Preferred Product Category
![Preferred Product Category]![8_Preferred Product Category Distribution](https://github.com/user-attachments/assets/7ec1fbad-ac8e-4e4e-aeaa-5d585f8d0c41)

- Popular categories include Groceries, Clothing, and Electronics.
- Less interest in Automotive and Books—useful for product placement.

---

## 📉 Behavioral Relationship Plots

### 💡 Income vs Spending Score by Gender
![Income vs Spending Score by Gender]![9_Income VS Spending Score By Gender](https://github.com/user-attachments/assets/556c1950-1d88-43e6-98e0-3eb304cbe032)

- Shows that income does not always correlate with spending.
- Some low-income, high-spending customers suggest emotional or urgent purchases.
- Gender-wise behavior is distributed evenly.

---

## 🔢 Optimal Cluster Selection

### 🔍 Elbow Method for K
![Elbow Plot]![10_Elbow Method for Optimal K](https://github.com/user-attachments/assets/142c5a89-f08f-40db-821c-35134610daae)

- Elbow occurs around k = 3 or 4.
- We selected **k = 4** for meaningful and interpretable segmentation.

---

## 🎯 Final Clusters

### 📌 Customer Segments Visualized in 2D (PCA)
![PCA Clustering]![11_Customer Segments Visuliazed in 2D (PCA)](https://github.com/user-attachments/assets/9809501e-9813-45d6-9a51-a173c7384899)

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
