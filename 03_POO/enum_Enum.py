# Enum -> Enumerações
# Enumerações na programação são usadas em ocasiões onde temos um 
# determinado número de coisas para escolher.
# Enums tem membros e seus valores são constantes.

# Enums em Python:
#   - são um conjunto de nomes simbólicos (membros) ligados a valores únicos.
#   - podem ser iterados para retornar seus membros canônicos na ordem
# de definição
# enum.Enum é a superclasse para suas enumerações. Mas também pode ser
# usada diretamente (mesmo assim, Enums não são classes normais em Python)
# Pode usar seu Enum com type annotations, com isinstance ou outras
# coisas relacionadas com tipo.

# Para obter os dados:
# membro = Classe(valor), Classe['chave']
# chave = Classe.chave.name
# valor = Classe.chave.value

import enum

# Direcoes = enum.Enum('Direcoes', ['ESQUERDA', 'DIREITA'])

class Direcoes(enum.Enum):
    ESQUERDA = 1  # enum.auto()
    DIREITA = 2   # enum.auto()

print(Direcoes(1), Direcoes['ESQUERDA'], Direcoes.ESQUERDA)
print(Direcoes(1).name, Direcoes.ESQUERDA.value)


def mover(direcao: Direcoes):
    if not isinstance(direcao, Direcoes):
        raise ValueError('Direção não encontrada')

    print(f'Movendo para {direcao.name} ({direcao.value}).')


mover(Direcoes.ESQUERDA)
mover(Direcoes.DIREITA)
mover('lado')
