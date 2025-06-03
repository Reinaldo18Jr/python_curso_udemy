# Criando arquivos com Python
# Usamos a função open para abrir um arquivo em Python (pode ou não existir)

# Modos: r(leitura), w(escrita), x(para criação), a(escreve ao final),
# b(binário), t(modo texto), +(leitura e escrita)
# Context manager - with (abre e fecha)
# o 'w' APAGA tudo o que estiver escrito no aquivo pra depois escrever o novo texto
# o 'a' NÃO APAGA o que estiver escrito, ele mantem e começa a escrita do final

# Métodos úteis: write, read (escrever e ler); writelines (escrever várias
# linhas); seek (move o cursor); readline (ler linha); readlines (ler linhas)

# Módulos: os.remove ou unlink (apaga o arquivo); os.rename (troca o nome ou
# move o arquivo); json.dump (gera um arquivo json); json.load

caminho_arquivo = 'C:\\Users\\NAJA INFORMATICA\\desktop\\Udemy\\INTERMEDIARIO\\'
caminho_arquivo += 'aula116.txt'

# arquivo = open(caminho_arquivo, 'w')
# arquivo.close()

with open(caminho_arquivo, 'w+') as arquivo:        # with -> abre e depois fecha o arquivo no bloco
    arquivo.write('Linha 1\n')
    arquivo.write('Linha 2\n')

    arquivo.writelines(('Linha 3\n', 'Linha 4\n'))

    arquivo.seek(0,0)                           # move cursor para o topo e conseguir fazer o read
    print(arquivo.read())

    arquivo.seek(0,0)
    print(arquivo.readline(), end='')
    print(arquivo.readline().strip())

    print('Readlines')
    arquivo.seek(0,0)
    for linha in arquivo.readlines():
        print(linha.strip())

print('#' * 30)

with open(caminho_arquivo, 'r') as arquivo:
    print(arquivo.read())

###################################################

caminho_arquivo2 = 'aula116_2.txt'

with open(caminho_arquivo2, 'w', encoding='utf8') as arquivo:
    arquivo.write('Atenção\n')
    arquivo.write('Linha 2\n')
    arquivo.writelines(('Linha 3\n', 'Linha 4\n'))
