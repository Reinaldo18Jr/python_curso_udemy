# __new__ é o método responsável por criar e retornar o novo objeto, por
# isso recebe cls.
# __new__ DEVE retornar o novo objeto.

# __init__ é o método responsável por inicializar a instância, por isso
# recebe self.
# __init__ NÃO DEVE retornar nada (None)

# object é a super classe de uma classe

class A(object):
    def __new__(cls, *args, **kwargs):
        # print('Antes de criar a instância')
        # instancia = super().__new__(cls)
        # print('Depois de criar a instância')
        # instancia.x = 213
        # return instancia

        instancia = super().__new__(cls)
        return instancia


    def __init__(self, x):
        self.x = x
        print('Sou o init')


    def __repr__(self):
        return 'A()'


a = A(123)
print(a)
print(a.x)
