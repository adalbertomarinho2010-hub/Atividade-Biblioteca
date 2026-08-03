import sys

from PySide6.QtWidgets import QApplication

from tela_livros import TelaLivros
from biblioteca import Biblioteca
from livro import Livro
from banco import Banco

app = QApplication(sys.argv)
biblioteca = Biblioteca()
banco = Banco()

for dados in banco.carregar_livros():

    livro = Livro(*dados)

    biblioteca.adicionar(livro)

janela = TelaLivros(biblioteca)

janela.show()

app.exec()