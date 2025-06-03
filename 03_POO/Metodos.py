# Métodos em instâncias/objetos de classses Python

class Carro:
    def __init__(self, nome):
        self.nome = nome

    def acelerar(self):                         # MÉTODO DA CLASSE CARRO
        print(f'{self.nome} está acelerando.')


fusca = Carro('Fusca')
print(fusca.nome)
fusca.acelerar()


celta = Carro('Celta')
print(celta.nome)
celta.acelerar()
