from veiculos import Veiculos
	
class Carro(Veiculos):

	def __init__(self, marca, cor, litros):
		Veiculos.__init__(self, 4, marca, cor, litros)