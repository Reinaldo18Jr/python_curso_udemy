# Polimorfismo é o princípio que permite que classes derivadas de uma
# mesma superclasse tenham métodos iguais (com a mesma assinatura) mas
# com comportamentos diferentes.

# Assinatura do método = mesmo nome e quantiade de parâmetros (retorno
# não faz parte da assinatura)
# Assinatura do método: nome, parâmetros e retorno iguais
#SO"L"ID
# Princípio da substituição de liskov
# objetos de uma superclasse devem ser substituíveis por objetos de 
# uma subclasse sem quebrar a aplicação.

from abc import ABC, abstractmethod


class Notificacao(ABC):
    def __init__(self, mensagem) -> None:
        self.mensagem = mensagem

    @abstractmethod
    def enviar(self) -> bool: ...


class NotificacaoEmail(Notificacao):
    def enviar(self) -> bool:
        print('E-mail: enviando - ', self.mensagem)
        return True


class NotificacaoSMS(Notificacao):
    def enviar(self) -> bool:
        print('SMS: enviando - ', self.mensagem)
        return True


# n = NotificacaoSMS('testando')
# n.enviar()


def notificar(notificacao: Notificacao):
    notificacao_enviada = notificacao.enviar()

    if notificacao_enviada:
        print('Notificação enviada.')
    else:
        print('Notificação NÃO enviada.')


notificacao_email = NotificacaoEmail('testando email')
notificar(notificacao_email)

notificacao_sms = NotificacaoSMS('testando SMS')
notificar(notificacao_sms)
