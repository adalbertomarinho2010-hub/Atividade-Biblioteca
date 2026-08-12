import sys
from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, 
                             QHBoxLayout, QLabel, QLineEdit, QPushButton, 
                             QComboBox, QTableView, QMessageBox, QHeaderView,
                             QTabWidget)
from PySide6.QtCore import Slot, QDate, Qt
from PySide6.QtSql import QSqlDatabase, QSqlQuery, QSqlRelationalTableModel, QSqlRelation

class SistemaBiblioteca(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Gerenciador de Biblioteca - Controle de Cargos")
        self.resize(1000, 600)

        # Inicializa o banco de dados
        self.configurar_banco_dados()

        # Componente de Abas Principal
        self.abas = QTabWidget()
        self.setCentralWidget(self.abas)

        # Criação dos painéis das abas
        self.aba_cadastro = QWidget()
        self.aba_visualizacao = QWidget()

        # Adiciona as abas ao componente principal
        self.abas.addTab(self.aba_cadastro, "📌 Cadastrar Funcionário")
        self.abas.addTab(self.aba_visualizacao, "📊 Visualizar e Gerenciar")

        # Configura o conteúdo de cada aba
        self.montar_aba_cadastro()
        self.montar_aba_visualizacao()

        # Configurações do MVC (Model-View-Controller)
        self.configurar_modelo_tabela()
        self.carregar_combos_selecao()

        # Conexões de Sinais
        self.btn_cadastrar_usuario.clicked.connect(self.adicionar_usuario)
        self.btn_excluir_usuario.clicked.connect(self.remover_usuario)
        self.combo_cargos_filtro.currentIndexChanged.connect(self.ordenar_por_cargo_dropdown)

    def configurar_banco_dados(self):
        """Cria as tabelas relacionais de funcionários e cargos na memória."""
        self.db = QSqlDatabase.addDatabase("QSQLITE")
        self.db.setDatabaseName(":memory:") 
        if not self.db.open():
            QMessageBox.critical(None, "Erro de Conexão", "Não foi possível iniciar o banco.")
            sys.exit(1)

        query = QSqlQuery()
        query.exec("CREATE TABLE cargos (id INTEGER PRIMARY KEY AUTOINCREMENT, nome_cargo TEXT)")
        query.exec("""
            CREATE TABLE funcionarios (
                id INTEGER PRIMARY KEY AUTOINCREMENT, 
                nome TEXT, 
                cargo_id INTEGER, 
                data_cadastro TEXT
            )
        """)
        
        query.exec("INSERT INTO cargos (nome_cargo) VALUES ('Administrador')")
        query.exec("INSERT INTO cargos (nome_cargo) VALUES ('Bibliotecário')")
        query.exec("INSERT INTO cargos (nome_cargo) VALUES ('Assistente')")
        query.exec("INSERT INTO cargos (nome_cargo) VALUES ('Gerente')")

        query.exec("INSERT INTO funcionarios (nome, cargo_id, data_cadastro) VALUES ('Ana Silva', 2, '2026-08-12')")
        query.exec("INSERT INTO funcionarios (nome, cargo_id, data_cadastro) VALUES ('Carlos Souza', 1, '2026-08-12')")
        query.exec("INSERT INTO funcionarios (nome, cargo_id, data_cadastro) VALUES ('Beatriz Costa', 3, '2026-08-12')")

    def montar_aba_cadastro(self):
        """Estrutura os elementos visuais da aba de inclusão de novos registros."""
        layout = QVBoxLayout(self.aba_cadastro)
        layout.setSpacing(15)
        layout.addSpacing(20)

        # Campo de Nome
        layout_nome = QHBoxLayout()
        self.txt_novo_usuario = QLineEdit()
        self.txt_novo_usuario.setPlaceholderText("Digite o nome completo do funcionário...")
        layout_nome.addWidget(QLabel("Nome do Funcionário:"))
        layout_nome.addWidget(self.txt_novo_usuario)
        layout.addLayout(layout_nome)

        # Campo de Seleção de Cargo
        layout_cargo = QHBoxLayout()
        self.combo_cargos_cadastro = QComboBox()
        layout_cargo.addWidget(QLabel("Atribuir Cargo:"))
        layout_cargo.addWidget(self.combo_cargos_cadastro)
        layout.addLayout(layout_cargo)

        # Botão de Ação
        self.btn_cadastrar_usuario = QPushButton("Salvar Novo Funcionário")
        self.btn_cadastrar_usuario.setStyleSheet("background-color: #2ecc71; color: white; font-weight: bold; padding: 8px;")
        layout.addWidget(self.btn_cadastrar_usuario)
        
        layout.addStretch() # Empurra tudo para o topo de forma limpa

    def montar_aba_visualizacao(self):
        """Estrutura a tabela e as ações de exclusão e filtros."""
        layout = QVBoxLayout(self.aba_visualizacao)

        # Barra superior com ordenação e exclusão
        layout_topo = QHBoxLayout()
        self.combo_cargos_filtro = QComboBox()
        self.btn_excluir_usuario = QPushButton("Excluir Selecionado")
        self.btn_excluir_usuario.setStyleSheet("background-color: #e74c3c; color: white; font-weight: bold;")
        
        layout_topo.addWidget(QLabel("Ordenar por Cargo:"))
        layout_topo.addWidget(self.combo_cargos_filtro)
        layout_topo.addSpacing(50)
        layout_topo.addWidget(self.btn_excluir_usuario)
        layout.addLayout(layout_topo)

        # Elemento da Tabela
        self.tabela_emprestimos = QTableView()
        self.tabela_emprestimos.setSortingEnabled(True)
        self.tabela_emprestimos.setSelectionBehavior(QTableView.SelectRows)
        self.tabela_emprestimos.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        layout.addWidget(self.tabela_emprestimos)

    def carregar_combos_selecao(self):
        """Alimenta tanto o dropdown de cadastro quanto o de filtro visual."""
        self.combo_cargos_cadastro.clear()
        self.combo_cargos_filtro.clear()
        
        query = QSqlQuery()
        query.exec("SELECT id, nome_cargo FROM cargos")
        while query.next():
            nome = query.value("nome_cargo")
            id_cargo = query.value("id")
            self.combo_cargos_cadastro.addItem(nome, id_cargo)
            self.combo_cargos_filtro.addItem(nome, id_cargo)
    
    def configurar_modelo_tabela(self):
        """Ajusta a ponte relacional de dados para a exibição na tabela."""
        self.model = QSqlRelationalTableModel(self, self.db)
        self.model.setTable("funcionarios")
        self.model.setRelation(2, QSqlRelation("cargos", "id", "nome_cargo"))

        self.model.setHeaderData(0, Qt.Horizontal, "ID")
        self.model.setHeaderData(1, Qt.Horizontal, "Nome do Funcionário")
        self.model.setHeaderData(2, Qt.Horizontal, "Cargo")
        self.model.setHeaderData(3, Qt.Horizontal, "Data de Cadastro")

        self.model.select() 
        self.tabela_emprestimos.setModel(self.model)
    
    def ordenar_por_cargo_dropdown(self):
        """Ordena a listagem da tabela baseado no item selecionado no topo."""
        self.model.setSort(2, Qt.AscendingOrder)
        self.model.select()

    @Slot()
    def adicionar_usuario(self):
        """Cadastra o funcionário pegando as informações da aba correspondente."""
        nome_usuario = self.txt_novo_usuario.text().strip()
        id_cargo = self.combo_cargos_cadastro.currentData()
        
        if not nome_usuario:
            QMessageBox.warning(self, "Aviso", "O nome do funcionário não pode estar em branco.")
            return
            
        data_atual = QDate.currentDate().toString("yyyy-MM-dd")
        
        query = QSqlQuery()
        query.prepare("INSERT INTO funcionarios (nome, cargo_id, data_cadastro) VALUES (?, ?, ?)")
        query.addBindValue(nome_usuario)
        query.addBindValue(id_cargo)
        query.addBindValue(data_atual)
        
        if query.exec():
            QMessageBox.information(self, "Sucesso", f"Funcionário '{nome_usuario}' cadastrado!")
            self.txt_novo_usuario.clear() 
            self.model.select() # Mantém o modelo da tabela atualizado em segundo plano
            self.abas.setCurrentIndex(1) # Muda automaticamente para a aba de listagem para ver o resultado
        else:
            QMessageBox.critical(self, "Erro SQL", query.lastError().text())

    @Slot()
    def remover_usuario(self):
        """Deleta a linha selecionada de dentro do painel de visualização."""
        indices_selecionados = self.tabela_emprestimos.selectionModel().selectedRows()
        
        if not indices_selecionados:
            QMessageBox.warning(self, "Aviso", "Por favor, selecione um funcionário na tabela para excluí-lo.")
            return
            
        index = indices_selecionados[0]
        linha = index.row()
        
        confirmacao = QMessageBox.question(
            self, "Confirmar Exclusão", "Tem certeza de que deseja excluir o funcionário selecionado?",
            QMessageBox.Yes | QMessageBox.No, QMessageBox.No
        )
        
        if confirmacao == QMessageBox.Yes:
            self.model.removeRow(linha)
            self.model.submitAll()
            self.model.select()
            QMessageBox.information(self, "Sucesso", "Funcionário removido com sucesso!")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    janela = SistemaBiblioteca()
    janela.show()
    sys.exit(app.exec())
