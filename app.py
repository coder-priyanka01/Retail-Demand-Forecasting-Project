import streamlit as st
import pandas as pd
import numpy as np
import pickle
import plotly.express as px

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="AI Demand Forecasting Platform",
    page_icon="📦",
    layout="wide"
)

# ---------------- LOAD DATA ----------------
model = pickle.load(open("demand_forecasting_model.pkl","rb"))
features = pickle.load(open("model_features.pkl","rb"))
data = pd.read_csv("online_retail.csv")

# ---------------- SESSION STATE ----------------
if "prediction" not in st.session_state:
    st.session_state.prediction = None

# ---------------- STYLE ----------------
st.markdown("""
<style>

.stApp{
background:linear-gradient(135deg,#0f2027,#203a43,#2c5364);
color:white;
}

.stButton>button{
background:linear-gradient(90deg,#ff7e5f,#feb47b);
color:white;
font-size:18px;
border-radius:10px;
padding:0.6em 1.2em;
}

</style>
""",unsafe_allow_html=True)

# ---------------- SIDEBAR ----------------
st.sidebar.title("📦 AI Demand Forecasting")

st.sidebar.markdown("""
This platform predicts **future product demand** using a trained **Random Forest machine learning model**.

It analyzes historical sales patterns and helps businesses:

• Forecast product demand  
• Plan inventory levels  
• Reduce stock shortages  
• Improve supply chain decisions
""")

page = st.sidebar.radio(
    "Navigation",
    [
        "📊 Dashboard",
        "🔮 Demand Prediction",
        "📈 Sales Analytics",
        "🧠 Model Insights",
        "📄 Forecast Report"
    ]
)

st.sidebar.markdown("---")
st.sidebar.write("Built by **Priyanka**")

# ---------------- DASHBOARD ----------------
if page == "📊 Dashboard":

    st.title("AI Demand Forecasting Dashboard")

    col1,col2,col3 = st.columns(3)

    col1.metric("Total Orders",len(data))
    col2.metric("Unique Products",data["StockCode"].nunique())
    col3.metric("Countries",data["Country"].nunique())

    st.subheader("Dataset Preview")
    st.dataframe(data.head())

# ---------------- DEMAND PREDICTION ----------------
elif page == "🔮 Demand Prediction":

    st.title("Demand Prediction")

    st.write("Enter historical demand values to predict future demand.")

    day = st.slider("Day of Month",1,31,15)
    month = st.slider("Month",1,12,6)
    dow = st.slider("Day of Week",0,6,3)

    lag1 = st.number_input("Sales 1 Day Ago",0.0,10000.0,150.0)
    lag7 = st.number_input("Sales 7 Days Ago",0.0,10000.0,180.0)
    rolling = st.number_input("7 Day Average Sales",0.0,10000.0,170.0)

    if st.button("🚀 Predict Demand"):

        input_data = np.array([[day,month,dow,lag1,lag7,rolling]])

        st.session_state.prediction = model.predict(input_data)[0]

        prediction = st.session_state.prediction

        inventory = prediction*1.25
        safety = prediction*0.2

        c1,c2,c3 = st.columns(3)

        c1.metric("Predicted Demand",f"{prediction:.2f}")
        c2.metric("Recommended Inventory",f"{inventory:.2f}")
        c3.metric("Safety Stock",f"{safety:.2f}")

# ---------------- SALES ANALYTICS ----------------
elif page == "📈 Sales Analytics":

    st.title("Sales Analytics")

    country_sales=data.groupby("Country")["Quantity"].sum().reset_index()

    fig=px.bar(
        country_sales.sort_values("Quantity",ascending=False).head(10),
        x="Country",
        y="Quantity",
        color="Quantity",
        color_continuous_scale="Turbo",
        title="Top Countries by Sales"
    )

    st.plotly_chart(fig,use_container_width=True)

# ---------------- MODEL INSIGHTS ----------------
elif page == "🧠 Model Insights":

    st.title("Key Factors Influencing Product Demand")

    feature_names = {
        "lag_7": "Sales 7 Days Ago",
        "lag_1": "Sales 1 Day Ago",
        "rolling_mean_7": "7-Day Average Sales",
        "day_of_week": "Day of Week",
        "day": "Day of Month",
        "month": "Month"
    }

    importance=model.feature_importances_

    imp_df=pd.DataFrame({
        "Feature":features,
        "Importance":importance
    })

    imp_df["Feature"]=imp_df["Feature"].map(feature_names)

    imp_df=imp_df.sort_values("Importance",ascending=True)

    fig=px.bar(
        imp_df,
        x="Importance",
        y="Feature",
        orientation="h",
        color="Importance",
        color_continuous_scale="plasma",
        title="Key Factors Affecting Product Demand Prediction"
    )

    st.plotly_chart(fig,use_container_width=True)

# ---------------- FORECAST REPORT ----------------
elif page == "📄 Forecast Report":

    st.title("Forecast Report")

    if st.session_state.prediction is not None:

        prediction = st.session_state.prediction

        report=pd.DataFrame({
            "Predicted Demand":[prediction],
            "Recommended Inventory":[prediction*1.25],
            "Safety Stock":[prediction*0.2]
        })

        st.dataframe(report)

        st.download_button(
            "Download Report",
            report.to_csv(index=False),
            "forecast_report.csv"
        )

    else:
        st.info("Go to Demand Prediction page to generate forecast.")

st.markdown("---")
st.write("Built with ❤️ by **Priyanka**")