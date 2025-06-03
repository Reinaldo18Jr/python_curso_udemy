# count é um iterador sem fim (itertools)

from itertools import count

c1 = count()          # count(11) -> inicia do 11
r1 = range(100)       # range(11, 100) -> inicia do 11 até 99

print('count')
for i in c1:
    if i >= 100:
        break

    print(i)
print()

print('range')
for i in r1:
    print(i)
