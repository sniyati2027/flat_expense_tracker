# import streamlit as st
# import pandas as pd
# import os

# # ---------- Config ----------
# st.set_page_config(page_title="Flat Expense Tracker", layout="centered")
# st.title("🏠 Shared Flat Expense Tracker")

# st.markdown("""
# <style>
# @import url('https://fonts.googleapis.com/css2?family=Quicksand:wght@500&display=swap');

# html, body, [class*="css"]  {
#     font-family: 'Quicksand', sans-serif;
# }
# </style>
# """, unsafe_allow_html=True)



# # ---------- File ----------
# DATA_FILE = "expenses.csv"

# # ---------- Load or create file ----------
# if not os.path.exists(DATA_FILE):
#     df = pd.DataFrame(columns=["Date", "Description", "Amount", "Paid_By", "Category"])
#     df.to_csv(DATA_FILE, index=False)

# df = pd.read_csv(DATA_FILE)

# # ---------- Add Expense ----------
# st.subheader("➕ Add New Expense")

# with st.form("expense_form"):
#     date = st.date_input("Date")
#     description = st.text_input("Description")
#     amount = st.number_input("Amount (₹)", min_value=0.0, format="%.2f")
#     paid_by = st.selectbox("Paid By", ["Niyati", "Gorika"])
#     category = st.text_input("Category (e.g. Kitchen, Rent, etc.)")
#     submitted = st.form_submit_button("💸 Add Expense")


#     if submitted:
#         new_data = pd.DataFrame([[date, description, amount, paid_by, category]],
#                                 columns=["Date", "Description", "Amount", "Paid_By", "Category"])
#         df = pd.concat([df, new_data], ignore_index=True)
#         df.to_csv(DATA_FILE, index=False)
#         st.success("✅ Expense added successfully!")
#         st.rerun()

# # ---------- Balance Summary ----------
# st.subheader("💰 Balance Summary")

# niyati_paid_total = df[df["Paid_By"] == "Niyati"]["Amount"].sum()
# gorika_paid_total = df[df["Paid_By"] == "Gorika"]["Amount"].sum()

# # Calculate net balance per expense
# niyati_owes = 0
# gorika_owes = 0

# for _, row in df.iterrows():
#     split_amount = row["Amount"] / 2
#     if row["Paid_By"] == "Niyati":
#         gorika_owes += split_amount
#     else:
#         niyati_owes += split_amount

# net_balance = gorika_owes - niyati_owes  # +ve: Gorika owes Niyati, -ve: Niyati owes Gorika

# col1, col2 = st.columns(2)
# col1.metric("Niyati Paid", f"₹{niyati_paid_total:.2f}")
# col2.metric("Gorika Paid", f"₹{gorika_paid_total:.2f}")

# if net_balance > 0:
#     st.info(f"🧾 Gorika owes Niyati ₹{net_balance:.2f}")
# elif net_balance < 0:
#     st.info(f"🧾 Niyati owes Gorika ₹{abs(net_balance):.2f}")
# else:
#     st.success("🎉 You're all settled up!")



# # ---------- All Expenses Table with Delete ----------
# st.subheader("📋 All Expenses")

# if df.empty:
#     st.info("No expenses yet.")
# else:
#     # Table Header
#     header_cols = st.columns([1.5, 3, 1.5, 1.5, 2, 1])
#     headers = ["Date", "Description", "Amount", "Paid By", "Category", "Delete"]
#     for col, header in zip(header_cols, headers):
#         col.markdown(f"**{header}**")

#     # Table Rows
#     for i, row in df.iterrows():
#         cols = st.columns([1.5, 3, 1.5, 1.5, 2, 1])
#         cols[0].write(row["Date"])
#         cols[1].write(row["Description"])
#         cols[2].write(f"₹{row['Amount']:.2f}")
#         cols[3].write(row["Paid_By"])
#         cols[4].write(row["Category"])
#         if cols[5].button("❌", key=f"delete_{i}"):
#             df.drop(index=i, inplace=True)
#             df.reset_index(drop=True, inplace=True)
#             df.to_csv(DATA_FILE, index=False)
#             st.rerun()


# st.markdown("""
# ---
# <div style='text-align: center; font-size: 14px; color: #888'>
#     Made with ❤️ by Niyati & Gorika
# </div>
# """, unsafe_allow_html=True)



#with images


# import streamlit as st
# import pandas as pd
# import os

# # ---------- Page Config ----------
# st.set_page_config(page_title="Flat Expense Tracker", layout="centered")

# # ---------- Theme ----------
# def set_theme(dark_mode=False):
#     if dark_mode:
#         st.markdown("""
#         <style>
#         body, .stApp {
#             background-color: #1c1c1c !important;
#             color: #f2f2f2 !important;
#         }
#         </style>
#         """, unsafe_allow_html=True)
#     else:
#         st.markdown("""
#         <style>
#         body, .stApp, .block-container {
#             background-color: #fff4f6 !important;
#             color: #4B0082 !important;
#             font-family: 'Segoe UI', sans-serif;
#         }
#         h1, h2, h3, label, .css-10trblm, .stMarkdown, .stTextInput>div>div>input {
#             color: #4B0082 !important;
#         }
#         </style>
#         """, unsafe_allow_html=True)



