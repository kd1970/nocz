# -*- coding: utf-8 -*-

################################################################################
##
# Created by: Giovani M Castro version 1.0.2
##
################################################################################
import sqlite3

global con, cursor


def conectDB():
    global con, cursor
    con = sqlite3.connect('suporte.sqlite3')

    if con:
        # print('Conectado com sucesso !')  # Teste sucesso conexao
        cursor = con.cursor()
    else:
        print('Ocorreu erro na conexão com o banco Verifique as credencias.')


def loadUsr(usuario, senha):
    conectDB()
    u = usuario
    s = senha
    #print('Dados passados para o model', u, s)
    data = cursor.execute(f"SELECT * FROM usuarios WHERE usuario ='{u}'")

    if data:
        for i in data:
            usuario = i[1]
            senha = i[2]
        #print(f'Usuario cadastrado no banco {usuario} e sua senha é {senha}')
        return usuario, senha

    else:
        return False
        #print("Usuário não cadastrado- Model msg")

    con.close()


def loadJob():  # Busca um job especifico

    conectDB()
    opcao = 'hasp100'
    sql = cursor.execute(
        f"SELECT * FROM jobs WHERE codigo LIKE '%{opcao}%'")
    return sql
    con.close()


def loadAll():  # Busca todos os jobs cadastrados na tabela
    conectDB()

    sql = cursor.execute(f"SELECT * FROM jobs")
    for i in sql:
        print(
            f'CÓDIGO :{i[1]} DESCRICAO: {i[2]} ACOES: {i[3]} OBSERVACOES : {i[4]}')
    con.close()


def loadImg():
    conectDB()
    # cursor.execute("INSERT INTO imgs (id , desc , path) VALUES (1,'logonoc','C:\\Users\21872\\Venv-umkxGo-h\\imgs')")

    sql = cursor.execute('SELECT * FROM imgs')
    for i in sql:
        print(i)
    con.close()
