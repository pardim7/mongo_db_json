from pymongo import MongoClient
import json
from bson import ObjectId

#database do mongodb
database = 'teste_dados'
#tabela de multas
collection = 'multas'

#string de conexao
connection_string = 'string connection aqui'



#Json encoder, para poder receber as buscas como json
class JSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        return super().default(o)
    

#client com a string de conexao
client = MongoClient(connection_string)
db = client[database]
#tabela coomo colection
collection = db[collection]


#retorna os resultados na tabela multas
result = collection.find()

#serializa e exporta como json, e converte para uma lista
data = list(result)  
#serializa o json com a classe JSONEncoder
json_data = json.dumps(data, indent=4, cls=JSONEncoder)  

#salva o json como data.json
with open('data.json', 'w') as file:
    file.write(json_data)
