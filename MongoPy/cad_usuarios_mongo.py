import sys
from pymongo import MongoClient
from PyQt5.QtWidgets import QApplication, QWidget,QLabel,QLineEdit, QVBoxLayout, QPushButton


client = MongoClient("mongodb://root:senac123@127.0.0.1:37452")


db = client.loga_db


class CadUsuarios(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(30,40,600,250)
        self.setWindowTitle("Cadastro de Uusarios")

        

        labelNomeUsuario = QLabel("Nome Usuario")
        self.editNomeUsuario = QLineEdit()

        labelSenha = QLabel("Senha")
        self.editSenha = QLineEdit()

        labelNivel = QLabel("Nivel de acesso")
        self.editNivel = QLineEdit()

        psbCadastro = QPushButton("Cadastrar")

        self.labelMsg = QLabel("Rua Coronel Luís Americano, 130 Tatuapé, São Paulo - SP, 03308-020")
        
        layout = QVBoxLayout()
        

        layout.addWidget(labelNomeUsuario)
        layout.addWidget(self.editNomeUsuario)

        layout.addWidget(labelSenha)
        layout.addWidget(self.editSenha)

        layout.addWidget(labelNivel)
        layout.addWidget(self.editNivel)


        layout.addWidget(psbCadastro)
        psbCadastro.clicked.connect(self.CadUs)

        layout.addWidget(self.labelMsg)

        self.setLayout(layout)
    
    def CadUs(self):
        usuario_id = db["usuario"].insert_one({"nomeusuario":self.editNomeUsuario.text(),"senha":self.editSenha.text(),"nivel":self.editNivel.text()}).inserted_id
        self.labelMsg.setText("Usuario Cadastrado")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    tela = CadUsuarios()
    tela.show()
    sys.exit(app.exec_())