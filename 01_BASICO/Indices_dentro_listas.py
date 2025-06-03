salas = [
    # 0            1
    ['Reinaldo', 'Rei'],  # 0
    # 0
    ['Junior'],  # 1
    # 0           1         2
    ['Angelo', 'Souza', 'Juninho', (0, 10, 20, 30, 40)],  # 2
]

print(salas[1][0])
print(salas[0][1])
print(salas[2][2])
print(salas[2][3][2])

for sala in salas:
    print(f'A sala é {sala}')
    for aluno in sala:
        print(aluno)
