primeiro_valor = input('Digite um número: ')
segundo_valor = input('Digite outro número: ')

# number_1 = float(primeiro_valor)
# number_2 = float(segundo_valor)

# if number_1 > number_2:
#     print(f'O número {number_1} é MAIOR que o número {number_2}.')

# elif number_1 < number_2:
#     print(f'O número {number_1} é MENOR que o número {number_2}.')

# elif number_1 == number_2:
#     print(f'O número {number_1} é IGUAL ao número {number_2}.')

# else:
#     print('Por favor, digite números válidos!')

if primeiro_valor > segundo_valor:
    print(f'{primeiro_valor=} é maior do que {segundo_valor=}')

else:
    print(f'{segundo_valor=} é maior do que {primeiro_valor=}')