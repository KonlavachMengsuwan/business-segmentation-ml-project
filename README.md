# 🧠 Customer Segmentation Dashboard

This project presents a data-driven approach to customer segmentation using K-Means clustering on a synthetic dataset containing demographic and behavioral data of 1,000 customers. The analysis uncovered four distinct customer groups based on key features such as age, income, spending score, product preference, and purchase frequency. The results are visualized using PCA, and an interactive Streamlit dashboard was developed to explore these clusters and their characteristics in a user-friendly way.

---

## 🎯 Objective & Key Findings

- Segment customers into meaningful behavioral groups using unsupervised learning.
- Visualize and analyze consumer patterns based on demographics, income, and spending.
- Develop a Streamlit dashboard to explore and interpret segments interactively.

**Key Insights:**
- High-frequency, tech-savvy buyers prefer electronics and exhibit strong loyalty.
- Older, loyal customers tend to spend more and prefer home & garden categories.
- Spending behavior varies independently of income, highlighting the need for behavioral segmentation.

---

## 🧠 PCA Visualization of Customer Clusters

![11_Customer Segments Visuliazed in 2D (PCA)](https://github.com/user-attachments/assets/39836acf-d1c6-484f-9683-6ddc14e181b9)


Clusters projected onto 2D space using PCA clearly show well-separated customer groups.

---

## 📋 Cluster Summary Table

| Cluster | Avg Age | Income | Spending Score | Top Category | Gender | Strategy |
|---------|---------|--------|----------------|---------------|--------|----------|
| 0       | 56      | 79k    | 49             | Home & Garden | Other  | Loyalty campaigns, home improvement bundles |
| 1       | 30      | 97k    | 48             | Home & Garden | Male   | Smart home marketing, frequent buyer perks |
| 2       | 54      | 97k    | 52             | Sports        | Female | Re-engagement campaigns, seasonal promos   |
| 3       | 33      | 81k    | 52             | Electronics   | Male   | Premium launches, tech-focused ads         |

---

## 🚀 Future Applications

- Personalized marketing and product recommendation systems
- Loyalty program segmentation and optimization
- Informed decisions for market entry and regional promotion
- Targeted communication based on behavioral profiles

---

## 🔮 What Can Be Used in the Future?

- **Real-time segmentation** through CRM or live sales API integrations
- **Predictive models** for assigning new users to segments instantly
- **Cross-platform analytics** combining web, app, email, and purchase data
- **Geographic and seasonal analysis** for tailored promotions

---

## 🔧 Future Improvements

- Incorporate time-series and regional data
- Use alternative clustering models (e.g., DBSCAN, HDBSCAN)
- Add supervised classification for new-customer prediction
- Deploy with database backends and auth for business users

---

## 🔁 Adaptability to Other Use Cases

- 📦 **B2B segmentation** based on revenue, purchase volume
- 🎓 **Student personalization** for EdTech
- 🏥 **Patient clustering** for healthcare resource optimization
- 🛒 **SaaS and subscription modeling** for churn and loyalty analysis
- 🎯 **Donor profiling** in nonprofit and fundraising platforms

---

## 📦 Dataset Preview

| id | age | gender | income | spending_score | membership_years | purchase_frequency | preferred_category | last_purchase_amount |
|----|-----|--------|--------|----------------|-------------------|---------------------|---------------------|----------------------|
| 1  | 38  | Female | 99342  | 90             | 3                 | 24                  | Groceries           | 113.53               |
| 2  | 21  | Female | 78852  | 60             | 2                 | 42                  | Sports              | 41.93                |

---

## 📊 EDA & Clustering with Python

Includes histograms, categorical distributions, scatter plots, and clustering:

- Age, Income, Spending Score Distributions
- Gender and Product Category Distributions
- Income vs Spending Score by Gender
- Elbow Method for Optimal Clusters
- PCA Clustering Results

![1_Distribution of Age](https://github.com/user-attachments/assets/1ee17185-c435-44fa-930a-110ecdea0d3b)
![2_Distribution of income](https://github.com/user-attachments/assets/665a1366-d018-4044-b441-153b84f0ac94)
![3_Distribution of Spending_score](https://github.com/user-attachments/assets/c6baf86a-45ae-4805-9548-ddf835190997)
![4_Distribution of Membership_years](https://github.com/user-attachments/assets/7b074144-20f0-4253-a2e5-5117c0ab0ec6)
![5_Distribution of Purchase_frequency](https://github.com/user-attachments/assets/d2955866-01ca-46d8-b976-36fb7ce5c068)
![6_Distribution of Last_purchase_amount](https://github.com/user-attachments/assets/0105efed-a51b-449b-af1c-42114f4ee1cb)
![7_Gender Distribution](https://github.com/user-attachments/assets/69d0dbe1-4c11-42a2-8759-75340d9a5bbc)
![8_Preferred Product Category Distribution](https://github.com/user-attachments/assets/c9a2822d-60c2-46f5-92db-dd04083d1a29)
![9_Income VS Spending Score By Gender](https://github.com/user-attachments/assets/cf7f4a89-d0b5-4d7f-9798-b6bb369783d7)
![10_Elbow Method for Optimal K](https://github.com/user-attachments/assets/6783f80c-d936-4fad-842c-0952ffd4bab0)

---

## ▶️ Run the App Locally

```bash
git clone https://github.com/KOnlavachMengsuwan/customer-segmentation-dashboard.git
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
