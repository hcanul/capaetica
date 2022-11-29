from flask_marshmallow import Marshmallow

ma = Marshmallow()



class personalSchema(ma.Schema):
    class Meta:
        fields = ('id', 'numTra', 'nombre', 'puesto')


class VotosSchema(ma.Schema):
    class Meta:
        fields = ('id', 'numTra', 'votos')



### Instancia Tazas Schema ##

Schema_Per = personalSchema()
Schemas_Per = personalSchema(many=True)


Schema_Voto = VotosSchema()
Schema_Votos = VotosSchema(many=True)