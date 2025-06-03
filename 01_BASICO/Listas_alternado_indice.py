'''
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis:
    append -> Adiciona um item ao final da lista
    insert -> Adiciona um item no índice escolhido
    pop -> Remove do final ou do índice escolhido
    del -> Apaga um índice
    clear -> Limpa a lista
    extend -> Estende a lista
    + -> Concatena listas
Create Read Update  Delete
Criar, ler, alterar, apagar = lista[i] (CRUD)
'''

lista = [10, 20, 30, 40]
lista[2] = 300
print(lista)

del lista[2]
print(lista)

lista.append('Reinaldo')        #adiciona item na lista
print(lista)

lista.append(99)
ultimo_valor = lista.pop()       #remove o último indíce da lista
print(lista, 'Removido:', ultimo_valor)

lista.insert(2, 'NovoItem')
print(lista)


lista_a = [1, 2, 3]
lista_b = [4, 5, 6]
lista_c = lista_a + lista_b
print(lista_c)
