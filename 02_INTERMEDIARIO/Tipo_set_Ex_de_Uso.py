# Exemplo de uso dos sets

letras = set()

while True:
    letra = input('Digite: ')
    letras.add(letra.lower())

    if 'r' in letras:
        print('Quebrou o laço.')
        break

    print(letras)
