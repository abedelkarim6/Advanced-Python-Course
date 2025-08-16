import streamlit as st

columns = st.columns(4)

with columns[2] as r:
    st.write("this is the 3rd column in the 1st row")

for cnt, col in enumerate(st.columns(6)):
    col.write(f"this is row 2 column {cnt}")

for cnt, col in enumerate(st.columns([1, 2, 3])):
    col.container(border=True).write(f"this is row 3 with unequal sizes column {cnt}")
