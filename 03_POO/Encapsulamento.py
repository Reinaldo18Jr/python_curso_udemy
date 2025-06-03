# ENCAPSULAMENTO (modificadores de acesso: public, protected e private)

# Python NÃO TEM modificadores de acesso mas podemos seguir as convenções:
# Sem Underline = Public (pode ser usado em qualquer lugar)
# Um Underline = Protected (não deve ser usado fora da classe ou subclasses)
# Dois Underlines = Private - 'name mangling' (desfiguração de nomes) só
# deve ser usado na classe em que foi declarado.

class Foo:
    def __init__(self):
        self.public = 'isso é público'
        self._protected = 'isso é protegido'
        self.__private = 'isso é privado'

    def metodo_publico(self):
        self._metodo_protected()
        print(self.__private)
        return 'metodo_publico'

    def _metodo_protected(self):
        print('_metodo_protected')
        return '_metodo_protected'

    def __metodo_private(self):
        print('__metodo_private')
        return '__metodo_private'



######### PUBLICO #################
f = Foo()
print(f.public)
print(f.metodo_publico())

######### PROTEGIDO ###############
f = Foo()
print(f.metodo_publico())
