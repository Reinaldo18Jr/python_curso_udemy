# Peça ao usuário para digitar seu Nome
# Peça ao usuário para digitar sua Idade 
# Se Nome e Idade forem digitados:
#     Exiba:
#     Seu Nome é {nome}
#     Seu nome invertido é {nome invertido}
#     Seu nome contém (ou não) espaços
#     Seu nome tem {n} letras
#     a primeira letra do seu nome é {letra}
#     a última letra do seu nome é {letra}
# Se nada for digitado em Nome ou Idade:
#     Exiba 'Desculpe, você deixou campos vazios.'

nome = input('Digite seu nome: ')
idade = input('Digite sua idade: ')

if not nome or not idade:                          # ou if nome and idade:
    print('Desculpe, você deixou campos vazios.')

else:
    print(f'Seu nome é {nome}.')
    print(f'Seu nome invertido é {nome[::-1]}.')

    if ' ' in nome:
        print('Seu nome contém espaço.')
    else:
        print('Seu nome não possui espaço.')

    print(f'Seu nome tem {len(nome)} letras.')
    print(f'A primeira letra do seu nome é: {nome[0]}.')
    print(f'A última letra do seu nome é: {nome[-1]}')
