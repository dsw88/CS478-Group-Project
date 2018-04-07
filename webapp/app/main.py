from flask import Flask, render_template, request

application = Flask(__name__, static_url_path='')

@application.route("/")
def index():
    """Route that renders the homepage of the CD server"""
    return render_template('index.html')

@application.route("/healthcheck")
def healthcheck():
    return "I'm healthy!"

# TODO - API CALLS GO HERE