# Desempacotamento em chamadas de métodos e funções

string = 'ABCD'
lista = ['Reinaldo', 'Junior', 1, 2, 3, 4, 'Rei']
tupla = 'Python', 'é', 'legal'

primeiro, *_, ultimo = lista
print(primeiro, ultimo)

for nome in lista:
    print(nome, end=' ')

# ou
print(*lista)
print(*string)
