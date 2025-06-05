import streamlit as st
import pandas as pd
from datetime import date
import os

FILE = 'Niyati.csv'  # 👈 Your personal file

st.title("🧍‍♀️ Niyati's Personal Expenses")

# Load or initialize the file
if not os.path.exists(FILE) or os.stat(FILE).st_size == 0:
    df = pd.DataFrame(columns=["date", "item", "amount", "category"])
    df.to_csv(FILE, index=False)
else:
    df = pd.read_csv(FILE)

# Add new expense
with st.form("add_expense"):
    st.subheader("Add New Expense")
    d = st.date_input("Date", date.today())
    item = st.text_input("Item")
    amount = st.number_input("Amount (₹)", min_value=0.0, step=1.0)
    category = st.text_input("Category (e.g., Snacks, Travel, Shopping)")
    submitted = st.form_submit_button("Add Expense")

    if submitted and item and amount:
        new_data = pd.DataFrame([[d, item, amount, category]], columns=["date", "item", "amount", "category"])
        df = pd.concat([df, new_data], ignore_index=True)
        df.to_csv(FILE, index=False)
        st.success("Expense added!")

# Show all
st.subheader("My Expenses")
st.dataframe(df)

# Summary
if not df.empty:
    st.subheader("Summary by Category")
    summary = df.groupby('category')['amount'].sum().sort_values(ascending=False)
    st.dataframe(summary)
    st.bar_chart(summary)
