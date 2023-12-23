import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st

import pandas as pd
summer_product = pd.read_csv("/content/summer-products.csv")
print(summer_product)

st.subheader("Null Values Count")
st.write(summer_product.isnull().sum())

summer_product.dropna(axis=0, inplace=True)
st.write(summer_product)

st.subheader("Grouped Analysis")
grouped_data = summer_product.groupby(by='Model_Product').agg({
    'rating': ['mean', 'max', 'min'],
})
average_rating = summer_product['rating'].mean()
st.write(f"Average Rating: {average_rating}")
summer_product['above_average'] = summer_product['rating'] > average_rating
st.subheader("Data with Rating Above Average")
st.write(summer_product[summer_product['above_average']])
st.write(grouped_data)

average_rating = summer_product['rating'].mean()
above_average_data = summer_product[summer_product['rating'] > average_rating]
merchant_counts = above_average_data['merchant_info_subtitle'].value_counts()
most_positive_merchant = merchant_counts.idxmax()
st.subheader("Most Positive Merchant Info Subtitle")
st.write(f"Subtitle: {most_positive_merchant}")

summer_product["price"] = pd.to_numeric(summer_product["price"], errors='coerce')

summer_product["Model_Product"] = summer_product["Model_Product"].astype('category')
summer_product["rating"] = summer_product["rating"].astype('category')

st.subheader("Visualizations")
fig1, ax1 = plt.subplots(figsize=(12, 6))
sns.stripplot(data=summer_product, x="Model_Product", y="rating", jitter=True, ax=ax1)
plt.title("Distribusi Rating untuk Setiap Model")
plt.xlabel("Model Produk")
plt.ylabel("Rating")

st.pyplot(fig1)

sample_data = summer_product.sample(frac=0.1)

model_rating_units = sample_data.groupby(["Model_Product", "rating"]).agg({
    "units_sold": "sum"
}).reset_index()

fig2, ax2 = plt.subplots(figsize=(12, 6))
sns.barplot(data=model_rating_units, x="Model_Product", y="units_sold", hue="rating", ax=ax2)
plt.title("Jumlah Unit Terjual Berdasarkan Model dan Rating")
plt.xlabel("Model Produk")
plt.ylabel("Jumlah Unit Terjual")
plt.legend(title="Rating", loc="upper right")
plt.xticks(rotation=45, ha="right")

st.subheader("Jumlah Unit Terjual Berdasarkan Model dan Rating")
st.pyplot()