# Salve sua classe em JSON
# Salve os dados da sua classe em JSON e depois crie novamente
# as instâncias da classe com os dados salvos.
# Faça em arquivos separados.

import json

CAMINHO_ARQUIVO = 'aula127.json'

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

p1 = Pessoa('Reinaldo', 31)
p2 = Pessoa('Junior', 25)
p3 = Pessoa('Juninho', 18)
bd = [vars(p1), p2.__dict__, vars(p3)] # transformar os objetos da classe em dicionários, para então gravar em JSON

def fazer_dump():
    with open(CAMINHO_ARQUIVO, 'w', encoding='utf8') as arquivo:
        json.dump(bd, arquivo, ensure_ascii=False, indent=2)

if __name__ == '__main__':
    fazer_dump()
