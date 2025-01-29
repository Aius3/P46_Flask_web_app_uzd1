from flask_sqlalchemy import SQLAlchemy
import datetime

db = SQLAlchemy()

class Automobilis(db.Model):
    __tablename__ = "automobiliai"
    id = db.Column(db.Integer, primary_key=True)
    gamintojas = db.Column(db.String)
    modelis = db.Column(db.String)
    spalva = db.Column(db.String)
    metai = db.Column(db.Integer)
    variklis = db.Column(db.String)
    kaina = db.Column(db.Float)
    sukurimo_data = db.Column(db.DateTime, default=datetime.datetime.now)

    def __repr__(self):
        return f"id: {self.id} {self.gamintojas} {self.modelis} {self.spalva} {self.metai} {self.variklis} {self.kaina} {self.sukurimo_data}"
