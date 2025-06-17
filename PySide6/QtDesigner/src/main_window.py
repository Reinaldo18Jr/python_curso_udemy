import sys
from typing import cast

from PySide6.QtWidgets import QMainWindow, QApplication
from PySide6.QtCore import QObject, QEvent
from PySide6.QtGui import QKeyEvent
from window import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.buttonSend.clicked.connect(self.changeLabelresult)
        self.lineName.setStyleSheet('background: rgba(0, 0, 0, 0.5);')

        self.lineName.installEventFilter(self)

    def changeLabelresult(self):
        text = self.lineName.text()
        self.labelResult.setText(text)

    def eventFilter(self, watched: QObject, event: QEvent) -> bool:

        if event.type() == QEvent.Type.KeyPress:
            event = cast(QKeyEvent, event)
            text = self.lineName.text()
            self.labelResult.setText(text + event.text())

        return super().eventFilter(watched, event)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    app.exec()
