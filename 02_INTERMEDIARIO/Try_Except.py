# Try, Except, Else e Finally

try:
    a = 18
    b = 0
    print('Aparece antes do erro')
    c = a / b
    print('Não aparece depois do erro')

except ZeroDivisionError:
    print('Dividiu por zero.')

except NameError:
    print('Nome da variável não está definido.')

except (TypeError, IndexError) as error:
    print('Erro de tipagem + Erro de índice.')
    print('MSG:', error)
    print('Nome:', error.__class__.__name__)

except Exception:
    print('ERRO DESCONHECIDO.')

print('CONTINUAR')
