# 📦 AI Driven Demand Forecasting & Inventory Optimization System

[![Streamlit App](https://img.shields.io/badge/Live%20App-Open-green?logo=streamlit)](https://ai-retail-demand-forecasting.streamlit.app/)

🚀 Built as part of my Data Science & Analytics learning journey

🔗 **Live Demo:** https://ai-retail-demand-forecasting.streamlit.app/
🔗 **GitHub Repo:** https://github.com/coder-priyanka01/Retail-Demand-Forecasting-Project.git

---

## 📌 Project Overview

This project is an **end-to-end AI-powered demand forecasting system** that predicts future product demand using machine learning and provides actionable insights for inventory planning.

It combines:

* 📊 Data Analysis
* 🤖 Machine Learning
* 🌐 Interactive Web Application (Streamlit)

to help businesses make smarter decisions related to **inventory management and demand prediction**.

---

## 🎯 Objectives

* Predict future product demand
* Optimize inventory levels
* Reduce stock shortages and overstocking
* Enable data-driven decision making

---

## ⚙️ Project Workflow

### 1️⃣ Data Preprocessing

* Handled missing values
* Converted date into useful features (day, month, weekday)
* Created lag features (previous sales)
* Generated rolling averages

---

### 2️⃣ Feature Engineering

* Sales 1 Day Ago
* Sales 7 Days Ago
* 7-Day Rolling Average
* Day, Month, Day of Week

---

### 3️⃣ Model Building

* Algorithm: **Random Forest Regressor**
* Trained on historical sales data

---

### 4️⃣ Model Evaluation

* R² Score
* MAE
* RMSE

---

## 🌐 Streamlit Application Features

### 📊 Dashboard

* Total Orders
* Unique Products
* Country Count

---

### 🔮 Demand Prediction

* Predict future demand based on user inputs
* Provides:

  * Predicted Demand
  * Recommended Inventory
  * Safety Stock

---

### 📈 Sales Analytics

* Country-wise sales visualization

---

### 🧠 Model Insights

* Feature importance chart
* Identifies key demand drivers

---

### 📄 Forecast Report

* Generates downloadable prediction report

---

## 🧰 Tools & Technologies

* Python
* Pandas, NumPy
* Scikit-learn
* Plotly
* Streamlit

---

## 📂 Project Structure

```
├── app.py
├── demand_forecasting_model.pkl
├── model_features.pkl
├── online_retail.csv
├── README.md
```

---

## ▶️ How to Run Locally

```bash
git clone https://github.com/coder-priyanka01/Retail-Demand-Forecasting-Project.git
cd Retail-Demand-Forecasting-Project
pip install -r requirements.txt
streamlit run app.py
```

---

## 📷 App Preview

(Add your screenshot here)

---

## 📊 Key Insights

* Past sales strongly influence demand
* Recent trends (rolling average) are important
* Time-based patterns affect predictions
* Model helps optimize inventory planning

---

## 🚀 Future Improvements

* Deploy on AWS / Cloud
* Improve model accuracy
* Add real-time data integration
* Enhance UI/UX

---

## 🙋‍♀️ Author

**Priyanka Kumari**

---

## ⭐ Support

If you like this project, give it a ⭐ on GitHub!


