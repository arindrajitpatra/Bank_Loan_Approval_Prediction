from flask import Flask, request, render_template, jsonify
import pickle

app = Flask(__name__)

try:
    with open('knn_model.pkl', 'rb') as model_file:
        model = pickle.load(model_file)
except Exception as e:
    print(f"Error loading the model: {e}")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    features = [
        int(data['age']),
        int(data['income']),
        int(data['family']),
        float(data['ccavg']),
        int(data['education']),
        float(data['mortgage']),
        1 if data['securities_account'] == 'yes' else 0,
        1 if data['cd_account'] == 'yes' else 0,
        1 if data['online'] == 'yes' else 0,
        1 if data['creditcard'] == 'yes' else 0
    ]

    try:
        prediction = model.predict([features])[0]
        result = 'Loan will be approved' if prediction == 1 else 'Loan will not be approved'
        return jsonify({'prediction': result})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
