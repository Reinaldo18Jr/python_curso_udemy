# Empacotamento e desempacotamento de dicionários
a, b = 1, 2
a, b = b, a
print(a, b)

pessoa = {
    'nome': 'Reinaldo',
    'sobrenome': 'Junior',
}
a, b = pessoa
print(a, b)   # desempacota apenas as chaves

c, d = pessoa.values()
print(c, d)   # desempacota os valores

# kwargs -> keyword arguments (argumentos nomeados)

dados_pessoa = {
    'idade': 31,
    'altura': 1.84,
}

pessoa_completa = {**pessoa, **dados_pessoa}  # para juntar dois dict em um movo
print(pessoa_completa)

def mostro_argumentos_nomeados(*args, **kwargs):
    print('NÃO NOMEADOS:', args)

    for chave, valor in kwargs.items():
        print('CHAVE:', chave, 'VALOR:', valor)

mostro_argumentos_nomeados(7, 8, 9, nome='Juninho', numero=1234)

mostro_argumentos_nomeados(**pessoa_completa)
