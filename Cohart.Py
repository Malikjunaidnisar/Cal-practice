import streamlit as st

def calculate(operator, num1, num2):
    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    elif operator == "*":
        return num1 * num2
    elif operator == "/":
        if num2   ￼
 == 0:
            return "Cannot divide by zero"
        return num1 / num2
    else:
        return "Invalid operator"   ￼


def main():
    st.title("Simple Calculator")

    num1 = st.number_input("Enter the first number")
    operator = st.selectbox("Select an operator", ["+", "-", "*", "/"])
    num2 = st.number_input("Enter the second number")

    if st.button("Calculate"):
        result = calculate(operator, num1, num2)
        st.success(f"Result: {result}")

if __name__ == "__main__":
    main()
