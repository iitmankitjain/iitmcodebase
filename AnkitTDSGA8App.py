import streamlit as st


def main():
    st.title("Find the largest of 3 numbers")

    a = st.number_input("Enter First Number:")
    b = st.number_input("Enter Second Number:")
    c = st.number_input("Enter Third Number:")

    if st.button("Largest"):
        largest = max(a, b, c)
        st.write("The largest number is: {}".format(largest))


if __name__ == "__main__":
    main()
