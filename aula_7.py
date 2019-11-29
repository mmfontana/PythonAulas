# Exercicio funcao

def delta(a, b, c):
	x = (b**2)-(4*a*c)
	return x 

resultado = delta(1,10,20)
#print(resultado)   

# Metodos para String

# Usaindo lower
cliente = "MAYCON"
cliente = cliente.lower()
#print(cliente)

# Usando upper
animal = 'ornitorrinco_voador'
primeira_letra = animal[0].upper()
palavra = primeira_letra + animal[1:]
#print(palavra)

# Usando strip
fruta = '  abacaxi '
#print(len(fruta))
a = fruta.strip()
#print(len(a))

# Usando isalpha
aluno = 'Anderson'
#print(aluno.isalpha())

# Usando isdigit
distancia = '550km'
#print(distancia.isdigit()) 

# Usando isspace
nome = "\t"
#print(nome.isspace())

# Usando startswith
cliente = 'Antonio'
#print(cliente.startswith('Ant'))

# Usando startswith
cliente = 'Antonio'
#print(cliente.endswith('Antonio'))

# Usando find
cliente = 'Antonio'
#print(cliente[cliente.find('nto')])

# Usando replace
cliente = 'Antonio'
#print(cliente.replace('An', 'On'))

# Usando split
aluno = 'Maycon Machado Fontana'
#print(aluno.split('a'))

# Usando join
alunos = ['Caio', 'Vittor', 'Larissa', 'Gabriela']
virg = ","
for aluno in alunos:
	a = virg.join(alunos)
#print(a)
#print(type(a))

# Usando format
saudacao = 'Ola Larissa'
alunos = ['Caio', 'Vittor', 'Larissa', 'Gabriela']
for aluno in alunos:
	print("Boa noite {1}. Ate a proxima {0}. Na aula do dia {2} ".format(aluno, 'terca-feira', 3))
























