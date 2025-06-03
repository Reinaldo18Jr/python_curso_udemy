# List comprehension é uma forma rápida para criar listas a partir de iteráveis

# print(list(range(10))) -> [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

lista = []
for numero in range(10):
    lista.append(numero)
print(lista)

lista = [numero for numero in range(10)]
# lista = [numero * 2 for numero in range(10)]
print(lista)


# Mapeamento de dados em list comprehension
produtos = [
    {'nome': 'p1', 'preco': 20,},
    {'nome': 'p2', 'preco': 10,},
    {'nome': 'p3', 'preco': 30,},
]

novos_produtos = [
    {**produto, 'preco': produto['preco'] * 1.05}
    if produto['preco'] > 20 else {**produto}
    for produto in produtos
]
print(*novos_produtos, sep='\n')


# Filtro de dados em list comprehension 
lista = [n for n in range(10) if n < 5]
print(lista)


lista9 = []
for x in range(3):
    for y in range(3):
        lista9.append((x, y))

lista9 = [
    (x, y)
    for x in range(3)
    for y in range(3)
]

print(lista9)
