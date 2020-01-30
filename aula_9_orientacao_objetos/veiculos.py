class Veiculos():

	nacionalidade = 'Brasil'

	def __init__(self, rodas, marca, cor, litros):

		self.rodas = rodas
		self.marca = marca
		self.cor = cor
		self.tanque = litros

	def marcha_re(self):
		print('O carro esta dando re')

	def encher_tanque(self, abastecimento):
		self.tanque += abastecimento