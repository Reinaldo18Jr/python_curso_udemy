# string.Template para substituir variáveis em textos
# Métodos:
#   substitute: substitui mas gera erros se faltar chaves
#   safe_substitute: substitui sem gerar erros
# Também pode trocar o delimitador e outras coisas criando uma subclasse de template.

import locale
from datetime import datetime
import json
import string
from pathlib import Path

CAMINHO_ARQUIVO = Path(__file__).parent / 'texto_aula.txt'

locale.setlocale(locale.LC_ALL, '')

def converte_para_brl(numero: float) -> str:
    brl = 'R$ ' + locale.currency(val=numero, symbol=False, grouping=True)
    return brl

data = datetime(2025, 1, 18)
dados = dict(
    nome='Reinaldo',
    valor=converte_para_brl(1_234_456),
    data=data.strftime('%d/%m/%Y'),
    empresa='O. M.',
    telefone='+55 (11) 94567-1087'
)

# print(json.dumps(dados, indent=2, ensure_ascii=False))

# texto = '''
# Prezado(a) $nome,

# Informamos que sua mensalidade será cobrada no valor de ${valor} no dia $data. Caso 
# deseje cancelar o serviço, entre em contato com a $empresa pelo telefone $telefone.

# Atenciosamente,

# ${empresa},
# Abraços
# '''

# template = string.Template(texto)
# # print(template.substitute(dados)) # usar se existir todas as chaves do dict, sem falta uma
# print(template.safe_substitute(dados))


with open(CAMINHO_ARQUIVO, 'r') as arquivo:
    texto = arquivo.read()    # para ler o arquivo inteiro
    template = string.Template(texto)
    print(template.substitute(dados))
