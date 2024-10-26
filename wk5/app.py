import pickle
import numpy as np

from flask import Flask, request, jsonify

#linux: use gunicorn
#pip install gunicorn
#gunicorn --bind localhost:9696 app:app 
#in windows 
#pip install waitress 
# waitress-serve --port=9696 app:app
app = Flask('myapp')

model_file = 'model2.bin'
dv_file = 'dv.bin'

with open(model_file, 'rb') as f_in: 
    model = pickle.load(f_in)

with open(dv_file, 'rb') as f_in: 
    dv = pickle.load(f_in)


def predict_customer(customer, dv, model):
    X = dv.transform([customer])
    y_pred = model.predict_proba(X)[0, 1]
    print('input:', customer)
    print('output:', y_pred)
    return y_pred


@app.route('/predict', methods = ['GET', 'POST'] )
def ping():
    customer = request.get_json()

    prediction = predict_customer(customer, dv, model)
    churn = prediction >= 0.5
    
    result = {
        'churn_probability': float(prediction),
        'churn': bool(churn),
    }

    return jsonify(result)
    

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port = 9696)
