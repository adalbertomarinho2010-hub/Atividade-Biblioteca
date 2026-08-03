from PySide6.QtWidgets import *
from PySide6.QtCore import Qt

class TelaLivros(QMainWindow):

    def __init__(self, biblioteca):
        super().__init__()

        self.biblioteca = biblioteca
        self.setWindowTitle("Biblioteca")
        self.resize(100, 600)
        self.tabela = QTableWidget()
        self.tabela.setColumnCount(3)

        self.tabela.setHorizontalHeaderLabels([
            "Título",
            "Autor",
            "ISBN"
        ])

        self.setCentralWidget(self.tabela)

        self.carregar()

    def carregar(self):

        livros = self.biblioteca.listar()

        self.tabela.setRowCount(len(livros))

        for linha, livro in enumerate(livros):

            self.tabela.setItem(linha, 0, QTableWidgetItem(livro.titulo))
            self.tabela.setItem(linha, 1, QTableWidgetItem(livro.autor))
            self.tabela.setItem(linha, 2, QTableWidgetItem(livro.isbn))