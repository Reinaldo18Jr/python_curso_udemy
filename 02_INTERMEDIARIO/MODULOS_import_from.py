
# Módulos padrão do Python -> import - from - as - *

# inteiro -> import nome_modulo
# Vantagens: tem o namespace do módulo
# Desvantagens: nomes grandes

import sys

platform = 'Variável que não vai afetar o platform do import sys'
print(sys.platform)
print(platform)



# partes -> from nome_modulo import objeto1, objeto2
# Vantagens: nomes pequenos
# Desvantagens: sem o namespace do módulo

from sys import exit, path



# alias 1 -> import nome_modulo as apelido

import sys as sistema
sys = 'alguma coisa'
print(sistema.platform)

# alias 2 -> from nome_modulo import objeto as apelido
# Vantagens: pode reservar nomes para seu código
# Desvantagens: pode ficar fora do padrão da linguagem

from sys import platform as pf, exit as ex



# má prática -> from nome_modulo import *
# Vantagens: importa tudo de um módulo
# Desvantagens: importa tudo de um módulo

from sys import *
