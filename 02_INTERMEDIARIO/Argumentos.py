'''
Argumentos nomeados e não nomeados em funções Python
Argumento nomeado tem nome com sinal de igual = 
Argumento não nomeado recebe apenas o argumento (valor)
'''

def soma(x, y):          # DEFINIÇÃO  x, y são Parâmetros
    print(f'{x=} y={y}', '|', 'x + y =', x + y)

soma(1, 2)               # VALORES    1, 2 são Argumentos (Posicional nesse caso)
soma(2, 1)
soma(y=2, x=1)           # Nomeado