# # ---------- Sidebar ----------
# st.sidebar.markdown("## 🌓 Theme Settings")
# dark_mode = st.sidebar.toggle("Night Mode")
# set_theme(dark_mode)



# # ---------- Title ----------
# st.markdown("<h1 style='text-align: center;'>🏡 Flat Expense Tracker</h1>", unsafe_allow_html=True)
# st.markdown("<div style='text-align: center; font-size: 18px;'>🏙️ Two girls. One city. One cozy home.<br>Tracking memories (and money) — together 💕</div><br>", unsafe_allow_html=True)

# # ---------- Display Image ----------
# from PIL import Image
# import streamlit as st

# # Load the image only once from a fixed path
# img_path = "niyati_gorika.png"  # replace with your image's filename
# img = Image.open(img_path)

# # Display the image on homepage with smaller width and center alignment
# st.markdown("<div style='text-align: center;'>", unsafe_allow_html=True)


# col1, col2, col3 = st.columns([1, 2, 1])
# with col2:
#     st.image(img, caption="Niyati & Gorika 💖", width=350)



# # ---------- Data Handling ----------
# DATA_FILE = "expenses.csv"
# if not os.path.exists(DATA_FILE):
#     df = pd.DataFrame(columns=["Date", "Description", "Amount", "Paid_By", "Category"])
#     df.to_csv(DATA_FILE, index=False)

# df = pd.read_csv(DATA_FILE)

# # ---------- Add Expense ----------
# st.subheader("🍽️🧴 Add a New Expense")
# with st.form("expense_form"):
#     date = st.date_input("Date")
#     description = st.text_input("Description")
#     amount = st.number_input("Amount (₹)", min_value=0.0, format="%.2f")
#     paid_by = st.selectbox("Paid By", ["Niyati", "Gorika"])
#     category = st.text_input("Category (e.g. Kitchen, Rent, etc.)")
#     submitted = st.form_submit_button("💸 Add Expense")

#     if submitted:
#         new_data = pd.DataFrame([[date, description, amount, paid_by, category]],
#                                 columns=["Date", "Description", "Amount", "Paid_By", "Category"])
#         df = pd.concat([df, new_data], ignore_index=True)
#         df.to_csv(DATA_FILE, index=False)
#         st.success("✅ Expense added successfully!")
#         st.rerun()

# # ---------- Balance Summary ----------
# st.subheader("🧾💞 Balance Summary")

# niyati_paid_total = df[df["Paid_By"] == "Niyati"]["Amount"].sum()
# gorika_paid_total = df[df["Paid_By"] == "Gorika"]["Amount"].sum()

# niyati_owes = 0
# gorika_owes = 0

# for _, row in df.iterrows():
#     split_amount = row["Amount"] / 2
#     if row["Paid_By"] == "Niyati":
#         gorika_owes += split_amount
#     else:
#         niyati_owes += split_amount

# net_balance = gorika_owes - niyati_owes

# col1, col2 = st.columns(2)
# col1.metric("Niyati Paid", f"₹{niyati_paid_total:.2f}")
# col2.metric("Gorika Paid", f"₹{gorika_paid_total:.2f}")

# if net_balance > 0:
#     st.info(f"🌸 Gorika owes Niyati ₹{net_balance:.2f}")
# elif net_balance < 0:
#     st.info(f"🌼 Niyati owes Gorika ₹{abs(net_balance):.2f}")
# else:
#     st.success("🎉 You're all settled up!")

# # ---------- All Expenses ----------
# st.subheader("📔🧺 All Shared Moments (Expenses)")

# if df.empty:
#     st.info("No expenses yet.")
# else:
#     header_cols = st.columns([1.5, 3, 1.5, 1.5, 2, 1])
#     headers = ["Date", "Description", "Amount", "Paid By", "Category", "Delete"]
#     for col, header in zip(header_cols, headers):
#         col.markdown(f"**{header}**")

#     for i, row in df.iterrows():
#         cols = st.columns([1.5, 3, 1.5, 1.5, 2, 1])
#         cols[0].write(row["Date"])
#         cols[1].write(row["Description"])
#         cols[2].write(f"₹{row['Amount']:.2f}")
#         cols[3].write(row["Paid_By"])
#         cols[4].write(row["Category"])
#         if cols[5].button("❌", key=f"delete_{i}"):
#             df.drop(index=i, inplace=True)
#             df.reset_index(drop=True, inplace=True)
#             df.to_csv(DATA_FILE, index=False)
#             st.rerun()

# # ---------- Footer ----------
# st.markdown("""
# ---
# <div style='text-align: center; font-size: 14px; color: #888'>
#     Made with love by Niyati 
# </div>
# """, unsafe_allow_html=True)

#final on phone changes

import streamlit as st
import pandas as pd
import os
from PIL import Image

# ---------- Page Config ----------
st.set_page_config(page_title="Flat Expense Tracker", layout="centered")

