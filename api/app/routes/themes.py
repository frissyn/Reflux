import os
import flask
import secrets

from app import db
from app import app

from json import JSONDecodeError

from ..models import User
from ..models import Theme


def unlock(req):
    return req.headers.get("PSWD").strip() == os.environ["PSWD"]


@app.route("/theme/<tcode>", methods=["GET"])
def get_theme(tcode: str):
    theme = Theme.query.filter_by(referral=tcode).first()

    if not theme:
        return flask.abort(404)

    return flask.jsonify(theme.cereal())


@app.route("/style/<tcode>", methods=["GET"])
def get_styles(tcode: str):
    theme = Theme.query.filter_by(referral=tcode).first()

    if not theme: return flask.abort(404)

    return flask.jsonify(theme.stylesheet)


@app.route("/theme/upload", methods=["POST"])
def upload_theme():
    try:
        body = flask.request.get_json(force=True)
    except JSONDecodeError:
        return flask.abort(400)

    user = User.query.filter_by(publish_key=body["publish_key"]).first()
    if not user: return flask.abort(401)

    theme = None
    themes = Theme.query.with_parent(user)

    for t in themes:
        if t.name.lower() == body["name"].lower():
            theme = t

    if not theme: 
        theme = Theme()
        tok = secrets.token_hex(8)

        while Theme.query.filter_by(referral=tok).first():
            tok = secrets.token_hex(8)
        
        theme.referral = tok
    
    theme.name        = body["name"]
    theme.description = body["description"]
    theme.stylesheet  = body["stylesheet"]
    theme.author_id   = user.id

    db.session.add(theme)
    db.session.commit()

    return flask.jsonify(theme.cereal())