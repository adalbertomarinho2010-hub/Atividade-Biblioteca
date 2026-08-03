from livro import Livro

class Biblioteca:

    def __init__(self):
        self.__livros=[]

    def adicionar(self, livro):
        self.__livros.append(livro)

    def listar(self):
        return self.__livros