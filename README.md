
# 🧠 Customer Segmentation Dashboard

This project is a **Streamlit-powered web dashboard** for customer segmentation using unsupervised learning (K-Means clustering). It segments users based on demographic and behavioral features to help businesses identify target customer groups, enhance personalization, and support strategic decision-making.

---

## 📊 Features

- Upload and visualize customer data
- Automatically segment customers using K-Means
- View clusters in 2D using PCA projection
- Interactive cluster profile table
- Download segmented dataset as CSV

---

## 📁 Project Structure

```
customer-segmentation-app/
├── app.py                         # Streamlit app
├── data/
│   └── customer_segments_labeled.csv  # Input data
├── summary/
│   └── customer_segmentation_summary.md  # Segment descriptions
├── README.md
├── requirements.txt              # Libraries used
└── visuals/
    └── elbow_plot.png            # Optional elbow plot
```

---

## 🔍 Data Description

Sample dataset includes the following fields:
- `age`
- `gender`
- `income`
- `spending_score`
- `membership_years`
- `purchase_frequency`
- `last_purchase_amount`
- `preferred_category`

---

## 📌 How to Run Locally

1. Clone this repository:
```bash
git clone https://github.com/your-username/customer-segmentation-app.git
cd customer-segmentation-app
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the app:
```bash
streamlit run app.py
```

---

## 💡 Cluster Insights Example

| Segment | Key Traits                                | Category Focus     | Suggested Strategy                        |
|---------|--------------------------------------------|--------------------|--------------------------------------------|
| 0       | Older, loyal, high spenders                | Home & Garden      | Gardening campaigns, loyalty offers       |
| 1       | Young, mid-income, frequent buyers         | Home & Garden      | Smart home bundles, subscription offers   |
| 2       | Mature, low frequency, sport-focused       | Sports             | Re-engagement emails, loyalty rewards     |
| 3       | Young tech buyers, highest frequency       | Electronics        | VIP access, product pre-launch campaigns  |

---

## 📸 Screenshots

*(Add screenshots of the app interface here)*

---

## 📬 Contact

Konlavach Mengsuwan  
📧 [YourEmail@example.com]  
🌐 [LinkedIn or Website]  

---

## 📝 License

MIT License
