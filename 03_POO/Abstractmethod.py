# abstractmethod para qualquer método já decorado
# é possível criar @property, @setter, @classmethod, @staticmethod
# e métodos normais como abstratos, para isso use @abstractmethod
# como decorator mais interno.

# Foo - Bar -> são palavras usadas como placeholder para palavras
# que podem mudar na programação.

from abc import ABC, abstractmethod

class AbstractFoo(ABC):
    def __init__(self, name):
        self._name = None     # 1º configura a propriedade
        self.name = name      # 2º recebe retorno do .setter -> property


    @property
    @abstractmethod
    def name(self):
        # return self._name
        ...


    # @name.setter
    # def name(self, name):
    #     self._name = name



class Foo(AbstractFoo):
    name = ''

    def __init__(self, name):
        super().__init__(name)
        # print('Sou inútil')


    # @property
    # def name(self):
    #     return self._name


    # @name.setter
    # def name(self, name):
    #     self._name = name





foo = Foo('Bar')
print(foo.name)
