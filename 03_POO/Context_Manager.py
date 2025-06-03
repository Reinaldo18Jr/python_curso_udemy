# Context Manager com classes
# pode implementar seus próprios protocolos apenas implementando
# os dunder methods que o Python vai usar. Isso é chamado de 
# Duck typing. Um conceito relacionado com tipagem dinâmica onde
# o Python não está interessado no tipo, mas se alguns métodos
# existem no seu objeto para que ele funcione de forma adequada.

# Para criar um context manager, os métodos __enter__ e __exit__
# devem ser implementados. o método __exit__ receberá a classe de
# exceção, a exceção e o traceback. Se ele retornar True, exceção
# no with serão suprimidas.

# EXEMPLO 1: APENAS ESCRITA
# class MyOpen:
#     def __init__(self, caminho_arquivo, modo):
#         self.caminho_arquivo = caminho_arquivo
#         self.modo = modo
#         self._arquivo = None


#     def __enter__(self):
#         print('ABRINDO ARQUIVO')
#         self._arquivo = open(self.caminho_arquivo, self.modo, encoding='utf8')
#         return self._arquivo


#     def __exit__(self, class_exception, exception_, traceback_):
#         print('FECHANDO ARQUIVO')
#         self._arquivo.close()



# with MyOpen('aula149.txt', 'w') as arquivo:
#     arquivo.write('Linha 1\n')
#     arquivo.write('Linha 2\n')
#     arquivo.write('Linha 3\n')
#     print('WITH', arquivo)




# # EXEMPLO 2: TRATANDO EXCEÇÕES NO __EXIT__
# class MyOpen:
#     def __init__(self, caminho_arquivo, modo):
#         self.caminho_arquivo = caminho_arquivo
#         self.modo = modo
#         self._arquivo = None


#     def __enter__(self):
#         print('ABRINDO ARQUIVO')
#         self._arquivo = open(self.caminho_arquivo, self.modo, encoding='utf8')
#         return self._arquivo


#     def __exit__(self, class_exception, exception_, traceback_):
#         print('FECHANDO ARQUIVO')
#         self._arquivo.close()

#         # raise class_exception(*exception_.args).with_traceback(traceback_)

#         # print(class_exception)
#         # print(exception_)
#         # print(traceback_)

#         exception_.add_note('Minha nota')

#         # raise ConnectionError('Não deu para conectar')

#         # return True



# with MyOpen('aula149.txt', 'w') as arquivo:
#     arquivo.write('Linha 1\n')
#     arquivo.write('Linha 2\n', 123)
#     arquivo.write('Linha 3\n')
#     print('WITH', arquivo)





# Context Manager com função
from contextlib import contextmanager

@contextmanager
def my_open(caminho_arquivo, modo):
    try:
        print('Abrindo arquivo')
        arquivo = open(caminho_arquivo, modo, encoding='utf8')
        yield arquivo             # yield pra função geradora

    # except Exception as e:
    #     print('Ocorreu erro', e)

    finally:
        print('Fechando arquivo')
        arquivo.close()


with my_open('aula149.txt', 'w') as arquivo:
    arquivo.write('Linha 1\n')
    arquivo.write('Linha 2\n', 123)
    arquivo.write('Linha 3\n')
    print('WITH', arquivo)
