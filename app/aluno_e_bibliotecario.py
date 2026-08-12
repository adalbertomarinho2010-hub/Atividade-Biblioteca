from app.pessoa import Pessoa


class Aluno(Pessoa):
  def __init__(self, nome: str, cpf: str, matricula):
    super().__init__(nome, cpf)
    self.matricula = matricula

    return Aluno


class Bibliotecario(Pessoa):
   def __init__(self, nome: str, cpf: str, registro):
    super().__init__(nome, cpf)
    self.registro = registro

    return Bibliotecario


class Livro():
  def __init__(self, nome_livro, id_livro, autor, disponivel):
    super().__init__(nome_livro, id_livro, autor, disponivel)
    self.nome_livro = nome_livro
    self.id_livro = id_livro
    self.autor = autor
    self.disponivel = True


    def marcar_emprestado(self):
        self.disponivel = False
    
    def marcar_disponivel(self):
        self.disponivel = True

    return Livro

class Emprestimo():
   def __init__(self, nome_livro, id_livro, autor, disponivel, data, atraso):
    super().__init__(nome_livro, id_livro, autor, disponivel)
    self.data = data
    self.atraso = atraso


    def devolucao(self):
        if self.disponivel == False:
           nome: str

    def adicionar_data(self):
        nome: str

    def multa(self):
        nome: str