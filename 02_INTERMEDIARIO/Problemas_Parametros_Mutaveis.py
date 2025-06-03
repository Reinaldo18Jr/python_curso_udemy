# Problemas dos parâmetros mutáveis em funções Python

def adiciona_clientes(nome, lista=[]):
    lista.append(nome)
    return lista

cliente1 = adiciona_clientes('Reinaldo')
adiciona_clientes('Ana', cliente1)
print(cliente1)

cliente2 = adiciona_clientes('Junior')
adiciona_clientes('Luiza', cliente2)
print(cliente2)
# será reaproveitado a lista do cliente1 aqui com cliente2, e não será feito duas listas separadas



### CORRIGINDO ###

lista1 = []
cliente1 = adiciona_clientes('Reinaldo', lista1)
adiciona_clientes('Ana', cliente1)
print(cliente1)

lista2 = []
cliente2 = adiciona_clientes('Junior', lista2)
adiciona_clientes('Luiza', cliente2)
print(cliente2)



### CORRIGINDO 2 ###

def adiciona_clientes2(nome, lista=None):
    if lista is None:
        lista = []
    lista.append(nome)
    return lista

cliente3 = adiciona_clientes2('Reinaldo')
adiciona_clientes2('Ana', cliente3)
print(cliente3)

cliente4 = adiciona_clientes2('Junior')
adiciona_clientes2('Luiza', cliente4)
print(cliente4)
