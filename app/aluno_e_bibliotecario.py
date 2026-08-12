from app.pessoa import Pessoa


class Aluno(Pessoa):
    def __init__(self, nome, cpf):
        super().__init__(nome, cpf)

class Bibliotecario():
    nome: str


class Livro:
    nome: str
    id: str
    categoria: str
    autor: str
    status: str

    def marcar_emprestado():
        nome:str
    
    def marcar_disponivel():
        nome:str

class Emprestimo:
    def devolucao():
        nome: str

    def adicionar_data():
        nome: str

    def multa():
        nome: str