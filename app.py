import streamlit as st
from streamlit_option_menu import option_menu
from pages import group_members, image_processing  # Assuming you create subpages

# Sidebar Navigation Menu
with st.sidebar:
    selected = option_menu(
        menu_title="Navigation", 
        options=["Home", "Image Processing"], 
        icons=["house", "image"],
        menu_icon="cast",
        default_index=0,
    )

if selected == "Home":
    group_members.show_page()  # Group Members Description
elif selected == "Image Processing":
    image_processing.show_page()  # Image Processing Features
