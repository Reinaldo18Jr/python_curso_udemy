# enumerate -> enumera iteráveis (índices)

lista = ['Reinaldo', 'Junior', 'Luiz']
lista.append('Juninho')


for item in enumerate(lista):
    print(item)



lista_enumerada = list(enumerate(lista))
print(lista_enumerada)
