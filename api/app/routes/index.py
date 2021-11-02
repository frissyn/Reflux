import flask

from app import app

@app.route("/")
def index_route():
    return flask.jsonify({"status": 200})