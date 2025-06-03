'''
Dicionários em Python (tipo dict)
Estrutura de dados do tipo par de 'chave' e 'valor'.

Chave pode ser considerada como o 'índice'
    tipo imutável como str, int, float, bool, tuple, etc.
Valor pode ser de qualquer tipo, incluindo outro dicionário.

Usamos as chaves {} ou a classe dict

IMUTÁVEIS = str, int, float, bool, tuple
MUTÁVEIS = dict, list

'''


pessoa = {
    'nome': 'Reinaldo',
    'sobrenome': 'Junior',
    'idade': 31,
    'altura': 1.84,
    'endereços': [
        {'rua': 'tal tal', 'número': 123},
        {'rua': 'outra rua', 'número': 321}
    ]
}

print(pessoa, type(pessoa))
print(pessoa['idade'])

for chave in pessoa:
    print(chave, pessoa[chave])
