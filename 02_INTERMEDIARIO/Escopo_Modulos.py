'''
Escopo de funções em Python
Escopo significa o local onde aquele código pode atingir.
Existe o escopo global e local.
Escopo Global: onde todo o código é alcançável.
Escopo Local: onde apenas nomes do mesmo local podem ser alcançados.
'''

def escopo():
    x = 1
    print(x)

escopo()


y = 2

def escopo_2():
    y = 20

    def outra_funcao():
        y = 222
        z = 3
        print(y, z)

    outra_funcao()
    print(y)

print(y)
escopo_2()
