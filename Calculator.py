import streamlit as st

st.title('Hi This Calculator is Made by Kamil Kamran from Batch 15')

def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    if num2 == 0:
        return "Error! Division by zero."
    else:
        return num1 / num2

def main():
    st.title("GUI Calculator")

    num1 = st.number_input("Enter the first number:")
    num2 = st.number_input("Enter the second number:")

    operation = st.radio("Select an operation:", ("Addition", "Subtraction", "Multiplication", "Division"))

    result = 0

    if operation == "Addition":
        result = add(num1, num2)
    elif operation == "Subtraction":
        result = subtract(num1, num2)
    elif operation == "Multiplication":
        result = multiply(num1, num2)
    elif operation == "Division":
        result = divide(num1, num2)

    st.write(f"Result: {result}")

if __name__ == "__main__":
    main()