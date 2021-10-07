import hashlib
import re
import model as m

# ================================  CHECK DE USUARIO NO BANCO ========================================


def valida(usuario, senha):

    data = m.loadUsr(usuario, senha)
    usuario = usuario
    password = senha

   # print(f'Dados retornados de validar {usuario} - {password}')

    db_password = data[1]
   # print('senha da variavel db_password', db_password)
    if (hashlib.md5(password.encode()).hexdigest() == db_password):
        return True
    else:
        #print('Dados Incorretos...')
        return False


# ========================  REGEX VALIDA E-MAIL =========================================================
regex = r'^([a-z0-9._-]+)@[^@]+$'
email = ''
#data = retorno.group(0)


def validaMail(email):
    email = email
    retorno = re.search(regex, email)
    if not retorno is None:

        return True
    else:
        return False

# ===================================================================================================
