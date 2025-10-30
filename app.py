import streamlit as st

# Title
st.title("Simple Calculator App")

# Input numbers
num1 = st.number_input("Enter the first number:")
num2 = st.number_input("Enter the second number:")

# Select operation
operation = st.selectbox(
    "Select Operation",
    ("Addition", "Subtraction", "Multiplication", "Division")
)

# Calculate button
if st.button("Calculate"):
    if operation == "Addition":
        result = num1 + num2
    elif operation == "Subtraction":
        result = num1 - num2
    elif operation == "Multiplication":
        result = num1 * num2
    elif operation == "Division":
        if num2 != 0:
            result = num1 / num2
        else:
            result = "Error! Division by zero."
    st.success(f"Result: {result}")
