# secrets gera números aleatórios SEGUROS

import secrets
import string as s
from secrets import SystemRandom as sr

# criar uma senha forte segura aleatória
print(''.join(sr().choices(s.ascii_letters + s.digits + s.punctuation, k=12)))
print()

# print(secrets.randbelow(100)) # Nº aleatório abaixo de 100
# print(secrets.choice([10, 11, 12, 13 ,14])) # Nº aleatório da lista

random = secrets.SystemRandom()

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
