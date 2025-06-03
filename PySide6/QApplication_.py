# QApplication e QPushButton de Pyseide6.QtWidgets

# QApplication -> O Widget principal da aplicação
# QPushButton -> Um botão
# PySide6.QtWidgets -> Onde estão os widgets do PySide6

import sys
from PySide6.QtWidgets import QApplication, QPushButton, QWidget, QGridLayout

### Criando Widget de Botão para adicionar na hierarquia:
app = QApplication(sys.argv)

botao = QPushButton('Texto do Botão')
botao.setStyleSheet('font-size: 80px; color: red;')
# botao.show() -> faz o botão em janela separada

botao2 = QPushButton('Botão 2')
botao2.setStyleSheet('font-size: 40px;')
# botao.show() -> faz o botão em janela separada

botao3 = QPushButton('Botão 3')
botao3.setStyleSheet('font-size: 60px;')
# botao.show() -> faz o botão em janela separada

central_widget = QWidget()

layout = QGridLayout()
central_widget.setLayout(layout)

layout.addWidget(botao, 1, 1, 1, 1)       # com QGridLAyout: (widget, linha, coluna, linhaExpandir, colunaExpandir)
layout.addWidget(botao2, 1, 2, 1, 1)
layout.addWidget(botao3, 3, 1, 1, 2)

central_widget.show()

### Executar o loop da aplicação:
app.exec()
