from selenium import webdriver

class RaspagemCorona():

	def __init__(self):

		self.driver = webdriver.Chrome()
		self.driver.get('https://www.worldometers.info/coronavirus/')

	def RasparDados(self):


		for i in range(4,41): # Ativiade: levar os dois for para fora 
			for j in range(1,13):
					

				data = self.driver.find_element_by_xpath('//*[@id="main_table_countries_today"]/tbody[1]/tr[{}]/td[{}]'.format(i,j)).text
				lista_data.append(data)
				print(type(data))
	
	
	# def ParaDicionario():

		# dicionario_data = {'eua': {numero_mortes: 10000, numero_casos: 20000}, 'italy': {numero_mortes: 10000, numero_casos: 20000}}	 
	

