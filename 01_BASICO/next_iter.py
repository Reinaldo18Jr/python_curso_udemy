# Iterável -> str, range, etc
# Iterador -> quem sabe entregar um valor por vez
# next -> me entregue o próximo valor
# iter -> me entregue seu iterador

# texto = iter('Reinaldo')   # __iter__()

# print(texto.__next__())
# print(texto.__next__())
# print(texto.__next__())
# print(next(texto))


texto = 'Rei'   # iterável
iterador = iter(texto)  # iterador

while True:
    try:
        letra = next(iterador)
        print(letra)
    except StopIteration:
        break

# é o mesmo que:

for letra in texto:
    print(letra)