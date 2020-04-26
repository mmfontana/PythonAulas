import operacoes_matematicas as om

def test_soma():
	assert 'Maycon' in om.soma('Maycon', ' Fontana'), 'ERRO!' 
	assert 'Maycon' not in om.soma('Maycon', ' Fontana'), 'ERRO!'
	assert type(om.soma(100, 1)) is int, 'Deveria ser 101'

def test_subtracao():
	assert om.subtracao(100, 10) == 90, 'Deveria ser 90' 
	# assert om.soma(100, 20) == 101, 'Deveria ser 101'



