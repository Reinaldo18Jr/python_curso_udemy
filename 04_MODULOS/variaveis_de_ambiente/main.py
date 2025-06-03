# Variáveis de ambiente com Python
# para variáveis de ambiente
# Windows PS: $env:VARIAVEL="VALOR" | echo $VARIAVEL
# Linux e Mac: export NOME_VARIAVEL="VALOR" | echo $VARIAVEL

# Para obter o valor das variáveis de ambiente
# os.getenv ou os.environ['VARIAVEL']

# Para configurar variáveis de ambiente
# os.environ['VARIAVEL'] = 'valor'
# Ou usando python-doenv e o arquivo.

# pip install python-dotenv
# from doenv import load_dotenv
# load_dotenv()
# OBS.: sempre lembrar de criar um .env-example

import os
from dotenv import load_dotenv

load_dotenv()

# print(os.environ)
print(os.getenv('BD_PASSWORD'))
