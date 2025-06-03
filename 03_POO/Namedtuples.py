# namedtuples -> tuplas imutáveis com nomes para valores
# usamos namedtuples para criar classes de objetos que são apenas um agrupamento
# de atributos, como classes normais sem métodos, ou registros de bases de 
# dados, etc.
# as namedtuples são imutáveis assim como as tuplas.

from collections import namedtuple

Carta = namedtuple('Carta', ['valor', 'naipe'], defaults=['VALOR', 'NAIPE'])
as_espadas = Carta('A', 'Espadas')
print(as_espadas)
print(as_espadas[0])
print(as_espadas.valor)
print(as_espadas[1])
print(as_espadas.naipe)
print()

print(as_espadas._fields)
print(as_espadas._field_defaults)
print()

for item in as_espadas:
    print(item)
print()

print(as_espadas._asdict())


# MELHOR MANEIRA DE USAR
from typing import NamedTuple

class Carta(NamedTuple):
    valor: str = 'VALOR'
    naipe: str = 'NAIPE'