# ---------- Theme ----------
def set_theme(dark_mode=False):
    if dark_mode:
        st.markdown("""
        <style>
        body, .stApp {
            background-color: #1c1c1c !important;
            color: #f2f2f2 !important;
        }
        </style>
        """, unsafe_allow_html=True)
    else:
        st.markdown("""
        <style>
        body, .stApp, .block-container {
            background-color: #fff4f6 !important;
            color: #4B0082 !important;
            font-family: 'Segoe UI', sans-serif;
        }
        h1, h2, h3, label, .css-10trblm, .stMarkdown, .stTextInput>div>div>input {
            color: #4B0082 !important;
        }
        </style>
        """, unsafe_allow_html=True)

# ---------- Sidebar ----------
st.sidebar.markdown("## 🌓 Theme Settings")
dark_mode = st.sidebar.toggle("Night Mode")
set_theme(dark_mode)

# ---------- Title ----------
st.markdown("<h1 style='text-align: center;'>🏡 Flat Expense Tracker</h1>", unsafe_allow_html=True)
st.markdown("<div style='text-align: center; font-size: 18px;'>🏙️ Two girls. One city. One cozy home.<br>Tracking memories (and money) — together 💕</div><br>", unsafe_allow_html=True)

# ---------- Display Image ----------
img_path = "niyati_gorika.png"  # Replace with your image filename
if os.path.exists(img_path):
    img = Image.open(img_path)
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.image(img, caption="Niyati & Gorika 💖", width=350)
else:
    st.warning("📸 Image not found. Please place 'niyati_gorika.png' in the app directory.")

# ---------- Data Handling ----------
DATA_FILE = "expenses.csv"
if not os.path.exists(DATA_FILE):
    df = pd.DataFrame(columns=["Date", "Description", "Amount", "Paid_By", "Category"])
    df.to_csv(DATA_FILE, index=False)

df = pd.read_csv(DATA_FILE)

# ---------- Add Expense ----------
st.subheader("🍽️🧴 Add a New Expense")
with st.form("expense_form"):
    date = st.date_input("Date")
    description = st.text_input("Description")
    amount = st.number_input("Amount (₹)", min_value=0.0, format="%.2f")
    paid_by = st.selectbox("Paid By", ["Niyati", "Gorika"])
    category = st.text_input("Category (e.g. Kitchen, Rent, etc.)")
    submitted = st.form_submit_button("💸 Add Expense")

    if submitted:
        new_data = pd.DataFrame([[date, description, amount, paid_by, category]],
                                columns=["Date", "Description", "Amount", "Paid_By", "Category"])
        df = pd.concat([df, new_data], ignore_index=True)
        df.to_csv(DATA_FILE, index=False)
        st.success("✅ Expense added successfully!")
        st.rerun()

# ---------- Balance Summary ----------
st.subheader("🧾💞 Balance Summary")

niyati_paid_total = df[df["Paid_By"] == "Niyati"]["Amount"].sum()
gorika_paid_total = df[df["Paid_By"] == "Gorika"]["Amount"].sum()

niyati_owes = 0
gorika_owes = 0

for _, row in df.iterrows():
    split_amount = row["Amount"] / 2
    if row["Paid_By"] == "Niyati":
        gorika_owes += split_amount
    else:
        niyati_owes += split_amount

net_balance = gorika_owes - niyati_owes

col1, col2 = st.columns(2)
col1.metric("Niyati Paid", f"₹{niyati_paid_total:.2f}")
col2.metric("Gorika Paid", f"₹{gorika_paid_total:.2f}")

if net_balance > 0:
    st.info(f"🌸 Gorika owes Niyati ₹{net_balance:.2f}")
elif net_balance < 0:
    st.info(f"🌼 Niyati owes Gorika ₹{abs(net_balance):.2f}")
else:
    st.success("🎉 You're all settled up!")

# ---------- All Expenses ----------
st.subheader("📔🧺 All Shared Moments (Expenses)")

if df.empty:
    st.info("No expenses yet.")
else:
    header_cols = st.columns([1.5, 3, 1.5, 1.5, 2, 1])
    headers = ["Date", "Description", "Amount", "Paid By", "Category", "Delete"]
    for col, header in zip(header_cols, headers):
        col.markdown(f"**{header}**")

    for i, row in df.iterrows():
        cols = st.columns([1.5, 3, 1.5, 1.5, 2, 1])
        cols[0].write(row["Date"])
        cols[1].write(row["Description"])
        cols[2].write(f"₹{row['Amount']:.2f}")
        cols[3].write(row["Paid_By"])
        cols[4].write(row["Category"])
        if cols[5].button("❌", key=f"delete_{i}"):
            df.drop(index=i, inplace=True)
            df.reset_index(drop=True, inplace=True)
            df.to_csv(DATA_FILE, index=False)
            st.rerun()

# ---------- Footer ----------
st.markdown("""
---
<div style='text-align: center; font-size: 14px; color: #888'>
    Made with love by Niyati 💜
</div>
""", unsafe_allow_html=True)
