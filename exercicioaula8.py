peso = input("Qual o seu Peso:")

altura = input("Qual a sua altura:")

IMC = peso / altura**2

if IMC < 16:
	print("Magreza grave")
elif 16 <= IMC < 17:
	print("Magreza moderada")
elif 17 <= IMC < 18.5:
	print("Magreza moderada")
elif 17 <= IMC < 18.5:
	print("Magreza Leve")
elif 18.5 <= IMC < 25:
	print("Saudavel")
elif 25 <= IMC < 30:
	print("Sobrepeso")
elif 30 <= IMC < 35:
	print("Obesidade grau 1")
elif 35 <= IMC < 40:
	print("Obesidade grau 2")
elif IMC >= 40:
	print("Obesidade grau 3")