import sys
from PySide6.QtGui import QColor, QPalette
from PySide6.QtWidgets import QApplication
from app.Tela_Inicial import TelaInicial

class Aplicacao:

    def __init__(self):
        self._app = QApplication(sys.argv)
        self.tela_inicial = TelaInicial()

    def executar(self) -> int:
        self.tela_inicial.show()
        return self._app.exec()