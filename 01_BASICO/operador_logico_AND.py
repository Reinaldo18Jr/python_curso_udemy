# AND: todas condições precisam ser verdadeiras
# se qualquer valor for falso, a expressão inteira será falso
# valores '0', '0.0' e '' são considerados falsy em comparação no python

entrada = input('[E]ntrar [S]air: ')
senha_digitada = input('Senha: ')

senha_permitida = '123456'

if entrada == 'E' and senha_digitada == senha_permitida:
    print('Entrar')
else:
    print('Sair')
