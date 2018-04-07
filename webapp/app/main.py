from flask import Flask, render_template, request

app = Flask(__name__, static_url_path='')

@app.route("/")
def index():
    """Route that renders the homepage of the CD server"""
    return render_template('index.html')

@app.route("/healthcheck")
def healthcheck():
    return "I'm healthy!"

# TODO - API CALLS GO HERE