# Funções recursivas e recursividade
# - funções que podem se chamar de volta
# - úteis para dividir problemas grandes em partes menores
# Toda função recursiva deve ter:
# - Um problema que possa ser dividido em partes menores
# - Um caso recursivo que resolve o pequeno problema
# - Um caso base que para a recursão
# - fatorial -> n! -> 5! = 5 * 4 * 3 * 2 * 1 = 120

def recursiva(inicio=0, fim=10):
    print(inicio, fim)

    # CASO BASE/SEGURANÇA
    if inicio >= fim:
        return fim

    # CASO RECURSIVO:
    # contar até chegar ao final
    inicio += 1
    return recursiva(inicio, fim)

print(recursiva())
print()



def fatorial(n):
    if n <= 1:
        return 1

    return n * fatorial(n - 1)

print(fatorial(5))
