# import pymysql.cursors
# from PyQt5 import QtWidgets
# from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox, QTableWidget
# from CadAluno import Ui_CadAlunos

# class Banco:
#     def __init__(self):
#         self.conexao = pymysql.connect(host='localhost',
#                                   user='root',
#                                   password='',
#                                   database='escola',
#                                   cursorclass=pymysql.cursors.DictCursor)


#     def listarPorNome(self, nome):
#         with self.conexao.cursor() as cursor:
#             sql = "SELECT * FROM alunos WHERE Nome LIKE %s"
#             cursor.execute(sql, (f"%{nome}%",))
#             resultado = cursor.fetchall()
#             self.conexao.commit()

#             return resultado

#     def listarAlunos(self):
#         with self.conexao.cursor() as cursor:
#             sql = "SELECT * FROM alunos"
#             cursor.execute(sql)
#             resultado = cursor.fetchall()
#             self.conexao.commit()

#             return resultado

#     def inserirAluno(self, nome, idade, curso):
#         with self.conexao.cursor() as cursor:
#             sql = "INSERT INTO alunos (Nome, Idade, Curso) VALUES (%s, %s, %s)"
#             cursor.execute(sql, (nome, idade, curso))
#             self.conexao.commit()

#     def atualizarAluno(self, nome, idade, curso, matricula):
#         with self.conexao.cursor() as cursor:
#             sql = "UPDATE alunos SET Nome = %s, Idade = %s, Curso = %s WHERE Matricula = %s"
#             cursor.execute(sql, (nome, idade, curso, matricula))
#             self.conexao.commit()

#     def deletar(self, matricula):
#         with self.conexao.cursor() as cursor:
#             sql = "DELETE FROM alunos WHERE Matricula = %s"
#             cursor.execute(sql, (matricula,))
#             self.conexao.commit()





# class TelaAluno(QMainWindow, Ui_CadAlunos):
#     def __init__(self):
#         super().__init__()
#         self.setupUi(self)
#         self.btn_editar.setEnabled(False)
#         self.btn_excluir.setEnabled(False)
#         self.carregarTabela()
#         self.txt_buscar.textChanged.connect(self.carregarTabela)
#         self.btn_novo.clicked.connect(self.cadastrar)
#         self.btn_editar.clicked.connect(self.editar)
#         self.btn_excluir.clicked.connect(self.excluir)
#         self.tb_alunos.cellClicked.connect(self.tb_evento)

#     def tb_evento(self, row):
#         matricula = self.tb_alunos.item(row, 0).text()
#         nome = self.tb_alunos.item(row, 1).text()
#         idade = self.tb_alunos.item(row, 2).text()
#         curso = self.tb_alunos.item(row, 3).text()

#         self.txt_matricula.setText(str(matricula))
#         self.txt_nome.setText(nome)
#         self.txt_idade.setText(str(idade))
#         self.cb_curso.setCurrentText(curso)

#         self.btn_editar.setEnabled(True)
#         self.btn_excluir.setEnabled(True)


#     def excluir(self):
#         if self.txt_matricula == '':
#             QMessageBox.critical(self, "Erro", "O campo matricula deve estar preenchido")

#         else:
#             matricula = int(self.txt_matricula.text())
#             db = Banco()
#             resultado = QMessageBox.question(self, "Deletar", "Deseja excluir o aluno?",
#                                              QMessageBox.Yes | QMessageBox.No)

#             if resultado == QMessageBox.Yes:
#                 db.deletar(matricula)
#                 QMessageBox.information(self, "Excluir", "Aluno excluido com sucesso!")
#                 self.txt_nome.setText("")
#                 self.txt_idade.setText("")
#                 self.txt_matricula.setText("")
#                 self.btn_editar.setEnabled(False)
#                 self.btn_excluir.setEnabled(False)
#                 self.carregarTabela()


#     def editar(self):
#         if self.txt_nome.text() == '' or self.txt_idade.text() == '':
#             QMessageBox.critical(self, "Erro", "Preencha todos os campos")
#         else:
#             matricula = int(self.txt_matricula.text())
#             nome = self.txt_nome.text()
#             idade = int(self.txt_idade.text())
#             curso = self.cb_curso.currentText()


#             db = Banco()
#             resultado = QMessageBox.question(self, "Editar", "Deseja realmente editar o aluno?",
#                                              QMessageBox.Yes | QMessageBox.No)

#             if resultado == QMessageBox.Yes:
#                 db.atualizarAluno(nome, idade, curso, matricula)
#                 QMessageBox.information(self, "Editar", "Dados atualizados com sucesso!")
#                 self.txt_nome.setText("")
#                 self.txt_idade.setText("")
#                 self.txt_matricula.setText("")
#                 self.btn_editar.setEnabled(False)
#                 self.btn_excluir.setEnabled(False)
#                 self.carregarTabela()



#     def cadastrar(self):
#         if self.txt_nome.text() == '' or self.txt_idade.text() == '':
#             QMessageBox.critical(self, "Erro", "Preencha todos os campos")
#         else:
#             nome = self.txt_nome.text()
#             idade = int(self.txt_idade.text())
#             curso = self.cb_curso.currentText()
#             db = Banco()
#             db.inserirAluno(nome, idade, curso)

#             QMessageBox.information(self, "Cadastro", "Aluno Matriculado Com Sucesso!!")
#             self.carregarTabela()
#             self.txt_nome.setText("")
#             self.txt_idade.setText("")

#     def carregarTabela(self):

#         db = Banco()
#         if self.txt_buscar.text() == '':
#             resultado = db.listarAlunos()
#         else:
#             nome = self.txt_buscar.text()
#             resultado = db.listarPorNome(nome)

#         linha = 0
#         self.tb_alunos.setRowCount(len(resultado))
#         for aluno in resultado:
#             self.tb_alunos.setItem(linha, 0, QtWidgets.QTableWidgetItem(str(aluno['Matricula'])))
#             self.tb_alunos.setItem(linha, 1, QtWidgets.QTableWidgetItem(aluno['Nome']))
#             self.tb_alunos.setItem(linha, 2, QtWidgets.QTableWidgetItem(str(aluno['Idade'])))
#             self.tb_alunos.setItem(linha, 3, QtWidgets.QTableWidgetItem(aluno['Curso']))
#             linha += 1



# app = QApplication([])
# window = TelaAluno()
# window.show()
# app.exec()
