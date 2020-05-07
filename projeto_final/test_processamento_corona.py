from raspagem_corona import RaspagemCorona

def test_raspagem_corona():
	
	raspador = RaspagemCorona()
	assert raspador.RasparDados() == 'rodou', 'Erro ao rodar'
	


 