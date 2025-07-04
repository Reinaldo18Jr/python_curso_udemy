# Herança Múltipla
# uma classe pode estender várias outras classes.

# Herança simples:
# Animal -> Mamifero -> Humano -> Pessoa -> Cliente

# Herança múltipla e mixins
# Log -> FileLog
# Animal -> Mamifero -> Humano -> Pessoa -> Cliente
# Cliente(Pessoa, FileLog)

# Saber a ordem de chamada dos métodos usar método Classe.mro()
# Ou o atributo __mro__

class A:
    ...

    def quem_sou(self):
        print('A')


class B(A):
    ...

    def quem_sou(self):
        print('B')


class C(A):
    ...

    def quem_sou(self):
        print('C')


class D(B, C):
    ...

    def quem_sou(self):
        print('D')


d = D()
d.quem_sou()
print(D.mro())
