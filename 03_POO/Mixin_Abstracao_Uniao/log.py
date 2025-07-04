# Abstração -> classe Log
# Herança -> LogFileMixin e LogPrintMixin É UM Log

from pathlib import Path

LOG_FILE = Path(__file__).parent / 'log.txt'


class Log:
    def _log(self, msg):
        raise NotImplementedError('Implemente o método log.')

    def log_error(self, msg):
        return self._log(f'Error: {msg}')

    def log_success(self, msg):
        return self._log(f'Success: {msg}')


class LogFileMixin(Log):
    def _log(self, msg):
        msg_formatada = f'{msg} ({self.__class__.__name__})'
        print('Salvando no log:', msg_formatada)
        with open(LOG_FILE, 'a') as arquivo:        # 'a' append mode: escrever mais linhas sem apagar a anterior
            arquivo.write(msg_formatada)
            arquivo.write('\r\n')


class LogPrintMixin(Log):
    def _log(self, msg):
        print(f'{msg} ({self.__class__.__name__})')



if __name__ == '__main__':   # Para testar esse log apenas aqui e não no main.py
    lp = LogPrintMixin()
    lp.log_error('qualquer coisa')
    lp.log_success('certo')
    
    lf = LogFileMixin()
    lf.log_error('qualquer coisa')
    lf.log_success('certo')

    print(LOG_FILE)
