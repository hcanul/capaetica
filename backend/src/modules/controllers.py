from .functions import Votos


votos = Votos()

class Servicios:
    def setLista(self):
        return votos.setLista()


    def setVotados(self, data):
        return votos.setVotos(data)


    def getVotacioes(self):
        return votos.getVotacioes()