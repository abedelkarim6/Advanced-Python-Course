import streamlit as st

st.title("Welcome to Python Advanced Course")
st.write("1. Introduction to Python")

columns = st.columns(3)

with columns[0].container(border=True):
    st.image("https://via.placeholder.com/150", caption="Python Logo")

with columns[1].container(border=True):
    st.write("This course will cover advanced topics in Python programming, including:")
    st.write("- Object-Oriented Programming")
    st.write("- Functional Programming")
    st.write("- Error Handling and Exceptions")

with columns[2].container(border=True):
    st.write("By the end of this course, you will be able to:")
    st.write("- Write efficient and clean Python code")
    st.write("- Understand advanced Python concepts")
    st.write("- Apply Python in real-world scenarios")
