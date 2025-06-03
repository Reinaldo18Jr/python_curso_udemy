# argparse.ArgumentParser para argumentos mais complexos

from argparse import ArgumentParser

parser = ArgumentParser()

parser.add_argument(
    '-b', '--basic',
    help= 'Mostra "MENSAGEM" na tela',
    # type=str, tipo do argumento
    metavar='STRING',
    # default='MENSAGEM', valor padrão
    required=False,
    action='append', # recebe o argumento mais de uma vez
    # nargs='+' recebe mais de um valor

    )
args = parser.parse_args()

if args.basic is None:
    print('Você não passou o valor de b.')
    print(args.basic)
else:
    print('O valor de basic:', args.basic)
