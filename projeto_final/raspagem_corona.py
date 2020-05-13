from selenium import webdriver
import pandas as pd

class RaspagemCorona():

	def __init__(self):

		self.driver = webdriver.Chrome()
		self.driver.get('https://www.worldometers.info/coronavirus/')

	def RasparDados(self, pais, coluna):

		dado = self.driver.find_element_by_xpath('//*[@id="main_table_countries_today"]/tbody[1]/tr[{}]/td[{}]'.format(pais,coluna)).text
		
		return dado		

	def ParaDicionario(self, dados_pais, dict_final):

		dict_final[dados_pais[0]] = dict()

		dict_final[dados_pais[0]]['Total de Casos'] = dados_pais[1]
		dict_final[dados_pais[0]]['Novos Casos'] = dados_pais[2]
		dict_final[dados_pais[0]]['Total de Mortes'] = dados_pais[3]
		dict_final[dados_pais[0]]['Novas Mortes'] = dados_pais[4]
		dict_final[dados_pais[0]]['Total de Recuperados'] = dados_pais[5]
		dict_final[dados_pais[0]]['Casos Ativos'] = dados_pais[6]
		dict_final[dados_pais[0]]['Sério ou Crítico'] = dados_pais[7]
		dict_final[dados_pais[0]]['Total de Casos/1M População'] = dados_pais[8]
		dict_final[dados_pais[0]]['Mortes/1M População'] = dados_pais[9]
		dict_final[dados_pais[0]]['Total de Testes'] = dados_pais[10]
		dict_final[dados_pais[0]]['Testes/1M População'] = dados_pais[11]

		return dict_final

	def TratarString(self, dado):

		if ',' in dado:
			dado = dado.replace(',', '')

		if '+' in dado:
			dado = dado.replace('+', '') 

		if dado == '':
			dado = 0

		if 'N/A':
			#ATIVIDADE
		
		try:
			dado = int(dado)
		except:	
			pass

		return dado

class TratamentoDados():

	def ParaDataFrame(self, dict_final):

		df = pd.DataFrame(dict_final).T

		return df

	def ParaExcel(self, df):

		df.to_excel('out_corona.xlsx', sheet_name = 'analise_corona')

	# def GerarPorcentagem(self, coluna_dataframe):
		# ATIVIDADE
