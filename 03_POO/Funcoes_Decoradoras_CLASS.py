# Funções decoradoras e decoradores com CLASSES

def adiciona_repr(cls):
    def meu_repr(self):
        class_name = self.__class__.__name__
        class_dict = self.__dict__
        class_repr = f'{class_name}({class_dict})'
        return class_repr
    cls.__repr__ = meu_repr       # mesclar o __repr__ com a função meu_repr
    return cls


class MyReprMixin:
    def __repr__(self):
        class_name = self.__class__.__name__
        class_dict = self.__dict__
        class_repr = f'{class_name}({class_dict})'
        return class_repr
# classe para usar como HERANÇA abaixo, mas deve-se evitar de usar muita herança


@adiciona_repr
class Time:
    def __init__(self, nome):
        self.nome = nome


@adiciona_repr
class Planeta:
    def __init__(self, nome):
        self.nome = nome


# Time = adiciona_repr(Time) -> SEM USAR @adiciona_repr
brasil = Time('Brasil')
portugal = Time('Portugal')

# Planeta = adiciona_repr(Planeta) -> SEM USAR @adiciona_repr
terra = Planeta('Terra')
marte = Planeta('Marte')

print(brasil)
print(portugal)

print(terra)
print(marte)
