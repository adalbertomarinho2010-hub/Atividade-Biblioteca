from item_biblioteca import itembiblioteca

class Livro(itembiblioteca):

    def __init__(self, titulo, autor, isbn):
        super().__init__(titulo)

        self.__autor = autor
        self.__isbn = isbn

    @property
    def autor(self):
        return self.__autor
    
    @property
    def isbn(self):
        return self.__isbn
    
    def tipo(self):
        return "Livro"