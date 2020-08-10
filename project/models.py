from database import db
from flask_login import UserMixin


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))


class Carrier(db.Model):
    __tablename__ = 'carrier'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(1000), unique=True)
    email = db.Column(db.String(100))
    children = db.relationship("Contact")

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}


class Contact(db.Model):
    __tablename__ = 'contact'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(1000))
    cell_number = db.Column(db.String(100))
    email = db.Column(db.String(100))
    carrier_id = db.Column(db.Integer, db.ForeignKey('carrier.id'))

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
