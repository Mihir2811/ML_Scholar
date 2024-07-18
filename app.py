from flask import Flask, request, render_template
import pickle
import pandas as pd

model = pickle.load(open('mod.py', 'rb'))

app = Flask(__name__)

@app.route('/')

def home():
    return render_template('index.html')

@app.route('/predict', methods = ["POST"])

def predict():

    hours = request.form['studyHours']

    input_data = pd.DataFrame([[hours]])
    prediction = model.predict(input_data)
    print(prediction)

    if(prediction>=0):
        return render_template('index2.html',prediction_result= prediction)
    else:
        print('false')

if __name__ == '__main__':
    app.run(debug=None)

