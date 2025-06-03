'''
split e join com list e str
split -> divide uma string
join -> une uma string
strip -> corta os espaços do começo e do fim
rstrip -> corta espaço da direita
lstrip -> corta espaço da esquerda
'''

frase = 'Olha só que, coisa interessante'

lista_frases = frase.split()
lista_frases_2 = frase.split(', ')

print(lista_frases)
print(lista_frases_2)



outra_frase = 'Programação Python, aula básica'
lista_crua = outra_frase.split(',')

lista_python_fixed = []
for i, outra_frase in enumerate(lista_crua):
    lista_python_fixed.append(lista_crua[i].strip())

print(lista_python_fixed)


frases_unidas = '-'.join('abc')
print(frases_unidas)
