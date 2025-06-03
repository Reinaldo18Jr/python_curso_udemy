# WHILE -> Executa uma ação ENQUANTO uma condição for verdadeira

condicao = True

while condicao:
    nome = input('Qual o seu nome? ')
    print(f'Seu nome é {nome}.')

    if nome == 'sair':
        break

print('Acabou.')




# contar até dez:
contador = 0

while contador <= 10:
    print(contador)
    contador = contador + 1

print('Acabou.')