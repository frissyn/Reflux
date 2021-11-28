import os
import flask
import secrets
import repltalk
import psycopg2

from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

app = flask.Flask(__name__)
replit = repltalk.Client()
app.config.from_mapping({
    "DEBUG": False,
    "TESTING": False,
    "FLASK_DEBUG": 0,
    "CACHE_TYPE": "simple",
    "CACHE_DEFAULT_TIMEOUT": 300,
    "SECRET_KEY": secrets.token_hex(16),
    "SQLALCHEMY_DATABASE_URI": os.environ["DATABASE_URL"],
    "SQLALCHEMY_TRACK_MODIFICATIONS": False
})

conn = psycopg2.connect(os.environ["DATABASE_URL"], sslmode="require")

@app.after_request
def apply_caching(response):
    response.headers["Access-Control-Allow-Origin"] = "*"
    
    return response

tokens = [os.getenv("TOKEN")]
db = SQLAlchemy(app)
migrator = Migrate(app, db)

from .routes import *