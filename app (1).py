import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="Netflix Dashboard",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Netflix Data Analysis Dashboard")

df = pd.read_csv("netflix_sample.csv")

st.subheader("Dataset Preview")
st.dataframe(df)

st.subheader("Movies vs TV Shows")

type_counts = df["type"].value_counts()

fig, ax = plt.subplots()
ax.bar(type_counts.index, type_counts.values)
ax.set_xlabel("Type")
ax.set_ylabel("Count")
ax.set_title("Movies vs TV Shows")

st.pyplot(fig)

st.subheader("Top Countries")

country_counts = df["country"].value_counts().head(5)

fig2, ax2 = plt.subplots()
ax2.bar(country_counts.index, country_counts.values)
ax2.set_title("Top 5 Countries")

st.pyplot(fig2)
