import sys

from PySide6.QtWidgets import QApplication
from PySide6.QtGui import QIcon

from main_window import MainWindow
from display import Display
from info import Info
from buttons import ButtonsGrid
from styles import setupTheme
from variables import WINDOW_ICON_PATH


if __name__ == '__main__':
# Cria a aplicação
    app = QApplication(sys.argv)
    setupTheme(app)
    window = MainWindow()

# Define o ícone
    icon = QIcon(str(WINDOW_ICON_PATH))
    window.setWindowIcon(icon)
    app.setWindowIcon(icon)

# Info
    info = Info('Sua Conta')
    window.addWidgetToVLayout(info)

# Cria o display
    display = Display()
    window.addWidgetToVLayout(display)

# Cria o grid dos botões
    buttonsGrid = ButtonsGrid(display, info)
    window.vLayout.addLayout(buttonsGrid)

# Executa tudo
    window.adjustFixedSize()

    window.show()
    app.exec()
