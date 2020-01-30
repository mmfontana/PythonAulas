from veiculos import Veiculos
from carro import Carro

# Estanciando classes

meu_veiculo = Veiculos(4, 'Ford', 'Gelo', 10)
gabriela_veiculo = Veiculos(2, 'Honda', 'Vermelho', 15)

gabriela_carro = Carro('Ferrari', 'Vermelha', 250)

# Acesando metodos e propriedades

#gabriela_veiculo.marcha_re()
#print(gabriela_veiculo.cor)

# Conferindo as classes e objetos

#print(meu_veiculo)
#print(gabriela_veiculo)
#print(type(meu_veiculo))
#print(type(gabriela_veiculo))

print(gabriela_veiculo.tanque)
gabriela_veiculo.encher_tanque(20)
print(gabriela_veiculo.tanque)