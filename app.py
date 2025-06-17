import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("laptop_prices.csv")

df["Price"] = df["Price"].str.replace('₹','').str.replace(',','')
df["Price"] = pd.to_numeric(df['Price'],errors= 'coerce')
df.dropna(subset=['Price'])


df["Brand"] = df["Name"].str.split().str[0]



st.title(" Amazon Laptop Tracker")

st.sidebar.header(" Filters")

brands = st.sidebar.multiselect("Select Brands", options=df["Brand"].unique(), default=df["Brand"].unique())
min_price, max_price = st.sidebar.slider("Select Price Range (₹)", 
                                         int(df["Price"].min()), int(df["Price"].max()), 
                                         (int(df["Price"].min()), int(df["Price"].max())))

# Filter data
filtered_df = df[
    (df["Brand"].isin(brands)) & 
    (df["Price"] >= min_price) & 
    (df["Price"] <= max_price)
]

# Show table
st.dataframe(filtered_df[["Date", "Brand", "Name", "Price", "Link"]].reset_index(drop=True))

# Price bar chart
st.subheader("Top 10 Laptops by Price")
top10 = filtered_df.sort_values("Price", ascending=False).head(10)
top10["ShortName"] = top10["Name"].str.slice(0, 40) + "..."

fig, ax = plt.subplots(figsize=(10, 6))
ax.barh(top10["ShortName"], top10["Price"], color="skyblue")
ax.set_xlabel("Price (₹)")
ax.set_ylabel("Laptop")
ax.invert_yaxis()
st.pyplot(fig)