# IN: está entre || NOT IN: não está entre

# 0 1 2 3 4 5 6 7  -- índice crescente
# R e i n a l d o  -- string para iterar(navegar entre)
#-8-7-6-5-4-3-2-1  -- índice decrescente(negativo)

nome = 'Reinaldo'

print(nome[3])
print(nome[-5])

print('R' in nome)
print('z' not in nome)


nome_usuario = input('Digite seu nome: ')
encontrar = input('Digite o que deseja encontrar: ')

if encontrar in nome_usuario:
    print(f'"{encontrar}" está em {nome_usuario}.')
else:
    print(f'"{encontrar}" não está em {nome_usuario}.')
