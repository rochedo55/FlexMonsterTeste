import json
from faker import Faker
import random
random.seed(8)
fake = Faker()

print(fake.name())
array = []
# for i in range(1000):
#     dictonary = {
#             "DOCUMENTO": str(i),
#             "PRECO_VENDA": 52,
#             "VALOR": random.random(),
#             "CLIENTE": fake.name(),
#             "ESTADO": "AP",
#             "PEDIDO": "000004",
#             "COD_PRODUTO": "000000000000062",
#             "ID": str(i+1),
#             "GRUPO": "Plastico",
#             "FILIAL": "01",
#             "UF_DESTINO": "AP",
#             "PRODUTO": "CAMISETA FOX - AMEIXA",
#             "COD_VENDEDOR": "",
#             "VENDEDOR": fake.name(),
#             "TES": "501",
#             "QUANTIDADE": random.random(),
#             "PERIODO": "2022-03-22",
#             "VAL_ICM": random.random(),
#             "DT_EMISSAO": "2022/03/22",
#             "TIPO_CLIENTE": "F",
#             "COD_CLIENTE": str(random.random()),
#             "COD_GRUPO": str(random.random())
#         }
#     array.append(dictonary)
with open("f800k.json", "w") as outfile:
    for i in range(800000):
        dictonary = {
                "DOCUMENTO": str(i),
                "PRECO_VENDA": 52,
                "VALOR": random.random(),
                "CLIENTE": fake.name(),
                "ESTADO": "AP",
                "PEDIDO": "000004",
                "COD_PRODUTO": "000000000000062",
                "ID": str(i+1),
                "GRUPO": "Plastico",
                "FILIAL": "01",
                "UF_DESTINO": "AP",
                "PRODUTO": "CAMISETA FOX - AMEIXA",
                "COD_VENDEDOR": "",
                "VENDEDOR": fake.name(),
                "TES": "501",
                "QUANTIDADE": random.random(),
                "PERIODO": "2022-03-22",
                "VAL_ICM": random.random(),
                "DT_EMISSAO": "2022/03/22",
                "TIPO_CLIENTE": "F",
                "COD_CLIENTE": str(random.random()),
                "COD_GRUPO": str(random.random())
            }
        array.append(dictonary)
    json.dump(array, outfile)