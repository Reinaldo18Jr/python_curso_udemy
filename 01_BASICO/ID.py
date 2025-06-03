# id = Identidade da variável na mémoria

# variáveis de diferentes nomes mas com mesmo valor, Python coloca mesmo id
# fica usando um mesmo espaço de memória, sem alocar um novo espaço
v1 = 'a'
print(id(v1))

v2 = 'a'
print(id(v2))
