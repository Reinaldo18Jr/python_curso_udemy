'''
Funções (def) em Python
são trechos de código usados para replicar determinada ação
ao longo do seu código. Elas podem receber valores para
parâmetros (argumentos) e retornar um valor específico.
Por padrão, funções Python retornam None (nada).
'''

def Print():
    print('Várias')

Print()


def imprimir(a, b, c):
    print(a, b, c)

imprimir(1, 2, 3)
imprimir(4, 5, 6)


def saudacao(nome):
    print(f'Olá, {nome}!')

saudacao('Reinaldo')
saudacao('Junior')
