import pymysql
 
  
bd = pymysql.connect(host='localhost',
                         user='usuario',
                         password='usuario',
                         db='dados')
                          
# instancia um objeto cursor utilizando o método cursor
cursor = bd.cursor()


# Esta senteça SQL atualiza todas as linhas do banco.
# no caso so temos uma linha
 
sql = "UPDATE estados SET usuario = 'berti'"
 
try:
    # Execute o comando SQL
    cursor.execute(sql)
    # confirme
    bd.commit()
     
    
except:
    print ("Erro: Impossível atualizar")
    #cancela operações
    bd.rollback()

# fecha a conexão
bd.close()
