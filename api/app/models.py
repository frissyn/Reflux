import locale

from app import db

from datetime import datetime as dt

from sqlalchemy.inspection import inspect

locale.setlocale(locale.LC_ALL, "")


class User(db.Model):
    id          = db.Column(db.Integer, primary_key=True)
    avatar      = db.Column(db.String, nullable=False)
    name        = db.Column(db.String(64), nullable=False)
    description = db.Column(db.String, nullable=False)
    publish_key = db.Column(db.String(32), nullable=False, unique=True)
    admin       = db.Column(db.Boolean, nullable=False, default=False)
    timestamp   = db.Column(db.DateTime, default=dt.utcnow(), nullable=False)
    themes      = db.relationship(
        "Theme", lazy=True, backref=db.backref("author", lazy=True)
    )

    def cereal(self, admin=False):
        result = {c: getattr(self, c) for c in inspect(self).attrs.keys()}
        result["themes"] = [t.cereal(partial=True) for t in result["themes"]]

        if not admin:
            result.pop("admin")
            result.pop("publish_key")

        return result

    def __repr__(self):
        return f"<User @id:{self.id}, @name:{self.name}>"


class Theme(db.Model):
    id          = db.Column(db.Integer, primary_key=True)
    name        = db.Column(db.String, nullable=False)
    stylesheet  = db.Column(db.Text, nullable=False)
    referral    = db.Column(db.String(16), nullable=False, unique=True)
    downloads   = db.Column(db.Integer, nullable=False, default=0)
    description = db.Column(db.String, nullable=False, default="")
    author_id   = db.Column(db.Integer, db.ForeignKey("user.id"))

    def cereal(self, admin=False, partial=False):
        result = {c: getattr(self, c) for c in inspect(self).attrs.keys()}
        result["f_downloads"] = locale.format("%d", self.downloads, grouping=True)

        if partial:
            result.pop("author")
        else:
            a = self.author
            author = {c.name: getattr(a, c.name) for c in a.__table__.columns}

            result["author"] = author
            result.pop("author_id")

            if not admin:
                result["author"].pop("admin")
                result["author"].pop("publish_key")

        if "monaco" not in result:
            result["monaco"] = "#1c2333"

        if "xterm" not in result:
            result["xterm"] = "#1c2333"

        return result

    def __repr__(self):
        return f"<Theme @author:{self.author} @referral:{self.referral}>"
