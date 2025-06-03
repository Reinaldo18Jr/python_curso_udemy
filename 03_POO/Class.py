# class -> Classes são moldes para criar novos objetos
# As classes geram novos objetos (instâncias) que podem
# ter seus próprios atributos e métodos.
# Os objetos gerados pela classe podem usar seus dados
# internos para realizar várias ações.
# Por convenção usamos PascalCase para nomear classes

class Pessoa:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome


p1 = Pessoa('Reinaldo', 'Junior')

# p1.nome = 'Reinaldo'       # . atributos
# p1.sobrenome = 'Junior'

print(p1.nome)
print(p1.sobrenome)

p2 = Pessoa('Ana', 'Luiza')

# p2.nome = 'Ana'
# p2.sobrenome = 'Luiza'

print(p2.nome)
print(p2.sobrenome)
