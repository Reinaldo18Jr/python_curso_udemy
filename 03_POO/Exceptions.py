# Exceptions em Python Orientado a Objetos
# Para criar uma Exception em Python você só precisa herdar de alguma
# exceção da linguagem. A recomendação é herdar de Exception.

# Criando exceções (comum colocar Error ao final)
# Levantando (raise) / Lançando (throw) exceções
# Relançando exceções
# Adicionando notas em exceções 

class MeuError(Exception):
    ...


class OutroError(Exception):
    ...



def levantar():
    exception_ = MeuError('a', 'b', 'c')
    exception_.add_note('Olha a nota 1')
    exception_.add_note('Você errou isso')
    raise exception_


try:
    # 1/0
    levantar()
except (MeuError, ZeroDivisionError) as error:
    print(error.__class__.__name__)
    print(error.args)
    print()
    exception_ = OutroError('lançar de novo')
    exception_.add_note('Mais uma nota')
    exception_.__notes__ += error.__notes__.copy()
    raise exception_ from error
