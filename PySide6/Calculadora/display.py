from PySide6.QtWidgets import QLineEdit
from PySide6.QtCore import Qt, Signal
from PySide6.QtGui import QKeyEvent

from variables import BIG_FONT_SIZE, TEXT_MARGIN, MININUM_WIDTH
from utils import isEmpty, isNumOrDot


# PARA EVITAR CIRCULAR IMPORT

# from typing import TYPE_CHECKING
# if TYPE_CHECKING:
#     from buttons import Button

# button: 'Button'


class Display(QLineEdit):
    eqPressed = Signal()
    delPressed = Signal()
    clearPressed = Signal()
    inputPressed = Signal(str)
    operatorPressed = Signal(str)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.configStyle()

        # self.setReadOnly(True)

    def configStyle(self):
        self.setStyleSheet(f'font-size: {BIG_FONT_SIZE}px;')
        self.setMinimumHeight(BIG_FONT_SIZE * 2)
        self.setMinimumWidth(MININUM_WIDTH)
        self.setAlignment(Qt.AlignmentFlag.AlignRight)

        margins = [TEXT_MARGIN for x in range(4)]
        self.setTextMargins(*margins)


# Comentar esse trecho se self.setReadOnly(True) estiver ativo
    def keyPressEvent(self, event: QKeyEvent):
        text = event.text().strip()
        key = event.key()
        KEYS = Qt.Key

        isEnter = key in [KEYS.Key_Enter, KEYS.Key_Return, KEYS.Key_Equal]
        isDelete = key in [KEYS.Key_Backspace, KEYS.Key_Delete, KEYS.Key_D]
        isEsc = key in [KEYS.Key_Escape, KEYS.Key_C]
        isOperator = key in [
            KEYS.Key_Plus, KEYS.Key_Minus, KEYS.Key_Slash, KEYS.Key_Asterisk,
            KEYS.Key_P,
            ]

        if isEnter:
            self.eqPressed.emit()
            return event.ignore()

        if isDelete:
            self.delPressed.emit()
            return event.ignore()

        if isEsc:
            self.clearPressed.emit()
            return event.ignore()

        if isOperator:
            if text.lower() == 'p':
                text = '^'
            self.operatorPressed.emit(text)
            return event.ignore()

        # Não passar daqui se não tiver um texto
        if isEmpty(text):
            return event.ignore()
        
        if isNumOrDot(text):
            self.inputPressed.emit(text)
            return event.ignore()
