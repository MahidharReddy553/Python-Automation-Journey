import streamlit as st

def add(a, b): return a + b
def sub(a, b): return a - b
def mul(a, b): return a * b
def div(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Error: Division by zero!"

st.title("🧮 Simple Calculator")

a = st.number_input("Enter value of a:", value=0.0)
b = st.number_input("Enter value of b:", value=0.0)

operation = st.selectbox("Choose operation:", ["Add", "Subtract", "Multiply", "Divide"])

if st.button("Calculate"):
    if operation == "Add":
        st.success(f"Result: {add(a, b)}")
    elif operation == "Subtract":
        st.success(f"Result: {sub(a, b)}")
    elif operation == "Multiply":
        st.success(f"Result: {mul(a, b)}")
    elif operation == "Divide":
        st.success(f"Result: {div(a, b)}")
