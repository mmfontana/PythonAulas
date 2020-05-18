from selenium import webdriver
import plotly.express as px
import pandas as pd


class RaspagemCorona():

	def __init__(self):

		self.driver = webdriver.Chrome()
		self.driver.get('https://www.worldometers.info/coronavirus/')

	def RasparDados(self, pais, coluna):

		dado = self.driver.find_element_by_xpath('//*[@id="main_table_countries_today"]/tbody[1]/tr[{}]/td[{}]'.format(pais,coluna)).text
		
		return dado		

	def ParaDicionario(self, dados_pais, dict_final):

		dict_final[dados_pais[1]] = dict()

		dict_final[dados_pais[1]]['Total de Casos'] = dados_pais[2]
		dict_final[dados_pais[1]]['Novos Casos'] = dados_pais[3]
		dict_final[dados_pais[1]]['Total de Mortes'] = dados_pais[4]
		dict_final[dados_pais[1]]['Novas Mortes'] = dados_pais[5]
		dict_final[dados_pais[1]]['Total de Recuperados'] = dados_pais[6]
		dict_final[dados_pais[1]]['Casos Ativos'] = dados_pais[7]
		dict_final[dados_pais[1]]['Sério ou Crítico'] = dados_pais[8]
		dict_final[dados_pais[1]]['Total de Casos/1M População'] = dados_pais[9]
		dict_final[dados_pais[1]]['Mortes/1M População'] = dados_pais[10]
		dict_final[dados_pais[1]]['Total de Testes'] = dados_pais[11]
		dict_final[dados_pais[1]]['Testes/1M População'] = dados_pais[12]

		return dict_final

	def TratarString(self, dado):

		if ',' in dado:
			dado = dado.replace(',', '')

		if '+' in dado:
			dado = dado.replace('+', '') 

		if dado == '':
			dado = 0

		#if 'N/A':
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
	
	def LerExcel(self):

		df = pd.read_excel('_out_corona.xlsx')
		df.rename(columns={'Unnamed: 0':'Paises'},
                 inplace=True)
		#df = df.set_index('Paises')

		return df


class TratamentoGrafico():

	def PlotarBarrasComposto(self, df):
		
		pass