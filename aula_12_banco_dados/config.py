import json
import pymysql

# lemos o JSON em disco
config_file = open('config.json').read()
config_json = json.loads(config_file)
config = config_json[0]

bd = pymysql.connect(host=config['host'],
                         user=config['user'],
                         password=config['password'],
                         db=config['db'])
                          
# instancia um objeto cursor utilizando o método cursor
cursor = bd.cursor()

# gere uma consulta SQL solicitando a versão do banco de dados.
cursor.execute("SELECT VERSION()")

# Capture o resultado em uma única linha.
versao = cursor.fetchone()
print ("Versão do gerenciador Maria DB : %s " % versao)

# fecha a conexão
bd.close()

