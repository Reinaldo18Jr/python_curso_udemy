import copy

from dados import produtos

# Aumente os preços dos produtos a seguir em 10%
# Gere novos_produtos por deep copy (cópia profunda)

novos_produtos = [
    {**p, 'preco': round(p['preco'] * 1.1, 2)} 
    for p in copy.deepcopy(produtos)
]

print(*produtos, sep='\n')
print()
print(*novos_produtos, sep='\n')
print()




# Ordene os produtos por nome decrescente (do maior para o menor)
# Gere produtos_ordenandos_por_nome por deep copy (cópia profunda)

produtos_ordenandos_por_nome = sorted(
    copy.deepcopy(produtos),
    key=lambda p: p['nome'],
    reverse=True
)

print(*produtos, sep='\n')
print()
print(*produtos_ordenandos_por_nome, sep='\n')
print()




# Ordene os produtos por preco crescente (do menor para o maior)
# Gere produtos_ordenados_por_preco por deep copy (cópia profunda)

produtos_ordenados_por_preco = sorted(
    copy.deepcopy(produtos),
    key=lambda p: p['preco']
)

print(*produtos, sep='\n')
print()
print(*produtos_ordenados_por_preco, sep='\n')
print()
