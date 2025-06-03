import os
import json


def listar(tarefas):
    print()
    if not tarefas:
        print('Nenhuma tarefa para listar.')
        print()
        return

    print('Tarefas:')
    for tarefa in tarefas:
        print(f'\t{tarefa}')
    print()


def desfazer(tarefas, tarefas_refazer):
    print()
    if not tarefas:
        print('Nenhuma tarefa para desfazer.')
        print()
        return

    tarefa = tarefas.pop()
    print(f'"{tarefa}" removida da lista de tarefas.')
    tarefas_refazer.append(tarefa)
    print()


def refazer(tarefas, tarefas_refazer):
    print()
    if not tarefas_refazer:
        print('Nenhuma tarefa para refazer.')
        print()
        return

    tarefa = tarefas_refazer.pop()
    print(f'"{tarefa}" adicionada na lista de tarefas.')
    tarefas.append(tarefa)
    print()


def adicionar(tarefa, tarefas):
    print()
    tarefa = tarefa.strip()

    if not tarefa:
        print('Você não digitou uma tarefa.')
        print()
        return

    print(f'"{tarefa}" adicionada na lista de tarefas.')
    tarefas.append(tarefa)
    print()


def ler(tarefas, caminho_arquivo):
    dados = []

    try:
        with open(caminho_arquivo, 'r', encoding='utf8') as arquivo:
            dados = json.load(arquivo)

    except FileNotFoundError:
        print('Arquivo não existe.')
        salvar(tarefas, caminho_arquivo)

    return dados


def salvar(tarefas, caminho_arquivo):
    dados = tarefas

    with open(caminho_arquivo, 'w', encoding='utf8') as arquivo:
        dados = json.dump(tarefas, arquivo, indent=2, ensure_ascii=False)

    return dados


CAMINHO_ARQUIVO = 'exercicio119.json'
tarefas = ler([], CAMINHO_ARQUIVO)
tarefas_refazer = []


while True:
    print('COMANDOS -> listar, desfazer e refazer')
    tarefa = input('Digite uma tarefa ou comando: ')

    comandos = {
        'listar': lambda: listar(tarefas),
        'desfazer': lambda: desfazer(tarefas, tarefas_refazer),
        'refazer': lambda: refazer(tarefas, tarefas_refazer),
        'clear': lambda: os.system('cls'),
        'adicionar': lambda: adicionar(tarefa, tarefas),
    }

    comando = comandos.get(tarefa) if comandos.get(tarefa) is not None else comandos['adicionar']
    comando()

    salvar(tarefas, CAMINHO_ARQUIVO)
