 
import pymysql
 
# Abrindo uma conexão com o banco de dados
  
bd = pymysql.connect(host='localhost',
                         user='usuario',
                         password='usuario',
                         db='dados')
                          
# instancia um objeto cursor utilizando o método cursor
cursor = bd.cursor()


# construção da string SQL que insere um registro.
sql = """
INSERT INTO estados(sigla, nome, usuario) 
VALUES ('SC', 'Santa Catarina', 'lisangelo')
"""

try:
    # Execute o comando
    cursor.execute(sql)
    # Confirme a inserção na base de dados
    bd.commit()

except:
    # limpe tudo se algo saiu errado
    bd.rollback()
    print("Erro na inserção de dados na tabela de estados")

# fecha a conexão
bd.close()