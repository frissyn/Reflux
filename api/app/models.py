from app import db

from datetime import datetime

from flask_login import UserMixin

from sqlalchemy.inspection import inspect


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    pfp = db.Column(db.String, nullable=False)
    name = db.Column(db.String(64), nullable=False)
    publish_key = db.Column(db.String(32), nullable=False)
    admin = db.Column(db.Boolean, nullable=False, default=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow(), nullable=False)

    themes = db.relationship("Theme", backref="creator", lazy=True)

    def cereal(self, admin=False):
        result = {c: getattr(self, c) for c in inspect(self).attrs.keys()}

        if not admin: 
            result.pop("admin")
            result.pop("publish_key")
        
        return result

    def __repr__(self):
        return f"<User @id:{self.id}, @name:{self.name}>"


class Theme(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    referral = db.Column(db.String(16), nullable=False)
    styling = db.Column(db.Text, nullable=False)

    author = db.Column(db.Integer, db.ForeignKey("user.id"))
    
    def __repr__(self):
        return f"<Theme @author:{self.author} @referral:{self.referral}>"