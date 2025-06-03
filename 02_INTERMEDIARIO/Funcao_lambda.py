'''
Função lambda em Python
A função lambda é uma função como qualquer outra, porém são 
funções anônimas que contém apenas uma linha. Ou seja, tudo
deve ser contido dentro de uma única expressão.
'''

lista = [
    {'nome': 'José', 'sobrenome': 'Silva'},
    {'nome': 'Reinaldo', 'sobrenome': 'Junior'},
    {'nome': 'Daniel', 'sobrenome': 'Moreira'},
    {'nome': 'Maria', 'sobrenome': 'Souza'},
    {'nome': 'Aline', 'sobrenome': 'Oliveira'},
]

# def ordena(item):
#     return item['nome']

# lista.sort(key=ordena)

lista.sort(key=lambda item: item['nome'])

for item in lista:
    print(item)
    print()


def exibir(lista):
    for item in lista:
        print(item)
    print()

l1 = sorted(lista, key=lambda item: item['nome'])
l2 = sorted(lista, key=lambda item: item['sobrenome'])

exibir(l1)
exibir(l2)
