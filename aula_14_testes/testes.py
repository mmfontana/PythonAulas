# Testando funcoes com assert

# assert sum([1,10,3]) == 6, 'Deveria ser seis'


def teste_soma():
	assert sum([1,10,3]) == 6, 'Deveria ser seis'

def teste_soma_tupla():
	assert sum(((1,10,3))) == 6, 'Deveria ser seis'


if __name__ == '__main__':
	teste_soma()
	teste_soma_tupla()
	print('Passaram todos os testes')
