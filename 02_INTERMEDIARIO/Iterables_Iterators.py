# Generator expression, Iterables e Iterators em Python

import sys

iterable = ['Eu', 'Tenho', '__iter__']
iterator = iter(iterable)          # tem __iter__ e __next__

print(next(iterator))
print(next(iterator))
print(next(iterator))


lista = [n for n in range(10000)]
generator = (n for n in range(10000))      # usa o ()

print(sys.getsizeof(lista))
print(sys.getsizeof(generator))
