from flask import Blueprint, current_app, request
from flask_cors import CORS
from flask_jwt_extended import JWTManager, jwt_required
from ..modules import Servicios

jwt = JWTManager(current_app)
encuesta = Blueprint('encuesta', __name__)
cors = CORS(encuesta, resources={ r"/api/*":{"origins":"*"}})

servicio = Servicios()

@encuesta.route('/api/encuesta/lista', methods=['GET'])
def setLista():
    return servicio.setLista()


@encuesta.route('/api/encuesta/setVotados', methods=['POST'])
def setVotados():
    return servicio.setVotados(request.json)



@encuesta.route('/api/resultados/votos', methods=['GET'])
def getVotaciones():
    return servicio.getVotacioes()