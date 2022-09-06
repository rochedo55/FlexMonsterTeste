import json
from faker import Faker
import random
random.seed(8)
fake = Faker()

print(fake.name())
array = []
with open("f800k.json", "w") as outfile:
    for i in range(800000):
        dictonary = {
                "DOCUMENTO": str(i),
                "PRECO_VENDA": 52,
                "VALOR": random.random()*10,
                "CLIENTE": fake.name(),
                "ESTADO": "AP",
                "PEDIDO": "000004",
                "COD_PRODUTO": "000000000000062",
                "ID": str(i+1),
                "GRUPO": fake.company(),
                "FILIAL": "01",
                "UF_DESTINO": "AP",
                "PRODUTO": "CAMISETA FOX - AMEIXA",
                "COD_VENDEDOR": "",
                "VENDEDOR": fake.name(),
                "TES": "501",
                "QUANTIDADE": random.random()*10,
                "PERIODO": fake.date(),
                "VAL_ICM": random.random()*10,
                "DT_EMISSAO": fake.date(),
                "TIPO_CLIENTE": "F",
                "COD_CLIENTE": str(random.random()*10),
                "COD_GRUPO": str(random.random()*10)
            }
        array.append(dictonary)
    json.dump(array, outfile)
