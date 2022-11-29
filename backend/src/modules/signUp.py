from flask import jsonify
from .verifyuser import Verify


class Authorization():
    
    def SignIn(self, data):
        data = data['data']
        if  Verify().verifyUser(data['user']):
            if  Verify().verify_password(data['user'], data['password']):
                return Verify().getToken(data['user'])
            else:
                return jsonify({"data":'This password is incorrect'}), 401
        else:
            return jsonify({"data":'This user is incorrect'}), 401


    def SignInEncuesta(self, data):
        if  Verify().verifyUserEncuesta(data['data']):
            return Verify().getTokenEncuesta(data['data'])
        else:
            return jsonify({"data":'This user is incorrect'}), 401
        

    # def newUser(self, data):
    #     if  Verify().verifyUser(data['user_name']):
    #         return jsonify({"data":'El usuario existe'}), 401
        
    #     if Verify().verifyMail(data['email']):
    #         return jsonify({"data":'El usuario existe'}), 401

    #     try:
    #         return functionUser().saveUser(data), 200
    #     except Exception as error:
    #         return jsonify({"error":str(error)}), 500