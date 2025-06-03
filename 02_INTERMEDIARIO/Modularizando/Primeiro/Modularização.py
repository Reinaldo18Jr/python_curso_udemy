# O primeiro módulo executado chama-se __main__
# Pode importar outro módulo inteiro ou parte do módulo
# Python conhece a pasta onde o __main__ está e as pastas abaixo dele
# Ele não reconhece pastas e móduloas acima do __main__ por padrão
# Python conhece todos os módulos e pacotes presentes nos caminhos de sys.path


import teste_mod
from teste_mod import variavel_modulo, soma

print('Este módulo se chama', __name__)
print(teste_mod.variavel_modulo)
print(variavel_modulo)
print(soma(2, 3))
print(teste_mod.soma(4, 5))
