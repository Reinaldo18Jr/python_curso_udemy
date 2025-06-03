# FATIAMENTO DE STRINGS
#  012345678
#  Olá mundo
# -987654321
# Fatiamento [inicio:fim:passo] [::]
# função len retorna a quantidade de caracteres da string

variavel = 'Olá mundo'

print(variavel[4])    # pega apenas o indice 4
print(variavel[4:])   # pega a partir do indice 4 até o final da string
print(variavel[2:6])  # pega entre os indices 2 e 6 da string, OMITINDO O INDICE 6
print(variavel[:5])   # pega desde o ínicio e para no indice 5, OMITINDO O INDICE 5

print(len(variavel))
print(len(variavel[:7]))

print(variavel[0:len(variavel):1]) # passo: quantidade de caractere que deve ir pulando na iteração
print(variavel[0:len(variavel):3])
print(variavel[::-1])
