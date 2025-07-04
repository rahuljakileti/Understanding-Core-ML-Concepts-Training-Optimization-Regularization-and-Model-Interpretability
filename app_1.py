from flask import Flask, render_template, request, redirect
import os
from utils.ml_helpers import train_model, get_visualizations, predict_input

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/train', methods=['POST'])
def train():
    file = request.files['dataset']
    model_type = request.form.get('model_type', 'logistic')

    if file:
        path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(path)

        results = train_model(path, model_type=model_type)
        get_visualizations(results)

        return render_template('result.html', metrics=results['metrics'])

    return redirect('/')

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    prediction = None
    if request.method == 'POST':
        form_data = request.form.to_dict()
        prediction = predict_input(form_data)

    return render_template('predict.html', prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True)
