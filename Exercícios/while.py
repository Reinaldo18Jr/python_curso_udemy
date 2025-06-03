nome = 'Reinaldo Junior'

indice = 0
while indice < len(nome):
    print(nome[indice])
    indice += 1



indice = 0
novo_nome = ''
while indice < len(nome):
    letra = nome[indice]
    novo_nome += f'*{letra}'
    indice += 1
print(novo_nome)
