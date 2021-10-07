# -*- coding: utf-8 -*-

################################################################################
##
# Created by: Giovani M Castro version 1.0.2
##
################################################################################
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


def closeEvent(self, event):
    reply = QMessageBox.question(self, 'Sair', 'Deseja realmente sair?')

    if reply == QMessageBox.Yes:
        event.accept()
    else:
        event.ignore()


def sobre(self):
    msg = '''

        Sistema de apoio a produção.

        Desenvolvido por : N O C z Sistemas.

        versao : V 0.01 

        Site: www.rexxdevs.com
        '''
    sobre = QMessageBox()
    sobre.setFixedSize(100, 400)
    sobre.setText(msg)
    sobre.exec()


def help(self):

    texto = '''
    -Acesso ao manual do sistema 
    -Menu de navegação
    -Digite o código do evento no campo de busca 
    '''
    help = QMessageBox()
    help.setText(texto)
    help.exec()


def mousePressEvent(self, event):
    self.oldPos = event.globalPos()
    delta = QPoint(event.globalPos() - self.oldPos)
    self.move(self.x() + delta.x(), self.y() + delta.y())
    self.oldPos = event.globalPos()
