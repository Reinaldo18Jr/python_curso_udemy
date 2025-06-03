# __dict__ e vars para atributos de instâncias

class Pessoa:
    ano_atual = 2025

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def get_ano_nascimento(self):
        return Pessoa.ano_atual - self.idade


p1 = Pessoa('Reinaldo', 31)

print(p1.__dict__) # -> dicionário que detem os valores do p1
print(vars(p1))
