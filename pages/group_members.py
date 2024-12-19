import streamlit as st

def show_page():
    # Display the logo at the top
    st.image("logo.jpeg", width=200)  # Adjust the width as needed

    st.title("Welcome to the Image Processing Application!")
    st.subheader("Final Project Linear Algebra Group 3")
    st.write("### Team Members:")
    st.write("""
    1. Diva Anedtha Pradana Putri - 004202305014
    2. Tegar Hengky Dwi Saputro - 004202305067 (Leader)
    3. Saddam Argyant - 004202305054
    """)

# Call the function to display the page
show_page()
