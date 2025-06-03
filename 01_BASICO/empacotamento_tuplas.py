# desempacotamento

nomes = ['Reinaldo', 'Junior', 'Rei']
nome1, nome2, nome3 = nomes

# ou nome1, nome2, nome3 = ['Reinaldo', 'Junior', 'Rei']



# para desempacotar apenas um item e agrupar o restante em outra variavel
nome1, *resto = ['Reinaldo', 'Junior', 'Rei']
print(nome1, resto)

nome1, *_ = ['Reinaldo', 'Junior', 'Rei']
print(nome1, _)
# por convensão, o _ serve para indicar uma variavel que não será usada

_, nome2, *_ = ['Reinaldo', 'Junior', 'Rei']
print(nome2)
# para pegar o segundo item da lista
