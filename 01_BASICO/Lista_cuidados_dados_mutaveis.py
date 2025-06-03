'''
Cuidados com dados mutáveis:
    - copiado o valor (imutáveis)
    - aponta para o mesmo valor na memória (mutável)
'''

nome = 'Reinaldo'
outra_variavel = nome
nome = 'Junior'

print(nome)
print(outra_variavel)



# lista aponta para o mesmo espaço da memória
lista_a = ['Rei', 'Juninho']
lista_b = lista_a

lista_a[0] = 'Qualquer coisa'
print(lista_b)
