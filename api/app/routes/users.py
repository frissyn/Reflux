import os
import flask
import secrets
import asyncio

from app import db
from app import app
from app import replit

from ..models import User


def unlock(req):
    return req.headers.get("PSWD") == os.environ["PSWD"]


def lite(themes, req):
    if req.args.get("lite") in ["True", "true", "1", 1]:
        for t in themes:
            t.pop("stylesheet")
    
    return themes


@app.route("/user/<uname>", methods=["GET"])
def get_user(uname):
    data = asyncio.run(replit.get_user(uname))
    user = User.query.get_or_404(data.id)

    user = user.cereal(admin=unlock(flask.request))
    lite(user["themes"], flask.request)

    return flask.jsonify(user)


@app.route("/portal/<uname>", methods=["POST"])
def user_portal(uname: str):
    if not unlock(flask.request): return flask.abort(403)

    data = asyncio.run(replit.get_user(uname))
    user = User.query.get(data.id)

    if user is None:
        user = User(id=data.id)
        tok = secrets.token_urlsafe(16)

        while User.query.filter_by(publish_key=tok).first():
            tok = secrets.token_urlsafe(16)
        
        user.publish_key = tok

    user.id          = data.id
    user.name        = data.name
    user.avatar      = data.avatar
    user.description = data.bio
    user.timestamp   = data.timestamp

    db.session.add(user)
    db.session.commit()

    return flask.jsonify(user.cereal(admin=True))