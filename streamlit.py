import streamlit as st
from PIL import Image

st.title("Dermal diagnostic help")

# Загрузка фотографии
uploaded_file = st.file_uploader("Выберите файл", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Чтение и отображение фотографии
    image = Image.open(uploaded_file)
    st.image(image, caption="Загруженная фотография", use_column_width=True)
