from datetime import datetime
import datetime
from ..models import db, Personal
from flask_jwt_extended import create_access_token


base = db.session


class functionPersonal:

    def findUserbyNumTra(self, numTra):
        return Personal.query.filter_by(numTra = numTra).first()

    
    def setToken(self, numTra):
        us = Personal.query.filter_by(numTra = numTra).first()
        token = create_access_token(identity = {'nombre':us.nombre.upper(), 'id': us.numTra, 'rol':us.puesto }, expires_delta=datetime.timedelta(minutes=480))
        return token, 200


    def setTokenEncuesta(self, numTra):
        us = Personal.query.filter_by(numTra = numTra).first()
        token = create_access_token(identity = {'nombre':us.nombre.upper(), 'id': us.numTra, 'rol':us.puesto }, expires_delta=datetime.timedelta(minutes=480))
        return token, 200