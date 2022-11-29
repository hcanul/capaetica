from flask_sqlalchemy import SQLAlchemy
import datetime

db = SQLAlchemy()



class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    user_name = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(160), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    mobile = db.Column(db.String(20), unique=True, nullable=False)
    first_name = db.Column(db.String(20), nullable=True)
    last_name = db.Column(db.String(20), nullable=False)
    created_date = db.Column(db.DateTime, default=datetime.datetime.now)
    update_on = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())


class Personal(db.Model):
    __tablename__ = "personals"
    id = db.Column(db.Integer, primary_key=True, unique=True)
    numTra = db.Column(db.Integer, unique=True, nullable=False)
    nombre = db.Column(db.String(120), nullable=False)
    puesto = db.Column(db.String(100), nullable=False)
    depto = db.Column(db.String(90), nullable=False)
    tipoPersonal = db.Column(db.String(90), nullable=False)
    organismo = db.Column(db.Integer, nullable=False)


class Propuesta(db.Model):
    __tablename__ = "propuestas"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    numTra = db.Column(db.Integer, nullable=False)
    votos = db.Column(db.Integer, nullable=False)
    created_date = db.Column(db.DateTime, default=datetime.datetime.now)


class Voto(db.Model):
    __tablename__ = "votos"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    numTra = db.Column(db.Integer, nullable=False)
    votos = db.Column(db.Integer, nullable=False)
    update_on = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())