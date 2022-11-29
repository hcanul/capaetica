from datetime import datetime
import datetime
from ..models import db, User
from werkzeug.security import generate_password_hash
from werkzeug.security import check_password_hash
from flask_jwt_extended import create_access_token

base = db.session


class functionUser:

    admin = {
        "user_name": 'hcanul',
        "first_name":"Hugo Paulino",
        "last_name":"Canul Echazarreta",
        "email":"cyber.frenetic@gmail.com",
        "mobile":"(562) 114-3235",
        "password": "ha260182ha",
    }

    def is_Data(self):
        if not User.query.all():
            self.saveUser(self.admin)

    
    def findUserByUserName(self, user):
        isExist = User.query.filter_by(user_name = user).first()
        if isExist:
            return True
        else:
            return False


    def findUserByEmail(self, email):
        isExist = User.query.filter_by(email = email).first()
        if isExist:
            return True
        else:
            return False


    def create_password(self, password):
        return generate_password_hash(password)


    def findUserbyUser(self, user):
        return User.query.filter_by(user_name=user).first()


    def findUserbyId(self, id):
        return User.query.filter_by(id=id).first()


    def verify_password(self, user, password):
        return check_password_hash(self.findUserbyUser(user).password, password)


    def setToken(self, user):
        us = User.query.filter_by(user_name = user).first()
        token = create_access_token(identity = {'nombre':us.first_name.upper() + ' ' + us.last_name.upper(), 'id': us.id, 'rol':"SUPERADMIN" }, expires_delta=datetime.timedelta(minutes=480))
        return token, 200

    
    def saveUser(self, data):
        user = User(
            user_name = data['user_name'].upper(),
            first_name = data['first_name'].upper(),
            last_name = data['last_name'].upper(),
            email = data['email'],
            mobile = data['mobile'],
            password = self.create_password(data['password']),
            )
        base.add(user)
        base.commit()
        return data['user_name'].upper()
        

    def findUserbyId_Name(self, id):
        name = User.query.filter_by(id=id).first().first_name + ' ' + User.query.filter_by(id=id).first().last_name
        return name