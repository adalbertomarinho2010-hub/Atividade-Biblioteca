from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QFrame, QLabel, QWidget, QVBoxLayout

LARGURA = 1800
ALTURA = 920

class TelaInicial(QWidget):
    def __init__(self):
        super().__init__()

        self.setObjectName("tela_inicial")
        self.setWindowTitle("Inicío")
        self.setFixedSize(LARGURA, ALTURA)

        layout = QVBoxLayout(self)
        layout.setContentsMargins(30,30,30,30)
        layout.setSpacing(0)
