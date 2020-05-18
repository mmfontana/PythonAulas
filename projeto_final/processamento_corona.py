from raspagem_corona import RaspagemCorona, TratamentoDados, TratamentoGrafico



if __name__ == '__main__':
	
	raspador = RaspagemCorona()

	paises_out = [5, 6, 18, 20]
	n_primeiro = 4 
	n_ultimo_pais = 34

	dict_final = dict()

	for pais in range(n_primeiro, n_ultimo_pais): 
		
		dados_pais = list()

		if pais not in paises_out:

			for coluna in range(1,15):
				dado = raspador.RasparDados(pais, coluna)
				dado = raspador.TratarString(dado)
				dados_pais.append(dado)

			dict_final = raspador.ParaDicionario(dados_pais, dict_final)

		else:

			pass

	tratamento = TratamentoDados()
	df = tratamento.ParaDataFrame(dict_final)
	tratamento.ParaExcel(df)

	print(df)
		
