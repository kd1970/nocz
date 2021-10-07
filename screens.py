# -*- coding: utf-8 -*-

################################################################################
##
# Created by: Giovani M Castro version 1.0.2
##
################################################################################
from PyQt5 import QtCore, QtWidgets, QtGui, uic
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from qtpy.QtCore import *
import qtmodern.styles
import qtmodern.windows
import resources
import validar as mail
import LogonUI as l
import model as m
import themes as t
import actions
import sys

# =============================================================================================================
# ==      Janela principal da aplicação - MainWindow
# =============================================================================================================

class UiMain(QMainWindow):

    def __init__(self):

        super(UiMain, self).__init__()
        uic.loadUi('formui/MainApp.ui', self)

        self.showMaximized()
        self.setWindowIcon(QIcon('imgs/eyes.png'))
        self.setWindowIcon(QtGui.QIcon('imgs/arroba.png'))
        # self.setAttribute(Qt.WA_TranslucentBackground)
        self.actionLight.triggered.connect(self.lightTheme)
        self.actionDark.triggered.connect(self.darkTheme)
        self.actionZOs.triggered.connect(self.zosTheme)
        self.actionLaboratorio.triggered.connect(self.GoLab)
        self.actionSobre.triggered.connect(self.sobre)
        self.actionManuais.triggered.connect(self.help)
        # Eventos botoes da barra de navegacao
        self.btnRexx.clicked.connect(self.GoRexx)
        self.btnHome.clicked.connect(self.GoHome)
        self.btnJcl.clicked.connect(self.GoJcl)
        self.btnDB2.clicked.connect(self.GoDB2)
        self.btnUtils.clicked.connect(self.GoUtils)
        # self.btnLab.clicked.connect(self.GoLab)

    @Slot()
    def closeEvent(self, event):

        actions.closeEvent(self, event)

    def lightTheme(self):
        qtmodern.styles.light(QApplication.instance())
        t.light(self)

    def darkTheme(self):
        qtmodern.styles.light(QApplication.instance())
        t.dark(self)

    def zosTheme(self):
        qtmodern.styles.dark(QApplication.instance())
        t.zOS(self)

    def GoRexx(self):
        self.stackedWidget.setCurrentIndex(4)

    def GoHome(self):
        sql = m.loadJob()

        self.stackedWidget.setCurrentIndex(5)
        for i in sql:
            codigo = i[1]
            descricao = i[2]
            acoes = i[3]
            observacoes = i[4]
            print(f'O codigo é : {codigo} a descricao do evento é :{descricao} \n ações sugeridas :{acoes} - Observações :{observacoes} ')

    def sobre(self):
        actions.sobre(self)

    def help(self):
        actions.help(self)

    def GoDB2(self):

        self.stackedWidget.setCurrentIndex(0)

    def GoJcl(self):
        m.loadAll()
        self.stackedWidget.setCurrentIndex(3)

    def GoUtils(self):
        self.stackedWidget.setCurrentIndex(2)

    def GoLab(self):
        self.stackedWidget.setCurrentIndex(1)

    def MouseEvent(self, event):
        actions.mousePressEvent(self, event)


def loadMain():
    app = QApplication.instance()
    if app is None:
        app = QApplication(sys.argv)
    window = UiMain()
    window.show()
    app.exec()

# ===================================================================================================
# ==      Tela cadastrar novo usuário
# ===================================================================================================

class UiCad(QMainWindow):
    def __init__(self):

        super(UiCad, self).__init__()
        uic.loadUi('formui/formCadastrar.ui', self)

        self.setWindowIcon(QIcon('imgs/eyes.png'))
        self.setWindowIcon(QtGui.QIcon('imgs/arroba.png'))
        self.lblCadOk.hide()
        self.lblCadNo.hide()
        self.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.btnCadastrar.clicked.connect(self.LoadCadastrar)
        self.btnCadastrar_2.clicked.connect(self.ExitCad)

    def LoadCadastrar(self):
        # print('Load Cadastrar')   background-color: ;
        self.btnCadastrar.hide()
        self.btnCadastrar_2.show()
        self.lblCadOk.show()
        self.lblNome.setEnabled(False)
        self.lblEmail.setEnabled(False)
        self.lblNome.setText("")
        self.lblEmail.setText("")
        self.lblNome.setStyleSheet(
            "QLineEdit { background: rgba(255, 255, 127, 197)}")
        self.lblNome.setStyleSheet("border: 1px solid red")
        self.lblEmail.setStyleSheet(
            "QLineEdit { background: rgba(255, 255, 127, 197)}")
        self.lblEmail.setStyleSheet("border: 1px solid red")

    def ExitCad(self):
        self.close()


def LoadCadastro():
    app = QApplication.instance()
    if app is None:
        app = QApplication(sys.argv)
    window = UiCad()
    window.show()
    app.exec()

# ===================================================================================================
# ==      Tela Recuperar a senha do usuário
# ===================================================================================================
recStatus = False  #global retorna status (boolean) para o processo principal  
class UiRecup(QMainWindow):
    
    def __init__(self):
        
        global recStatus
        recStatus = ''              
        super(UiRecup, self).__init__()
        uic.loadUi('formui/formRecuperar.ui', self)
        self.show()
        self.setWindowIcon(QIcon('imgs/eyes.png'))
        self.setWindowIcon(QtGui.QIcon('imgs/arroba.png'))
        self.btnRecSair.hide()
        self.lblRecOk.hide()
        self.lblRecNo.hide()
        self.btnEnviar.clicked.connect(self.LoadEnviar)

    def LoadEnviar(self):
        global recStatus       
        
        email = self.txtGetEmail.text()
        ok = mail.validaMail(email)
        
        if ok:
            recStatus = True
            self.txtGetEmail.setText('')
            self.lblRecOk.show()
            self.btnEnviar.hide()
            self.TxtRecPass.hide()
            self.txtGetEmail.setStyleSheet(
                "QLineEdit { background: rgba(255, 255, 127, 197)}")
            self.txtGetEmail.setStyleSheet("border: 1px solid red")
            self.txtGetEmail.setEnabled(False)
            self.btnRecSair.show()
            return recStatus
        else:
            recStatus = False
            msg = QMessageBox()
            msg.setText('E-mail inválido.')
            msg.exec()
            self.txtGetEmail.setFocus()
            return recStatus


def LoadRecuperar():
    app = QApplication.instance()
    if app is None:
        app = QApplication(sys.argv)
    window = UiRecup()
    window.show()
    app.exec()
    return recStatus

#loadMain()
# LoadRecuperar()
# LoadCadastro
