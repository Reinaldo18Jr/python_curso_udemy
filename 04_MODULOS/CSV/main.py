# CSV (Comma Separated Values)
# É um formato de arquivo que armazena dados em forma de tabela, onde cada linha
# representa uma linha da tabela e as colunas são separadas por virgulas. Ele é
# amplamente usado para transferir dados entre sistemas de diferentes plataformas,
# por exemplo, para importar ou exportar dados para uma planilha (Google Sheets, 
# Excel, LibreOffice Calc) ou para uma base de dados. Um arquivo CSV geralmente tem
# a extensão ".csv" e pode ser aberto em um editor de texto ou em uma planilha
# eletrônica. 

# Exemplo de um arquivo CSV pode ser: 
# Nome,Idade,Endereço
# Reinaldo,31,"Av Python, 21, Centro"
# Junior,18,"Rua Código, 112, Bairro A"

# A primeira linha do arquivo define os nomes das colunas, enquanto as linhas 
# seguintes contêm os valoes das linhas, separados por vírgulas.

# Regras simples do CSV:
#   - Separe os valoes das colunas com um delimitador único (,)
#   - Cada registro deve estar em uma linha
#   - Não deixar linhas ou espaços sobrando
#   - Use o caractere de escape (") quando o delimitador aparecer no valor.

# csv.reader -> lê o CSV em formato de lista
# csv.DictReader -> lê o CSV em formato de dicionário

import csv
from pathlib import Path

CAMINHO_CSV = Path(__file__).parent / 'aula.csv'
print(CAMINHO_CSV)

# with open(CAMINHO_CSV, 'r') as arquivo:
#     leitor = csv.reader(arquivo)

#     for linha in leitor:
#         print(linha)

with open(CAMINHO_CSV, 'r') as arquivo:
    leitor = csv.DictReader(arquivo)

    for linha in leitor:
        print(linha)
