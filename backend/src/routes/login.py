from flask import Blueprint, current_app, request
from flask_cors import CORS
from flask_jwt_extended import JWTManager, jwt_required
from ..modules import Authorization

jwt = JWTManager(current_app)
auth = Blueprint('auth', __name__)
cors = CORS(auth, resources={ r"/api/*":{"origins":"*"}})

autoriza = Authorization()


@auth.route("/api/autho/signin", methods=['POST'])
def signIn():
	return autoriza.SignIn(request.json)


@auth.route("/api/autho/signin/encuesta", methods=['POST'])
def signInEncuesta():
	return autoriza.SignInEncuesta(request.json)