# method vs @classmethod vs @staticmethod

# method -> self, método de instância
# @classmethod -> cls, método de classe
# @staticmethod -> método estático (SEM self, SEM cls)

class Connection:
    def __init__(self, host='localhost'):
        self.host = host
        self.user = None
        self.password = None

    def set_user(self, user):
        self.user = user

    def set_password(self, password):
        self.password = password

    @classmethod
    def create_with_auth(cls, user, password):
        connection = cls()
        connection.user = user
        connection.password = password
        return connection

    @staticmethod
    def soma(x, y):
        return x + y



c1 = Connection()
c1.set_user('Reinaldo')
c1.set_password('1234')

c2 = Connection.create_with_auth('Junior', 'abcd')

print(c1.user)
print(c1.password)

print(c2.user)
print(c2.password)

print(Connection.soma(2, 3))
