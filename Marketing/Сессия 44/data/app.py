from flask import Flask, request, jsonify
import joblib

app = Flask(__name__)

# Загрузка модели
model = joblib.load("best_model.pkl")

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Получение данных из запроса
        input_data = request.json
        
        # Получение признаков
        feature1 = float(input_data['feature1'])
        feature2 = float(input_data['feature2'])
        feature3 = float(input_data['feature3'])
        feature4 = float(input_data['feature4'])
        feature5 = float(input_data['feature5'])
        feature6 = float(input_data['feature6'])
        
        # Предсказание
        predicted_cost = model.predict([[feature1, feature2, feature3, feature4, feature5, feature6]])[0]
        
        # Формирование ответа
        response = {'predicted_cost': predicted_cost}
        
        return jsonify(response)
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
