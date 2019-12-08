# Utilizando input

idade = input('Qual sua idade:')
if int(idade) >= 18:
	print("Você é maior de idade")
else:
	print("Você é menor de idade")
print(idade)
print(type(idade))

# Trabalhando com tuplas

coordenadas = (22.1, 57.3, 18,9)
#print(type(coordenadas))
coordenadas_calc = 12.1, 12,7, 12,6
#print(type(coordenadas_calc))
nomes = ('cristovan', 'adao', 'joao', 'maria', 'jose', 'jesus', 'joao', 'jose')
#print(type(nomes))

# Usando metodos de tuplas
# Count
numero = nomes.count('joao')
#print(numero)
# Index
indice = nomes.index('jose')
#print(indice)

# Usando built-in functions
maximo = max(nomes)
#print(maximo)

# Usando funcao tuple
print(tuple([1,2,3]))
print(tuple('Maycon'))

