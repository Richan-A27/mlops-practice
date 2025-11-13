from flask import Flask, request, jsonify, render_template_string
import joblib

app = Flask(__name__)
model = joblib.load('model.pkl')

# html
FORM_HTML = """
<!DOCTYPE html>
<html>
<head><title>Marks Predictor</title></head>
<body>
    <h2>Predict Marks</h2>
    <form method="POST" action="/predict">
        Enter Hours Studied: <input type="number" name="hours" required>
        <button type="submit">Predict</button>
    </form>
</body>
</html>
"""

@app.route('/')
def home():
    return "API is running"

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    # Case 1: Browser GET request → show HTML form
    if request.method == 'GET':
        return FORM_HTML

    # Case 2: Form POST request
    if request.form.get("hours"):
        hours = float(request.form.get("hours"))
        prediction = model.predict([[hours]])[0]
        return f"<h2>Predicted Marks: {prediction}</h2>"

    # Case 3: JSON request
    data = request.get_json(silent=True)
    if data and "hours" in data:
        hours = float(data["hours"])
        prediction = model.predict([[hours]])[0]
        return jsonify({"Predicted Marks": prediction})

    # If nothing valid was sent
    return "Please send JSON: {'hours': 5} OR use the form.", 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4000)
