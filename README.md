# Customer-segmentation-using-machine-learning
# 🧠 Customer Segmentation Web App

An interactive Machine Learning web application built with Streamlit that segments customers based on their Annual Income and Spending Score using clustering algorithms.

---

## 📌 Project Overview

Customer Segmentation is an unsupervised machine learning technique used to group customers with similar purchasing behaviors. Businesses can use these insights to design personalized marketing strategies and improve customer engagement.

This application allows users to input customer information and predict the customer segment using clustering algorithms.

---

## 🚀 Features

- Interactive Streamlit Dashboard
- Customer Segment Prediction
- Data Visualization of Clusters
- Multiple Clustering Algorithms
  - K-Means Clustering
  - DBSCAN Clustering
  - Agglomerative Clustering
- Real-time User Input
- Customer Behavior Analysis

---

## 📊 Dataset

This project uses the **Mall Customers Dataset**.

### Features Used

| Feature | Description |
|----------|-------------|
| Annual Income (k$) | Customer's annual income |
| Spending Score (1-100) | Spending behavior score assigned by the mall |

---

## 🛠️ Technologies Used

- Python
- Streamlit
- Pandas
- NumPy
- Matplotlib
- Scikit-Learn
- Joblib

---

## 🤖 Machine Learning Algorithms

### 1. K-Means Clustering

K-Means groups customers into predefined clusters based on similarity.

**Advantages**
- Fast and efficient
- Easy to interpret
- Supports prediction for new customers

---

### 2. DBSCAN

Density-Based Spatial Clustering used to discover clusters and identify outliers.

**Advantages**
- Detects noise/outliers
- Does not require predefined clusters

---

### 3. Agglomerative Clustering

A hierarchical clustering algorithm that merges similar data points into clusters.

**Advantages**
- Creates hierarchical relationships
- Useful for cluster analysis

---

## 📂 Project Structure

```text
customer-segmentation-ml-project/
│
├── app.py
├── Mall_Customers.csv
├── requirements.txt
├── README.md
```
---
## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/Tejaswini-narra/customer-segmentation-ml-project.git
```

### Navigate to Project Folder

```bash
cd customer-segmentation-ml-project
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Application

```bash
streamlit run app.py
```

---

## 📈 Workflow

```text
Load Dataset
      ↓
Data Preprocessing
      ↓
Feature Scaling
      ↓
Train Clustering Models
      ↓
User Input
      ↓
Segment Prediction
      ↓
Cluster Visualization
```

---

## 🎯 Customer Segments

The application identifies customers into segments such as:

- High Income – High Spending
- High Income – Low Spending
- Low Income – High Spending
- Low Income – Low Spending
- Average Customers

These segments help businesses create targeted marketing campaigns.

---
## 🔮 Future Improvements

- Deploy on Streamlit Cloud
- Add Customer Age and Gender Features
- Save Trained Models using Joblib
- Add Cluster Evaluation Metrics
- Implement Customer Recommendation System
- Integrate Real Business Datasets

---

## 📚 Learning Outcomes

Through this project, I gained experience in:

- Unsupervised Machine Learning
- Customer Segmentation
- Data Preprocessing
- Feature Scaling
- Cluster Analysis
- Streamlit Deployment
- Data Visualization
- Machine Learning Model Development

---

## 👩‍💻 Author

**Tejaswini Narra**

Aspiring AI & Machine Learning Engineer

Skills:
- Python
- Machine Learning
- Data Science
- Streamlit
- Scikit-Learn
- SQL
- Generative AI

---

## ⭐ If you found this project useful, please consider giving it a star!
