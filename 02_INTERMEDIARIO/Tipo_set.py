'''
Sets - Conjuntos em Python (tipo set)
Sets em Python são mutáveis, porém aceitam apenas
tipos imutáveis como valor interno.

Criando um set:
set(iterável) ou {1, 2, 3}

são eficientes para remover valores duplicados de iteráveis
- seus valores serão sempre únicos;
- não aceitam valores mutáveis;
- não tem índexes;
- não garantem ordem;
- são iteráveis (for, in, not in)

Métodos úteis:
add, update, clear, discard
'''

s1 = set('Reinaldo')   # vai iterar em cada letra sem garantir ordem
print(s1)

s2 = {'Rei', 'Junior', 31}
print(s2, type(s2))

s3 = {1, 2, 3, 3, 3, 3, 1} # elimina valores duplicados
print(s3)

s4 = set()
s4.add('Nome')    # add um valor por vez
s4.add(99)
s4.update('ABC', ('Reinaldo',))  # para adicionar vários valores de uma vez
print(s4)

# s4.clear() limpa todo o set
# s4.discard('ABC')  para excluir um valor por vez


'''
Operadores Úteis:
união | união (union) = une eliminando valores repetidos
intersecção & (intersection) = itens presentes em ambos
diferença - = itens presentes apenas no set da esquerda
diferença simétrica ^ = itens que não estão em ambos
'''

exemplo1 = {1, 2, 3}
exemplo2 = {2, 3, 4}

ex3 = exemplo1 | exemplo2        # UNIÃO
print(ex3)

ex4 = exemplo1 & exemplo2        # INTERSEÇÃO
print(ex4)

ex5 = exemplo1 - exemplo2        # DIFERENÇA
ex6 = exemplo2 - exemplo1
print(ex5)
print(ex6)

ex7 = exemplo1 ^ exemplo2        # DIFERENÇA SIMÉTRICA
print(ex7)
