nome = 'Reinaldo Junior'
altura = 1.84
peso = 68
imc = peso / (altura * altura)  # ou peso / altura ** 2

linha_1 = f'{nome} tem {altura:.2f} de altura,'
linha_2 = f'pesa {peso} quilos e seu IMC é:'
linha_3 = f'{imc:.2f}'

print(linha_1)
print(linha_2)
print(linha_3)
