# Métodos de classe + Factories (fábricas)
# São métodos onde 'self' será 'cls', ou seja:
# ao invés de receber a instância no primeiro
# parâmetro, recebemos a própria classe.

class Pessoa:
    ano = 2025   # -> ATRIBUTO DA CLASSSE

    def __init__(self, nome, idade):   # self -> Para chamar a instância
        self.nome = nome
        self.idade = idade

    @classmethod
    def metodo_de_classe(cls):     # cls -> Para chamar a própria classe e não o objeto/instância
        print('Executa Método de Classe.')

    @classmethod
    def criar_com_50_anos(cls, nome):
        return cls(nome, 50)

    @classmethod
    def criar_sem_nome(cls, idade):
        return cls('Anônima', idade)


p1 = Pessoa('Reinaldo', 31)
p2 = Pessoa.criar_com_50_anos('Junior')
p3 = Pessoa('Anônima', 18)
p4 = Pessoa.criar_sem_nome(25)

print(Pessoa.ano)

# Pessoa.metodo_de_classe(p1)
Pessoa.metodo_de_classe()

print(p2.nome, p2.idade)

print(p3.nome, p3.idade)

print(p4.nome, p4.idade)
