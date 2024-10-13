import streamlit as st

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero is not allowed."
    else:
        return x / y

st.title("Simple Calculator")
st.write("Select operation:")

operation = st.selectbox("Operation", ["Add", "Subtract", "Multiply", "Divide"])

num1 = st.number_input("Enter first number:")
num2 = st.number_input("Enter second number:")

if st.button("Calculate"):
    if operation == "Add":
        st.write("Result:", add(num1, num2))
    elif operation == "Subtract":
        st.write("Result:", subtract(num1, num2))
    elif operation == "Multiply":
        st.write("Result:", multiply(num1, num2))
    elif operation == "Divide":
        st.write("Result:", divide(num1, num2))
