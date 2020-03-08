import pymysql
 
bd = pymysql.connect(host='localhost',
                         user='usuario',
                         password='usuario',
                         db='dados')
                          
# instancia um objeto cursor utilizando o método cursor
cursor = bd.cursor()

# gere uma consulta SQL solicitando a versão do banco de dados.
cursor.execute("SELECT VERSION()")

# Capture o resultado em uma única linha.
versao = cursor.fetchone()
print ("Versão do gerenciador Maria DB : %s " % versao)

# fecha a conexão
bd.close()
 
