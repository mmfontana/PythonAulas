import pymysql
 

# Abrindo uma conexão com o banco de dados
  
bd = pymysql.connect(host='localhost',
                         user='usuario',
                         password='usuario',
                         db='dados')
                          
# instancia um objeto cursor utilizando o método cursor
cursor = bd.cursor()

# Esta senteça SQL apaga a linha correspondente à empresa 1.
sql = "DELETE FROM estados WHERE sigla = 'SC'"
 
try:
    # Execute o comando SQL
    cursor.execute(sql)
    # confirme
    bd.commit()
     
    
except:
    print ("Erro: Impossível apagar esta linha")
    #cancela operações
    bd.rollback()

# fecha a conexão
bd.close()