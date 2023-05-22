from flask import Flask, request
from flask_cors import CORS
import requests

app = Flask(__name__)


@app.route("/predict", methods=['POST'])
def predict():
    input_json = request.get_json(force=True) 
    print(f"\n\n [INFO] getting this : {input_json} \n\n") 

    request_data = {
        "question" : request.json['question'],
        "context" : request.json['context']
    } 
    response = requests.post("http://localhost:8000/predict", json=request.json)
    response = response.json()
    print(f"outputing : {response}")
    sorted_response = sorted(response, key=lambda x: -x['score'])
    print(f"outputing : {sorted_response}")

    return sorted_response[:5]

@app.route("/hey")
def hey():
    return "hey!"


if __name__ == "__main__":
    CORS(app)
    app.run(debug=True)