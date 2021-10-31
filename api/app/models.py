from app import db

from datetime import datetime as dt

from sqlalchemy.inspection import inspect


class User(db.Model):
    id          = db.Column(db.Integer, primary_key=True)
    avatar      = db.Column(db.String, nullable=False)
    name        = db.Column(db.String(64), nullable=False)
    description = db.Column(db.String, nullable=False)
    publish_key = db.Column(db.String(32), nullable=False)
    admin       = db.Column(db.Boolean, nullable=False, default=False)
    timestamp   = db.Column(db.DateTime, default=dt.utcnow(), nullable=False)
    themes      = db.relationship("Theme", backref="creator", lazy=True)

    def cereal(self, admin=False):
        result = {c: getattr(self, c) for c in inspect(self).attrs.keys()}

        if not admin: 
            result.pop("admin")
            result.pop("publish_key")
        
        return result

    def __repr__(self):
        return f"<User @id:{self.id}, @name:{self.name}>"


class Theme(db.Model):
    id        = db.Column(db.Integer, primary_key=True)
    styling   = db.Column(db.Text, nullable=False)
    referral  = db.Column(db.String(16), nullable=False)
    downloads = db.Column(db.Integer, nullable=False, default=0)
    author    = db.Column(db.Integer, db.ForeignKey("user.id"))

    def cereal(self, admin=False):
        return {c: getattr(self, c) for c in inspect(self).attrs.keys()}
    
    def __repr__(self):
        return f"<Theme @author:{self.author.name} @referral:{self.referral}>"