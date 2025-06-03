# OR: se uma condição é verdadeira, toda a expressão se torna verdadeira
# '0', '0.0' e '' são considerados falsy

entrada = input('[E]ntrar [S]air: ')
senha_digitada = input('Senha: ')

senha_permitida = '123456'

if (entrada == 'E' or entrada == 'e') and senha_digitada == senha_permitida:
    print('Entrar')
else:
    print('Sair')
