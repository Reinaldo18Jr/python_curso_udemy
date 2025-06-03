# Singleton -> módulos em Python são únicos

import importlib

import Aula98_Mod 

print(Aula98_Mod.variavel)

for i in range(10):
    importlib.reload(Aula98_Mod)
    print(i)

print('Fim')
