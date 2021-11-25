import os
import flask
import secrets

from app import db
from app import app

from json import JSONDecodeError, loads

from ..models import User
from ..models import Theme


def unlock(req):
    return req.headers.get("PSWD").strip() == os.environ["PSWD"]


def lite(themes, req):
    if req.args.get("lite") in ["True", "true", "1", 1]:
        for t in themes:
            t.pop("stylesheet")

    return themes


@app.route("/theme/all", methods=["GET"])
def get_all_themes():
    themes = Theme.query.all()
    themes = [t.cereal() for t in themes]

    return flask.jsonify(lite(themes, flask.request))


@app.route("/theme/feed/popular", methods=["GET"])
def get_popular_themes():
    floor = flask.request.args.get("floor")
    floor = int(floor) if floor else 10

    themes = Theme.query.filter(Theme.downloads >= floor).order_by(Theme.downloads.desc())
    themes = [t.cereal() for t in themes]

    return flask.jsonify(lite(themes, flask.request))


@app.route("/theme/feed/recent", methods=["GET"])
def get_recent_themes():
    limit = flask.request.args.get("limit")
    limit = int(limit) if limit else 60

    themes = Theme.query.filter().order_by(Theme.id.desc())
    themes = [t.cereal() for t in themes]

    return flask.jsonify(lite(themes, flask.request))


@app.route("/theme/<tcode>", methods=["GET"])
def get_theme(tcode: str):
    theme = Theme.query.filter_by(referral=tcode).first()

    if not theme:
        return flask.abort(404)

    theme.downloads += 1
    db.session.commit()

    return flask.jsonify(theme.cereal())


@app.route("/style/<tcode>", methods=["GET"])
def get_styles(tcode: str):
    theme = Theme.query.filter_by(referral=tcode).first()

    if not theme:
        return flask.abort(404)
    else:
        theme.downloads += 1

    return flask.jsonify(theme.stylesheet)


@app.route("/theme/delete/<tcode>", methods=["DELETE"])
def delete_theme(tcode: str):
    if not unlock(flask.request): return flask.abort(403)

    theme = Theme.query.filter_by(referral=tcode).first()

    if not theme: return flask.abort(404)

    db.session.delete(theme)
    db.session.commit()

    return "", 204


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

    if "monaco" in body.keys():
        theme.monaco      = body["monaco"]
    if "xterm" in body.keys():
        theme.xterm       = body["xterm"]

    db.session.add(theme)
    db.session.commit()

    return flask.jsonify(theme.cereal())
