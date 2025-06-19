
# streamlit_app.py
import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import pickle

# Load data and model
@st.cache_data
def load_data(csv_path):
    df = pd.read_csv(csv_path)
    # preprocess: fill missing postal codes and drop outliers
    df['Postal Code'].fillna(df['Postal Code'].mode()[0], inplace=True)
    df['Sales_zscore'] = (df['Sales'] - df['Sales'].mean()) / df['Sales'].std()
    df = df[df['Sales_zscore'].abs() <= 3].copy()
    df.rename({"Ship Mode": "Ship_Mode"}, axis=1, inplace=True)
    return df

@st.cache_resource
def load_model(pkl_path):
    with open(pkl_path, 'rb') as f:
        return pickle.load(f)

df = load_data('SALES FORCAST DATSET.csv')
model = load_model('sales_prediction_model.pkl')

st.title("📦 Sales Forecasting App")
st.write("Analyze historical sales and predict future sales based on input features.")

# Sidebar controls
st.sidebar.header("Prediction Input")
Segment = st.sidebar.selectbox("Segment", sorted(df['Segment'].unique()))
Ship_Mode = st.sidebar.selectbox("Ship Mode", sorted(df['Ship_Mode'].unique()))
Category = st.sidebar.selectbox("Category", sorted(df['Category'].unique()))
Region = st.sidebar.selectbox("Region", sorted(df['Region'].unique()))
City = st.sidebar.selectbox("City", sorted(df['City'].unique()))
State = st.sidebar.selectbox("State", sorted(df['State'].unique()))

# Run prediction
if st.sidebar.button("Predict Sales"):
    input_df = pd.DataFrame({
        'Segment': [Segment],
        'Ship_Mode': [Ship_Mode],
        'Category': [Category],
        'Region': [Region],
        'City': [City],
        'State': [State]
    })
    pred = float(model.predict(input_df)[0])
    st.subheader(f"📊 Predicted Sales: ${pred:,.2f}")

st.sidebar.markdown("---")
st.sidebar.header("Explore Data")

# Data visualizations
st.subheader("Historical Ship Mode Usage")
mode_counts = df['Ship_Mode'].value_counts()
fig, ax = plt.subplots()
sns.barplot(x=mode_counts.index, y=mode_counts.values, ax=ax, palette="viridis")
ax.set_ylabel("Count")
ax.set_xlabel("Ship Mode")
st.pyplot(fig)

st.subheader("Revenue by Ship Mode")
mode_sales = df.groupby('Ship_Mode')['Sales'].sum().sort_values(ascending=False)
fig2, ax2 = plt.subplots()
sns.barplot(x=mode_sales.values, y=mode_sales.index, ax=ax2, palette="magma")
ax2.set_xlabel("Total Sales")
st.pyplot(fig2)

st.subheader("Revenue by Segment")
seg_sales = df.groupby('Segment')['Sales'].sum().sort_values(ascending=False)
fig3, ax3 = plt.subplots()
sns.barplot(x=seg_sales.values, y=seg_sales.index, ax=ax3, palette="rocket")
ax3.set_xlabel("Total Sales")
st.pyplot(fig3)

st.subheader("Top Cities by Revenue (Top 10)")
city_sales = df.groupby('City')['Sales'].sum().sort_values(ascending=False).head(10)
fig4, ax4 = plt.subplots(figsize=(8, 4))
sns.barplot(x=city_sales.values, y=city_sales.index, ax=ax4, palette="crest")
ax4.set_xlabel("Total Sales")
st.pyplot(fig4)

# Raw data toggle
with st.expander("See raw data (first 50 rows)"):
    st.dataframe(df.head(50))

st.markdown("---")
st.write("Built with ❤ using Streamlit")

