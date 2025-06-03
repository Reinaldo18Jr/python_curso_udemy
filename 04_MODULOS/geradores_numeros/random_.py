# random tem geradores de números pseudoaleatórios
#   Pseudoaleatórios significa que os números parecem ser aleatórios mas na verdade
#   não são. Portanto este módulo não deve ser usado para segurança ou uso
#   criptográfico.
# O motivo disso é que quando temos uma mesma entrada e um mesmo algoritmo, a saída
# pode ser previsível.
# ALEATORIEDADE SEGUE PADRÃO DO MICROSSEGUNDO ATUAL, PODENDO SER REPRODUZIDO DENOVO
# COPIANDO O VALOR DESSE MICROSSEGUNDO USADO ANTERIORMENTE.

# Funções:
# seed -> inicializa o gerador de random (por isso "números pseudoaleatórios")
# random.seed(0) deixa estático o random. 

# random.randrange(inicio, fim, passo) -> gera um número inteiro aleatório dentro de 
# um intervalo especifico

# random.randint(inicio, fim) -> gera um número inteiro aleatório dentro de um 
# intervalo "sem passo"

# random.uniform(inicio, fim) -> gera um número flutuante aleatório dentro de um
# intervalo "sem passo"

# random.shuffle(SequenciaMutável) -> Embaralha a lista original

# random.choice(Iterável) -> escolhe um elemento do iterável

# random.choices(Ierável, k=N) -> escolhe elementos do iterável e retorna outro iterável
# (REPETE)

# random.sample(Iterável, k=N) -> escolhe elementos do iterável e retorna outro iterável
# (NÃO REPETE)

import random

# r_range = random.randrange(10, 20)
r_range = random.randrange(10, 20, 2)
print(r_range)
print()

r_int = random.randint(10, 20)
print(r_int)
print()

r_float = random.uniform(10, 20)
print(r_float)
print()

nomes = ['Reinaldo', 'Junior', 'Souza', 'Ana', 'Luiza', 'Fernandes']
random.shuffle(nomes)
print(nomes)
print()

novos_nomes = random.sample(nomes, k=3)
print(novos_nomes)
print()

# choices -> pode ocorrer repetição de algum valor da lista
novos_nomes = random.choices(nomes, k=3)
print(novos_nomes)
print()

print(random.choice(nomes))
print()
