import csv
from pathlib import Path

CAMINHO_CSV = Path(__file__).parent / 'aula2.csv'

lista_clientes = [
    {'Nome': 'Reinaldo', 'Endereço': 'Av 1, 22'},
    {'Nome': 'Junior', 'Endereço': 'Rua 2, 77'},
    {'Nome': 'Souza', 'Endereço': 'Av B, 120'},
]

# with open(CAMINHO_CSV, 'w') as arquivo:
#     nome_colunas = lista_clientes[0].keys()
#     escritor = csv.writer(arquivo)

#     escritor.writerow(nome_colunas)

#     for cliente in lista_clientes:
#         escritor.writerow(cliente.values())


with open(CAMINHO_CSV, 'w') as arquivo:
    nome_colunas = lista_clientes[0].keys()
    escritor = csv.DictWriter(
        arquivo,
        fieldnames=nome_colunas
    )
    escritor.writeheader()

    for cliente in lista_clientes:
        escritor.writerow(cliente)
