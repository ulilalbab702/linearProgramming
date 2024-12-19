import streamlit as st
import cv2
import numpy as np
from PIL import Image, ImageEnhance

def show_page():
    st.title("Image Processing")
    st.write("Upload an image to apply transformations.")

    uploaded_file = st.file_uploader("Choose an Image", type=["jpg", "png", "jpeg"])

    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image", use_column_width=True)

        # Transformation Options
        st.sidebar.header("Transformations")
        rotation_angle = st.sidebar.slider("Rotation Angle", -180, 180, 0)
        scale_factor = st.sidebar.slider("Scaling Factor", 0.1, 3.0, 1.0)
        brightness_factor = st.sidebar.slider("Brightness", 0.1, 3.0, 1.0)
        shear_factor = st.sidebar.slider("Shear", -50, 50, 0)

        # Apply Transformations
        image_array = np.array(image)
        image_array = cv2.cvtColor(image_array, cv2.COLOR_RGB2BGR)

        # Rotation
        if rotation_angle != 0:
            rows, cols = image_array.shape[:2]
            matrix = cv2.getRotationMatrix2D((cols / 2, rows / 2), rotation_angle, 1)
            image_array = cv2.warpAffine(image_array, matrix, (cols, rows))

        # Scaling
        if scale_factor != 1.0:
            image_array = cv2.resize(image_array, None, fx=scale_factor, fy=scale_factor, interpolation=cv2.INTER_LINEAR)

        # Brightness Adjustment
        image = Image.fromarray(cv2.cvtColor(image_array, cv2.COLOR_BGR2RGB))
        enhancer = ImageEnhance.Brightness(image)
        image = enhancer.enhance(brightness_factor)

        # Display Transformed Image
        st.image(image, caption="Transformed Image", use_column_width=True)
