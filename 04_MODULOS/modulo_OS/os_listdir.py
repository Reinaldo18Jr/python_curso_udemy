# os.listdir para navegar em caminhos
# c:\Users\NAJA INFORMATICA\Desktop\UNINOVE\Boletos

# caminho = r'c:\\Users\\NAJA INFORMATICA\\Desktop\\UNINOVE\\Boletos'

import os

caminho = os.path.join('c:\\Users', 'NAJA INFORMATICA', 'Desktop', 'UNINOVE', 'Boletos')
print(caminho)
print()

for pasta in os.listdir(caminho):
    caminho_completo_pasta = os.path.join(caminho, pasta)

    if not os.path.isdir(caminho_completo_pasta):
        continue

    for pdf in os.listdir(caminho_completo_pasta):
        print(pdf)
