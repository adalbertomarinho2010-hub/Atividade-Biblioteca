import sys
from PySide6.QtGui import QColor, QPalette
from PySide6.QtWidgets import QApplication
from app.Tela_Inicial import TelaInicial
from app.estilos import Cores, Estilos

class Aplicacao:

    def __init__(self):
        self._app = QApplication(sys.argv)
        self.tela_inicial = TelaInicial()

    def tema_estilos(self) -> None:
        self._app.setStyle("Fusion")
        self._app.setStyleSheet(Estilos)

        paleta = self._app.palette()
        paleta.setColor(QPalette.PlaceholderText,QColor(Cores.Placeholder))
        self._app.setPalette(paleta)

    def executar(self) -> int:
        self.tela_inicial.show()
        return self._app.exec()