from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox
from CadAluno import Ui_CadAlunos
import pymysql.cursors


class Banco:
    def __init__(self):
        self.conexao = pymysql.connect(host='localhost',
                                  user='root',
                                  password='',
                                  database='escola',
                                  cursorclass=pymysql.cursors.DictCursor)

    def listarAlunos(self):
        with self.conexao.cursor() as cursor:
            sql = "SELECT * FROM alunos"
            cursor.execute(sql)
            resultado = cursor.fetchall()
            return resultado


    def buscar_nome(self, nome):
        with self.conexao.cursor() as cursor:
            sql = "SELECT * FROM alunos WHERE Nome LIKE %s"
            cursor.execute(sql, (f"%{nome}%",))
            resultado = cursor.fetchall()
            return resultado



    def cadastrarAluno(self, nome, idade, curso):
        with self.conexao.cursor() as cursor:
            sql = "INSERT INTO alunos (Nome, Idade, Curso) VALUES (%s, %s, %s)"
            cursor.execute(sql, (nome, idade, curso))
            self.conexao.commit()

    def excluirAluno(self, matricula):
        with self.conexao.cursor() as cursor:
            sql = "DELETE FROM alunos WHERE Matricula = %s"
            cursor.execute(sql, (matricula,))
            self.conexao.commit()



    def editarAluno(self, matricula, nome, idade, curso):
        with self.conexao.cursor() as cursor:
            sql = "UPDATE alunos SET Nome = %s, Idade = %s, Curso = %s WHERE Matricula = %s"
            cursor.execute(sql, (nome, idade, curso, matricula))
            self.conexao.commit()




class Janela(QMainWindow, Ui_CadAlunos):
    def __init__(self):
        super().__init__()

        self.setupUi(self)
        self.carregarTabela()
        self.tb_alunos.cellClicked.connect(self.tabelaClick)
        self.btn_editar.setEnabled(False)
        self.btn_excluir.setEnabled(False)
        self.btn_novo.clicked.connect(self.inserir)
        self.btn_excluir.clicked.connect(self.excluir)
        self.btn_editar.clicked.connect(self.editar)
        self.txt_buscar.textChanged.connect(self.buscar)




    def limparCampos(self):
        self.txt_nome.setText("")
        self.txt_idade.setText("")
        self.txt_matricula.setText("")
        self.carregarTabela()

    def desabilitarBotoes(self):
        self.btn_excluir.setEnabled(False)
        self.btn_editar.setEnabled(False)

    def tabelaClick(self, row):
        matricula = self.tb_alunos.item(row, 0).text()
        nome = self.tb_alunos.item(row, 1).text()
        idade = self.tb_alunos.item(row, 2).text()
        curso = self.tb_alunos.item(row, 3).text()


        self.btn_excluir.setEnabled(True)
        self.btn_editar.setEnabled(True)

        self.txt_matricula.setText(matricula)
        self.txt_nome.setText(nome)
        self.txt_idade.setText(idade)



    def inserir(self):
        db = Banco()
        nome = self.txt_nome.text()
        idade = int(self.txt_idade.text())
        curso = self.cb_curso.currentText()

        db.cadastrarAluno(nome, idade, curso)
        QMessageBox.information(self,"Cadastro", "Aluno Cadastrado Com Sucesso!!")
        self.limparCampos()


    def excluir(self):

        res = QMessageBox.question(self,"Excluir Aluno", "Deseja realmente excluir o aluno?", QMessageBox.Yes | QMessageBox.Cancel)

        if res == QMessageBox.Yes:
            db = Banco()
            matricula = self.txt_matricula.text()
            db.excluirAluno(matricula)
            QMessageBox.information(self, "Cadastro", "Aluno Cadastrado Com Sucesso!!")
            self.limparCampos()
            self.desabilitarBotoes()


    def editar(self):
        db = Banco()
        matricula = self.txt_matricula.text()
        nome = self.txt_nome.text()
        idade = int(self.txt_idade.text())
        curso = self.cb_curso.currentText()

        res = QMessageBox.question(self, "Editar Aluno", "Deseja realmente editar o aluno?",
                                   QMessageBox.Yes | QMessageBox.Cancel)

        if res == QMessageBox.Yes:
            db.editarAluno(matricula, nome, idade, curso)
            self.limparCampos()
            self.desabilitarBotoes()

    def buscar(self):
        db = Banco()
        nome = self.txt_buscar.text()
        db.buscar_nome(nome)
        self.carregarTabela()


    def carregarTabela(self):
            db = Banco()

            if self.txt_buscar.text() == '':
                resultado = db.listarAlunos()
            else:
                resultado = db.buscar_nome(self.txt_buscar.text())

            linha = 0
            self.tb_alunos.setRowCount(len(resultado))
            for aluno in resultado:
                self.tb_alunos.setItem(linha, 0, QtWidgets.QTableWidgetItem(str(aluno["Matricula"])))
                self.tb_alunos.setItem(linha, 1, QtWidgets.QTableWidgetItem(aluno["Nome"]))
                self.tb_alunos.setItem(linha, 2, QtWidgets.QTableWidgetItem(str(aluno["Idade"])))
                self.tb_alunos.setItem(linha, 3, QtWidgets.QTableWidgetItem(aluno["Curso"]))
                linha += 1





app = QApplication([])
window = Janela()
window.show()
app.exec()


