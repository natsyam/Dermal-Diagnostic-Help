import streamlit as st
import requests
from PIL import Image
import io

# Заголовок приложения
st.title("Dermal Diagnostic Help")

# Виджет для загрузки изображения
uploaded_file = st.file_uploader(
    "Загрузите изображение меланомы", type=["jpg", "png", "jpeg"]
)

if uploaded_file is not None:
    # Отображение загруженного изображения
    image = Image.open(uploaded_file)
    st.image(image, caption="Загруженное изображение", use_column_width=True)

    # Кнопка отправки изображения на классификацию
    if st.button("Классифицировать"):
        # Конвертация изображения в байты для отправки на сервер
        files = {"file": (uploaded_file.name, uploaded_file.getvalue())}

        # Попытка отправить изображение на FastAPI сервер
        try:
            # Замените URL на актуальный адрес вашего FastAPI приложения
            response = requests.post("http://localhost:8000/upload/", files=files)

            # Проверка успешного ответа от сервера
            if response.status_code == 200:
                data = response.json()
                class_prediction = data["class_prediction"]
                st.success(f"Классификация: {class_prediction}")
            else:
                st.error("Ошибка на сервере при классификации изображения.")
        except Exception as e:
            st.error(f"Ошибка при отправке изображения: {e}")
else:
    st.warning("Пожалуйста, загрузите изображение.")
