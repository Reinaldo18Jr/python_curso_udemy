# Manipulando chaves e valores em dicionários

pessoa = {}

chave = 'nome'

pessoa[chave] = 'Reinaldo'
pessoa['sobrenome'] = 'Junior'

print(pessoa)
print(pessoa[chave])

del pessoa['sobrenome']
print(pessoa)

if pessoa.get('sobrenome') is None:
    print('Não Existe')
else:
    print(pessoa['sobrenome'])
