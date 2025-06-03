# super() é a super classe na sub classe

# Classe Principal -> super class, base class, parent class
# Classe Filha -> sub class, child class, derived class

class MinhaString(str):
    def upper(self):
        print('CHAMOU O UPPER')
        retorno = super().upper()   # Para buscar o método da class str e NÃO da MinhaString
        print('DEPOIS DO UPPER')
        return retorno


string = MinhaString('Reinaldo')
print(string.upper())




class A:
    atributo_a = 'valorA'

    def __init__(self, atributo):
        self.atributo = atributo

    def metodo(self):
        print('A')


class B(A):
    atributo_b = 'valorB'

    def __init__(self, atributo, outra_coisa):
        super().__init__(atributo)
        self.outra_coisa = outra_coisa

    def metodo(self):
        print('B')


class C(B):
    atributo_c = 'valorC'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        print('Burlando o sistema')

    def metodo(self):
        super().metodo()        # -> retorna o metodo da classe B (super em relação ao C)
        super(B, self).metodo() # -> retorna o metodo da classe A (super em relação ao B)

        A.metodo(self)          # -> NÃO RECOMENDADO DE FAZER
        B.metodo(self)          # -> NÃO RECOMENDADO DE FAZER

        print('C')


c = C('atributo', 'OutraCoisa')
print(c.atributo)
print(c.outra_coisa)

print(c.atributo_a)
print(c.atributo_b)
print(c.atributo_c)
c.metodo()
