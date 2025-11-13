from flask import Flask,request,jsonify
import joblib


app = Flask(__name__)
model = joblib.load('model.pkl')

@app.route('/')
def home():
    return "API is running"

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    hours = data['hours']
    prediction = model.predict([['hours']])
    return jsonify({'Predicted:':prediction})

if __name__ == '__main__':
    app.run(host = '0.0.0.0', port=4000)
