# dataclasses
# O módulo dataclasses fornece um decorador e funções para criar métodos como
# __init__(), __repr__(), __eq__() entre outros, em classes definidas pelo
# usuário. Em resumo: dataclasses são syntax sugar para criar classes normais

# from dataclasses import asdict(para converter em dicionario) astuple(para converter em tupla)
# print(asdict(objeto)) e print(astuple(objeto))

from dataclasses import dataclass, field, fields

@dataclass(order=True)
class Pessoa:
    nome: str
    sobrenome: str

    def __post_init__(self):
        self.nome_completo = f'{self.nome} {self.sobrenome}'

    # @property
    # def nome_completo(self):
    #     return f'{self.nome} {self.sobrenome}'

    # @nome_completo.setter
    # def nome_completo(self, valor):
    #     nome, *sobrenome = valor.split()
    #     self.nome = nome
    #     self.sobrenome = ' '.join(sobrenome)


if __name__ == '__main__':
    p1 = Pessoa('Reinaldo', 'Junior')
    # p1.nome_completo = 'Juninho Souza Junior'
    print(p1)
    print(p1.nome_completo)

    lista = [Pessoa('A', 'Z'), Pessoa('B', 'Y'), Pessoa('C', 'X')]
    ordenadas = sorted(lista, reverse=True) # SEM order no dataclass, usar: ,key=lambda p: p.nome
    print(ordenadas)



@dataclass
class Pessoa2:
    nome: str = field(default='Missing')
    sobrenome: str = 'Not sent'
    idade: int= 100
    enderecos: list[str] = field(default_factory=list)


if __name__ == '__main__':
    pp1 = Pessoa2()
    print(fields(pp1))
    print(pp1)
