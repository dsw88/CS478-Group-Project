from flask import Flask, render_template, request
from . import cars_model
import json

application = Flask(__name__, static_url_path='')

@application.route("/")
def index():
    """Route that renders the homepage of the CD server"""
    return render_template('index.html')

@application.route("/healthcheck")
def healthcheck():
    return "I'm healthy!"


@application.route("/api/predict", methods=['POST'])
def predict():
    car_to_predict = request.get_json()
    prediction = cars_model.predict_car(car_to_predict)
    return json.dumps(prediction)
