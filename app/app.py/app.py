import streamlit as st
import numpy as np
import pandas as pd
import joblib
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans, DBSCAN, AgglomerativeClustering
from sklearn.preprocessing import StandardScaler

# -------------------------------
# Title
# -------------------------------
st.title("🧠 Customer Segmentation Web App")

st.write("Enter customer details and select a model to predict the segment.")

# -------------------------------
# Load Dataset
# -------------------------------
df = pd.read_csv("C:/Users/91868/Desktop/customer-segmentation-ml-project/app/app.py/Mall_Customers.csv")
X = df[['Annual Income (k$)', 'Spending Score (1-100)']]

# -------------------------------
# Preprocessing
# -------------------------------
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# -------------------------------
# Train Models (for demo purpose)
# -------------------------------
kmeans = KMeans(n_clusters=5, random_state=42)
kmeans.fit(X_scaled)

dbscan = DBSCAN(eps=0.5, min_samples=5)
dbscan.fit(X_scaled)

agglo = AgglomerativeClustering(n_clusters=5)
agglo_labels = agglo.fit_predict(X_scaled)

# -------------------------------
# User Input
# -------------------------------
st.sidebar.header("User Input")

income = st.sidebar.slider("Annual Income (k$)", 10, 150, 50)
score = st.sidebar.slider("Spending Score (1-100)", 1, 100, 50)

model_choice = st.sidebar.selectbox(
    "Select Model",
    ["KMeans", "DBSCAN", "Agglomerative"]
)

# -------------------------------
# Prediction
# -------------------------------
if st.sidebar.button("Predict"):

    user_data = np.array([[income, score]])
    user_scaled = scaler.transform(user_data)

    if model_choice == "KMeans":
        cluster = kmeans.predict(user_scaled)[0]

    elif model_choice == "DBSCAN":
        cluster = dbscan.fit_predict(user_scaled)[0]

    elif model_choice == "Agglomerative":
        # Agglomerative doesn't support predict
        cluster = "Not Supported"

    
    # -------------------------------
    cluster_means = {
    0: "Low Income - Low Spending",
    1: "High Income - High Spending",
    2: "High Income - Low Spending",
    3: "Low Income - High Spending",
    4: "Average Customer"
}
    # Output
    # -------------------------------
    st.subheader("🔍 Prediction Result")
    st.write("Cluster:", cluster)
    st.write(cluster_means.get(int(cluster), "Unknown"))

# -------------------------------
# Visualization
# -------------------------------
st.subheader("📊 Data Visualization")

fig, ax = plt.subplots()

labels = kmeans.predict(X_scaled)

ax.scatter(X_scaled[:, 0], X_scaled[:, 1], c=labels)
ax.set_xlabel("Income")
ax.set_ylabel("Spending")

st.pyplot(fig)