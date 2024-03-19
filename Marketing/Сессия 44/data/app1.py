import streamlit as st
import requests

# Заголовок
st.title("Предсказание стоимости")

# Ввод признаков
feature1 = st.number_input("Признак 1", help="Введите значение признака 6")
feature2 = st.number_input("Признак 2", help="Введите значение признака 6")
feature3 = st.number_input("Признак 3", help="Введите значение признака 6")
feature4 = st.number_input("Признак 4", help="Введите значение признака 6")
feature5 = st.number_input("Признак 5", help="Введите значение признака 6")
feature6 = st.number_input("Признак 6", help="Введите значение признака 6")

# Отправка запроса на сервер для предсказания
input_data = {
    "feature1": feature1,
    "feature2": feature2,
    "feature3": feature3,
    "feature4": feature4,
    "feature5": feature5,
    "feature6": feature6
}
response = requests.post("http://127.0.0.1:5000/predict", json=input_data)

# Обработка ответа
if response.status_code == 200:
    result = response.json()
    if "predicted_cost" in result:
        st.success(f"Предполагаемая стоимость: {result['predicted_cost']}")
    elif "error" in result:
        st.error(f"Произошла ошибка: {result['error']}")
else:
    st.error("Произошла ошибка при выполнении запроса")