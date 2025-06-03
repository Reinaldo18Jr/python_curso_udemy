# try, except, else e finally

try:
    print('ABRIR ARQUIVO')
    8 / 0

except ZeroDivisionError:
    print('DIVIDIU POR ZERO')


else:
    print('Não deu erro.')

finally:                    # bloco que sempre será executado no try 
    print('FECHAR ARQUIVO')
