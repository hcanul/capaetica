from ..models import db, Personal, Propuesta, Voto
from ..schema import Schema_Per, Schemas_Per,Schema_Voto, Schema_Votos

base = db.session

class Votos:
    def setLista(self):
        return Schemas_Per.jsonify(Personal.query.order_by(Personal.nombre).all())


    def setVotos(self, data):
        persona = Personal.query.filter_by(nombre=data['data'][1]).first()
        voto = Voto.query.filter_by(numTra=persona.numTra).first()
        if voto:
            # if persona.numTra == voto.numTra:
            return 'error', 401
        datos = data['data'][0]
        for item in datos:
            lista = Propuesta.query.filter_by(numTra=item['numTra']).first()
            if lista:
                votos = lista.votos
                Propuesta.query.filter_by(numTra=item['numTra']).update({'votos':votos+1})
                base.commit()
            else:
                voto = Propuesta(
                    numTra = item['numTra'],
                    votos = 1,
                )
                base.add(voto)
                base.commit()
        regVoto = Voto( numTra = persona.numTra, votos = 7 )
        base.add(regVoto)
        base.commit()
        return 'exito', 200


    def getVotacioes(self):
        votos = Schema_Votos.dump(Propuesta.query.all())
        for item in votos:
            item['nombre'] = Personal.query.filter_by(numTra = item['numTra']).first().nombre
        print(votos)
        return votos, 200
