# 🧠 Customer Segmentation Dashboard

This project presents an end-to-end customer segmentation workflow using **unsupervised learning (K-Means)**, complete with **exploratory data analysis (EDA)**, **dimensionality reduction**, and a **Streamlit-powered dashboard**. It aims to support marketing and business strategies by identifying distinct customer profiles from demographic and behavioral data.

---

## 📊 Features

- Full exploratory data analysis (EDA)
- K-Means clustering with PCA visualization
- Segment profiling and insight generation
- Interactive Streamlit dashboard
- CSV export of labeled segments

---

## 📁 Project Structure

```
customer-segmentation-dashboard/
├── app.py                         # Streamlit app
├── data/
│   └── customer_segments_labeled.csv  # Input data
├── summary/
│   └── customer_segmentation_summary.md  # Segment descriptions
├── README.md
├── requirements.txt              # Libraries used
└── visuals/
    ├── eda_age_distribution.png
    ├── eda_income_distribution.png
    ├── eda_spending_score.png
    ├── category_distribution.png
    ├── gender_distribution.png
    └── elbow_plot.png
```

---

## 🔍 Exploratory Data Analysis (EDA)

Here are sample EDA plots generated from the dataset:

### Age Distribution
![Age Distribution](visuals/eda_age_distribution.png)

### Income Distribution
![Income Distribution](visuals/eda_income_distribution.png)

### Spending Score Distribution
![Spending Score](visuals/eda_spending_score.png)

### Gender Distribution
![Gender Distribution](visuals/gender_distribution.png)

### Preferred Category Distribution
![Preferred Category](visuals/category_distribution.png)

---

## 🧪 Clustering Process

- **StandardScaler** used for numerical features
- **OneHotEncoding** for categorical features (`gender`, `preferred_category`)
- **PCA** applied for 2D visualization
- **Elbow method** used to find optimal number of clusters
![Elbow Plot](visuals/elbow_plot.png)

---

## 📌 Segment Insights

| Segment | Key Traits                                | Category Focus     | Suggested Strategy                        |
|---------|--------------------------------------------|--------------------|--------------------------------------------|
| 0       | Older, loyal, high spenders                | Home & Garden      | Gardening campaigns, loyalty offers       |
| 1       | Young, mid-income, frequent buyers         | Home & Garden      | Smart home bundles, subscription offers   |
| 2       | Mature, low frequency, sport-focused       | Sports             | Re-engagement emails, loyalty rewards     |
| 3       | Young tech buyers, highest frequency       | Electronics        | VIP access, product pre-launch campaigns  |

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

*(Insert screenshot of the live Streamlit dashboard)*

---

## 📬 Author

Konlavach Mengsuwan  
📧 [YourEmail@example.com]  
🌐 [LinkedIn or Website]  

---

## 📝 License

MIT License
