'''
Closure e funções que retornam outras funções
'''

def criar_saudacao(saudacao):
    def saudar(nome):
        return f'{saudacao}, {nome}!'
    return saudar

falar_bom_dia = criar_saudacao('Bom dia')
falar_boa_noite = criar_saudacao('Boa noite')

print(falar_bom_dia)      # referencia da memória
print(falar_boa_noite)

print(falar_bom_dia('Reinaldo'))    # execução do saudar (Closure)
print(falar_boa_noite('Junior'))

for nome in ['Rei', 'Juninho', 'Souza']:
    print(falar_bom_dia(nome))
    print(falar_boa_noite(nome))
