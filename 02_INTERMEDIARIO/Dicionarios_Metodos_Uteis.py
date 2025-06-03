'''
Métodos úteis dos dicionários em Python
len -> quantas chaves
keys -> iterável com as chaves
values -> iterável com os valores
items -> iterável com chaves e valores
setdefault -> adiciona valor se a chave não existe
copy -> retorna uma cópia rasa (shallow copy)
get -> obtém uma chave
pop -> apaga um item com a chave especificada (del)
popitem -> apaga o último item adicionado
update -> atualiza um dicionário com outro
'''

pessoa = {
    'nome': 'Reinaldo',
    'sobrenome': 'Junior'
}

print(pessoa.__len__())
print(len(pessoa))
print()
print(pessoa.keys())
print(list(pessoa.keys()))
print()
print(list(pessoa.values()))
for valor in pessoa.values():
    print(valor)
print()
print(list(pessoa.items()))
for chave, valor in pessoa.items():
    print(chave, valor)
print()

pessoa.setdefault('idade', 31)
print(pessoa['idade'])
print(pessoa)

import copy

d1 = {
    'c1': 1,
    'c2': 2,
    'l1': [0, 1, 2],   
}
d2 = d1.copy()          # copia rasa não reserva a lista (sub-nivel)

# d2 = copy.deepcopy(d1)   onde preserva o d1 de todas as alterações na d2

d2['c1'] = 1000     # valor alterado na d2 não muda para d1 com copy()
d2['l1'][1] = 9999  # já lista é alterada em ambas com copy(), deve usar deepcopy()

print(d1)
print(d2)


p1 = {
    'nome': 'Rei',
    'sobrenome': 'Junior',
}

print(p1.get('nome'))

nome = p1.pop('nome')    # retorna valor da chave e apaga a chave do dict
print(nome)
print(p1)

# p1.popitem() -> apaga a ultima chave do dict

p1.update({
    'nome': 'novo valor',
    'idade': 31,
})
print(p1)

#p1.update(nome='novo valor', idade=31)

