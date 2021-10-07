import sqlite3


class ConectaDB():
    
    def __init__(self):

        self.con = sqlite3.connect('C:\\Users\\21872\\Venv-umkxGo-h\\nocui\\suporte.sqlite3')
        
        if self.con:
            print('Conectado com sucesso !')
            self.cursor = self.con.cursor()
        else:
            print('Ocorreu erro na conexão com o banco Verifique as credencias.')
         
    def LoadUsr(self):
        
        #cursor.execute("INSERT INTO usuarios (id , email , senha) VALUES (2,'giovani@email.com','teste')")
        
        sql = self.cursor.execute('SELECT * FROM usuarios')
        for i in sql:
            print('Usuario cadastrado no banco %s e sua senha é %s' %i)
        self.con.close()    
        

    def loadJob(self):
                      
        #self.cursor.execute("INSERT INTO jobs (id , codigo , descricao , acoes , observacoes) VALUES (1,'$hasp100','jes liberou job para execucao no INTRD' ,'Sem necessidade de ação','rotina do JES2')")
        
        sql = self.cursor.execute('SELECT * FROM jobs')
        for i in sql:
            print(i)
        self.con.close()

    def loadImg(self):
               
        #cursor.execute("INSERT INTO imgs (id , desc , path) VALUES (1,'logonoc','C:\\Users\21872\\Venv-umkxGo-h\\imgs')")
               
        sql = self.cursor.execute('SELECT * FROM imgs')
        for i in sql:
            print(i)
        self.con.close()
        
if __name__=='__main__':
            
    usuarios = ConectaDB()     
    #usuarios.loadJob()   