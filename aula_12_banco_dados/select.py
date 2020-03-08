import pymysql
 
 
# Abrindo uma conexão com o banco de dados
  
bd = pymysql.connect(host='localhost',
                         user='usuario',
                         password='usuario',
                         db='dados',
                         cursorclass=pymysql.cursors.DictCursor)
                          
# instancia um objeto cursor utilizando o método cursor
cursor = bd.cursor()


# Esta senteça SQL seleciona toda a tabela tb_fornecedores.
sql = "SELECT * FROM estados"
 
try:
    # Execute o comando SQL
    cursor.execute(sql)
    # le todas as linhas da tabela.
    registros = cursor.fetchall()
     
    print (registros)
     
    for reg in registros:
        codigo = reg['id']
        nome = reg['nome']
        sigla = reg['sigla']
        usuario = reg['usuario']
     
    # imprima, no terminal, os valores lidos de interesse
        print ("Código: ", codigo)
        print ("Nome: ", nome)
        print ("Sigla :", sigla)
        print ("Usuário :", usuario)
         
         
except:
    print ("Erro: Impossível obter dados")


# fecha a conexão
bd.close()