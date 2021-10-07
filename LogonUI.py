# -*- coding: utf-8 -*-

################################################################################
##
# Created by: Giovani M Castro version 1.0.2
##
################################################################################
import sys
import validar as v
from PyQt5 import uic
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import screens as s
status = False

class UiLogon(QMainWindow):

    def __init__(self):
        super(UiLogon, self).__init__()
        uic.loadUi('LogonUI.ui', self)

        self.setGeometry(350, 100, 450, 500)
        self.setWindowTitle('N O C z :: Logon')
        self.setWindowIcon(QIcon('imgs/eyes.png'))
        self.checkCad.hide()
        self.checkRec.hide()
        self.txtUser.setFocus()
        self.checkRec.stateChanged.connect(self.loadRec)
        #self.showMaximized()

        # ===========================================================================================
        self.btnOk.clicked.connect(self.logon)
        # ===========================================================================================

    def logon(self):
        global status
        status = False
        senha = self.txtPassword.text()
        usuario = self.txtUser.text()

        if usuario == '':
            aviso = QMessageBox()
            aviso.setText('Campo usuário vazio')
            aviso.exec()
            self.txtUser.setStyleSheet(
                "border-bottom: 1px solid rgba(85, 170, 255,87);color: rgb(61, 61, 91);")
            self.txtUser.setFocus()
            
        # ===============================================
        status = v.valida(usuario, senha)

        if status:

            msgok = QMessageBox()
            msgok.setIcon(QMessageBox.Information)
            msgok.setText(f"Bem Vindo {usuario}")
            msgok.setWindowTitle("Login !")
            msgok.setFixedSize(QSize(140, 40))
            msgok.exec()
            self.clearFields()
            self.close()

        else:
            msgNo = QMessageBox()
            msgNo.setIcon(QMessageBox.Critical)
            msgNo.setText("Dados Incorretos verifique !!!!")
            msgNo.setWindowTitle("Atenção")
            msgNo.setFixedSize(QSize(120, 40))
            msgNo.exec()
            self.checkRec.show()
            status = False
            self.clearFields()

    def clearFields(self):
        self.txtUser.setText("")
        self.txtPassword.setText("")

    def loadRec(self,e):
        self.close()
        s.LoadRecuperar()
        
        
            
    
def LoadLogin():

    app = QApplication.instance()
    if app is None:
        app = QApplication(sys.argv)
    window = UiLogon()
    window.show()
    app.exec()
    return status
