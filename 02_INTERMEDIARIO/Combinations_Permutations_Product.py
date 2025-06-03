# Combinations, Permutations e Product - Intertools

# Combinação - Ordem não importa - iterável + tamanaho do grupo
# Permutação - Ordem importa
# Produto - Ordem importa e repete valores únicos

from itertools import combinations, permutations, product

def print_iter(iterator):
    print(*list(iterator), sep='\n')
    print()

pessoas = [
    'João', 'Joana', 'Luiz', 'Letícia',
]

camisetas = [
    ['Preta', 'Branca'],
    ['P', 'M', 'G'],
    ['Masculino', 'Feminino', 'Unissex'],
    ['Algodão', 'Poliéster'],
]

print_iter(combinations(pessoas, 2))
print_iter(permutations(pessoas, 2))
print_iter(product(*camisetas))
