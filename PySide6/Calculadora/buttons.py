import math
from typing import TYPE_CHECKING

from PySide6.QtWidgets import QPushButton, QGridLayout
from PySide6.QtCore import Slot

from utils import isNumOrDot, isEmpty, isValidNumber, convertToNumber
from variables import MEDIUM_FONT_SIZE

if TYPE_CHECKING:
    from display import Display
    from main_window import MainWindow
    from info import Info


class Button(QPushButton):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.configStyle()

    def configStyle(self):
        font = self.font()
        font.setPixelSize(MEDIUM_FONT_SIZE)
        self.setFont(font)
        self.setMinimumSize(75, 75)


class ButtonsGrid(QGridLayout):
    def __init__(self, display: 'Display', info: 'Info', window: 'MainWindow',
                *args, **kwargs):
        super().__init__(*args, **kwargs)

        self._gridMask = [
            ['C', '◀', '^', '/'],
            ['7', '8', '9', '*'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            ['N',  '0', '.', '='],
        ]
        self.display = display
        self.info = info
        self.window = window
        self._equation = ''
        self._equationInitialValue = 'Sua Conta'
        self._left = None
        self._op = None
        self._right = None

        self.equation = self._equationInitialValue
        self._makeGrid()

    @property
    def equation(self):
        return self._equation
    
    @equation.setter
    def equation(self, value):
        self._equation = value
        self.info.setText(value)

    def _makeGrid(self):
        self.display.eqPressed.connect(self._eq)
        self.display.delPressed.connect(self._backspace)
        self.display.clearPressed.connect(self._clear)
        self.display.inputPressed.connect(self._insertToDisplay)
        self.display.operatorPressed.connect(self._configLeftOp)

        for rowNumber, rowData in enumerate(self._gridMask):
            for columnNumber, buttonText in enumerate(rowData):
                button = Button(buttonText)

                # if buttonText not in '0123456789.':
                if not isNumOrDot(buttonText) and not isEmpty(buttonText):
                    button.setProperty('cssClass', 'specialButton')
                    self._configSpecialButton(button)

                self.addWidget(button, rowNumber, columnNumber)

                slot = self._makeSlot(self._insertToDisplay, buttonText)
                self._connectButtonCliked(button, slot)

    def _connectButtonCliked(self, button, slot):
        button.clicked.connect(slot)

    def _configSpecialButton(self, button):
        text = button.text()
        
        if text == 'C':
            # slot = self._makeSlot(self._clear, 'Essa é a msg')
            self._connectButtonCliked(button, self._clear)
            # button.clicked.connect(self.display.clear)

        if text == '◀':
            self._connectButtonCliked(button, self.display.backspace)

        if text == 'N':
            self._connectButtonCliked(button, self._invertNumber)

        if text in '+-*/^':
            self._connectButtonCliked(
                button,
                self._makeSlot(self._configLeftOp, text)
            )

        if text == '=':
            self._connectButtonCliked(button, self._eq)


    @Slot()
    def _makeSlot(self, func, *args, **kwargs):
        @Slot(bool)
        def realSlot(_):
            func(*args, **kwargs)
        return realSlot

    @Slot()
    def _invertNumber(self):
        displayText = self.display.text()

        if not isValidNumber(displayText):
            return

        number = convertToNumber(displayText) * -1
        self.display.setText(str(number))

    @Slot()
    def _insertToDisplay(self, text):
        newDisplayValue = self.display.text() + text
    
        if not isValidNumber(newDisplayValue):
            return

        self.display.insert(text)
        self.display.setFocus()

    @Slot()
    def _clear(self):
        self.display.clear()
        self.equation = self._equationInitialValue
        self._left = None
        self._op = None
        self._right = None
        self.display.setFocus()

    @Slot()
    def _configLeftOp(self, text):
        displayText = self.display.text()           # valor Nº _left
        self.display.clear()
        self.display.setFocus()

# Se clicar em um operador(+_*/) sem ter digitado um Nº primeiro
        if not isValidNumber(displayText) and self._left is None:
            self._showError('Você não digitou algum valor!')
            return

# Se houver Nº na esquerda junto com operador, aguardar Nº da direita
        if self._left is None:
            self._left = convertToNumber(displayText)

        self._op = text
        self.equation = f'{self._left} {self._op} ??'

    @Slot()
    def _eq(self):
        displayText = self.display.text()

        if not isValidNumber(displayText) or self._left is None:
            self._showError('Você não digitou o outro número da operação.')
            return
        
        self._right = convertToNumber(displayText)
        self.equation = f'{self._left} {self._op} {self._right}'
        result = 'error'

        try:
            if '^' in self.equation and isinstance(self._left, int | float):
                result = math.pow(self._left, self._right)
                result = convertToNumber(str(result))
            else:
                result = eval(self.equation)

        except ZeroDivisionError:
            self._showError('Não é possível realizar divisão por zero.')
        except OverflowError:
            self._showError('Operação com valor muito alto de resultado.')

        self.display.clear()
        self.info.setText(f'{self.equation} = {result}')
        self._left = result
        self._right = None
        self.display.setFocus()

        if result == 'error':
            self._left = None

    # def _showError(self, text):
    #     msgBox = self.window.makeMsgBox()
    #     msgBox.setText(text)
    #     msgBox.setInformativeText('''
    #     Lorem ipsum dolor sit amet. Et magni animi non voluptate aperiam non
    #     quisquam perferendis ab rerum autem et sequi nihil qui voluptatem soluta
    #     et ratione possimus. Quo ipsum quaerat in dolorum nisi vel dolores nesciunt
    #     nam maiores asperiores a fugiat placeat. Eos ratione dolorem non galisum
    #     nostrum sit rerum magnam! Ut molestiae odit ut architecto internos hic
    #     tempore galisum! Hic distinctio porro id dolores nostrum et odio eveniet
    #     ut ratione temporibus ea repellat cupiditate eos laborum aperiam sed soluta
    #     error. Et architecto cupiditate non rerum aliquid 33 corrupti perferendis.
    #     Et repudiandae reprehenderit vel quos eligendi quo dolores distinctio.
    #     ''')
    #     msgBox.setIcon(msgBox.Icon.Warning)

    #     msgBox.setStandardButtons(
    #         msgBox.StandardButton.Ok |
    #         msgBox.StandardButton.Cancel
    #     )
    #     msgBox.button(msgBox.StandardButton.Ok).setText('Beleza')
    #     msgBox.exec()

    #     result = msgBox.exec()
    #     if result == msgBox.StandardButton.Ok:
    #         print('Usuário clicou em OK')
    #     elif result == msgBox.StandardButton.Cancel:
    #         print('Usuário clicou em Cancel')

    @Slot()
    def _backspace(self):
        self.display.backspace()
        self.display.setFocus()

    def _makeDialog(self, text):
        msgBox = self.window.makeMsgBox()
        msgBox.setText(text)
        return msgBox

    def _showError(self, text):
        msgBox = self._makeDialog(text)
        msgBox.setIcon(msgBox.Icon.Critical)
        msgBox.exec()
        self.display.setFocus()

    def _showInfo(self, text):
        msgBox = self._makeDialog(text)
        msgBox.setIcon(msgBox.Icon.Information)
        msgBox.exec()
        self.display.setFocus()
