# Método especial __call__
# callable é algo que pode ser excutado com parênteses em classes
# normais, __call__ faz a instância de uma classe "callable".

class CallMe:
    def __init__(self, phone):
        self.phone = phone

    def __call__(self, nome):   # ou *args, **kwargs
        print(nome, 'está chamando, Nº Cell:', self.phone)
        return 'exemplo'


call1 = CallMe('9870260489')
retorno = call1('Reinaldo')
print(retorno)
