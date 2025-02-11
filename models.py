from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Employ(db.Model):
    __tablename__ = 'employ'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    department = db.Column(db.String(50), nullable=False)
