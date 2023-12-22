
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st

summer_product = pd.read_csv("summer-products.csv")


st.title("Summer Products Data Analysis Dashboard")
st.dataframe(summer_product)


st.subheader("Null Values Count")
st.write(summer_product.isnull().sum())


summer_product.dropna(axis=0, inplace=True)


st.subheader("Data Summary")
st.write(summer_product.describe(include="all"))


st.subheader("Grouped Analysis")
grouped_data = summer_product.groupby(by='title_orig').agg({
    'rating': ['mean', 'max', 'min'],
})
st.write(grouped_data)

st.subheader("Visualizations")
fig1, ax1 = plt.subplots()
sns.barplot(data=summer_product, x="title_orig", y="price", hue="rating", ax=ax1)
st.pyplot(fig1)

fig2, ax2 = plt.subplots()
sns.barplot(data=summer_product, x="title_orig", y="price", hue="merchant_info_subtitle", ax=ax2)
st.pyplot(fig2)
