# -*- coding: utf-8 -*-

################################################################################
##
# Created by: Giovani M Castro version 1.0.2
##
################################################################################
import LogonUI as l
import screens as s
import sys


def loadSys():
    
    status = l.LoadLogin()
    
    if status:
        s.loadMain()
    else:
        recStatus = s.LoadRecuperar() #Retorno do novo status apos dados invalidos 3x
        if recStatus:
            status = l.LoadLogin()
            if status:
                s.loadMain()
            else:
                sys.exit(0)    
        else:
            sys.exit(0)    
            
            
loadSys()
sys.exit(0)
