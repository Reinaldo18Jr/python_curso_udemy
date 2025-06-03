# # PyPDF2 para manipular arquivos PDF (Instalação)
# PyPDF2 é uma biblioteca de manipulação de arquivos PDF feita em Python puro,
# gratuita e de código aberto. Ela é capaz de ler, manipular, escrever e unir
# dados de arquivos PDF, assim como adicionar anotações, transformar páginas,
# extrair texto e imagens, manipular metadados, e mais.
# A documentação contém todas as informações necessárias para usar PyPDF2.
# Link: https://pypdf2.readthedocs.io/en/3.0.0/

# Ative seu ambiente virtual
# pip install pypdf2

from pathlib import Path
from PyPDF2 import PdfReader, PdfWriter, PdfMerger

PASTA_RAIZ = Path(__file__).parent
PASTA_ORIGINAIS = PASTA_RAIZ / 'pdfs_originais'
PASTA_NOVA = PASTA_RAIZ / 'arquivos_novos'

RELATORIO_BACENT = PASTA_ORIGINAIS / 'R20230210.pdf'

PASTA_NOVA.mkdir(exist_ok=True)     # CRIAR A PASTA NOVA

reader = PdfReader(RELATORIO_BACENT)

print(len(reader.pages))
for page in reader.pages:
    print(page)
    print()

page0 = reader.pages[0]
imagem0 = page0.images[0]

print(page0.extract_text())

with open(PASTA_NOVA / imagem0.name, 'wb') as fp:    # wb = writen bytes
    fp.write(imagem0.data)


writer = PdfWriter()

with open(PASTA_NOVA / 'NOVO_PDF.pdf', 'wb') as arquivo:

    for page in reader.pages:
        writer.add_page(page)

    writer.write(arquivo)


merger = PdfMerger()

files = [
    PASTA_NOVA / 'NOVO_PDF.pdf',
    PASTA_NOVA / 'NOVO_PDF2.pdf',
]
for file in files:
    merger.append(file)

merger.write(PASTA_NOVA / 'MERGED.pdf')
merger.close()
