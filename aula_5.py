# Metodos de lista

# Usando append
bancos = ['bradesco', 'banco do brasil', 'itau']
bancos.append('nubank')
bancos_do_centro = bancos
#print(bancos_do_centro)

# Usando extend
precos = [12.1,13.4,12.7,98.3]
nome = 'maycon'
precos.extend(nome)
#print(precos)

# Usando insert
animais = ['cachorro','gato','rinoceronte','gato']
animais.insert(0,'girafa')
#print(animais)

# Usando remove
animais.remove('gato')
#print(animais)

# Usando pop
animais.pop(1)
#print(animais)

# Usando clear
animais.clear()
#print(animais)
#print(type(animais))

# Usando index
frutas = ['maca','morango','carambola','tamarindo']
indice = frutas.index('tamarindo')
#print(indice)
#print(len(frutas))
#print(len('cadeira'))

# Usando sort

frutas.sort(key=None,reverse=False)
#print(frutas)


# Usando sort

idades = [2,7,78,3,54,5,2]

idades.sort(reverse=True)
#print(idades)

# Usando reverse

objetos = ['vitor', 233, 'larissa', 12.4]
objetos.reverse()
#print(objetos)

# Usando copy

a = objetos.copy()
#print(a)

a = objetos

# Exercicios

# Somando notas

'''
notas = [8, 7, 5, 4, 3, 2, 1 ,10, 5]

soma = 0

for nota in notas:
	soma += nota

print(soma)
'''

# Tirando duplicadas
'''
notas = [7, 7, 5, 2, 8, 10, 8, 7, 3, 3, 10, 2, 5, 10, 5]

valores_unicos = []

for nota in notas:
	if nota not in valores_unicos:
		valores_unicos.append(nota) 
'''

# Comprimento dos Strings

series = ['strange things', 'suits', 'friends', 'revenge']
contador_maior = 0
contador_menor = 0

for serie in series:
	if len(serie) > 5:
		contador_maior += 1
contador_menor = len(series)-contador_maior

print(contador_maior)
print(contador_menor)


















































