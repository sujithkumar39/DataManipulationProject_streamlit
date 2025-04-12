import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("✨ Data Manipulation & Visualization ✨")

upload_file = st.file_uploader("Choose a CSV file", type="csv")
if upload_file is not None:
    df = pd.read_csv(upload_file)
    
    st.header("📄 Data Preview")
    st.write(df)
    st.write("The first five rows are:")
    st.write(df.head(5))
    
    st.write(f"🔢 Number of rows in the CSV file: {df.shape[0]}")
    st.write(f"📏 Number of columns in the CSV file: {df.shape[1]}")
    
    st.write("❌ Number of NULL values in the file:")
    st.write(df.isnull().sum()[df.isnull().sum() > 0])
    
    st.header("📊 Basic Statistics of the Data")
    st.write(df.describe())
    
    st.header("🧬 Datatypes")
    st.write(df.dtypes)
    
    st.header("📈 Data Distribution Pie Chart")
    num_numeric = df.select_dtypes(include='number').shape[1]
    num_non_numeric = df.select_dtypes(exclude='number').shape[1]
    num_null = df.isnull().sum().sum()
    pie_data = [num_numeric, num_non_numeric, num_null]
    pie_labels = ['Numeric Values', 'Non-Numeric Values', 'NULL Values']
    colors = ['#FF9999', '#FFFF99', '#FFCC99']
    fig, ax = plt.subplots()
    ax.pie(pie_data, labels=pie_labels, autopct='%1.1f%%', startangle=90, colors=colors)
    ax.axis('equal')
    st.pyplot(fig)
