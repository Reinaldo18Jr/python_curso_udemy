contador = 0

while contador <= 100:
    contador += 1

    if contador == 6:
        print('Não vou mostrar o Nº 6.')
        continue

    if contador >= 10 and contador <= 27:     # pula contagem do 10 ao 27
        print('Não vou mostrar o Nº', contador)
        continue

    print(contador)

    if contador == 40:
        break

print('Acabou.')
