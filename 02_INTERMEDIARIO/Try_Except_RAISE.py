# raise -> lançando exceções (erros)

# def divide(n, d):
#     try:
#         return n / d

#     except ZeroDivisionError:
#         print('Salvando erro no banco de dados...')
#         raise

# print(divide(8, 0))


def nao_aceito_zero(b):
    if b == 0:
        raise ZeroDivisionError('Impossível dividir por zero!')
    
    return True


def deve_ser_int_ou_float(n):
    tipo_n = type(n)
    if not isinstance(n, (float, int)):
        raise TypeError(
            f'"{n}" deve ser um número inteiro ou float! '
            f'"{tipo_n.__name__}" enviado.'
            )

    return True


def divide_2(a, b):
    deve_ser_int_ou_float(a)
    deve_ser_int_ou_float(b)
    nao_aceito_zero(b)

    return a / b


print(divide_2(8, '0'))
