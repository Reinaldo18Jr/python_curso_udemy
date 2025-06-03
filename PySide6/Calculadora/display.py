from PySide6.QtWidgets import QLineEdit
from PySide6.QtCore import Qt

from variables import BIG_FONT_SIZE, TEXT_MARGIN, MININUM_WIDTH


# PARA EVITAR CIRCULAR IMPORT

# from typing import TYPE_CHECKING
# if TYPE_CHECKING:
#     from buttons import Button

# button: 'Button'


class Display(QLineEdit):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.configStyle()

    def configStyle(self):
        self.setStyleSheet(f'font-size: {BIG_FONT_SIZE}px;')
        self.setMinimumHeight(BIG_FONT_SIZE * 2)
        self.setMinimumWidth(MININUM_WIDTH)
        self.setAlignment(Qt.AlignmentFlag.AlignRight)

        margins = [TEXT_MARGIN for x in range(4)]
        self.setTextMargins(*margins)
