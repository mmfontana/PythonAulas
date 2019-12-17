import csv


file = 'alunos_materia.csv'
data_alunos = []

with open(file) as csvfile:
	data  = csv.reader(csvfile, delimiter = ';')
	for row in data:
		data_alunos.append(row)

data_alunos = data_alunos[1:]
notas_media = []

for i in range(len(data_alunos)):
	notas_media.append((((float(data_alunos[i][2])+float(data_alunos[i][3])+float(data_alunos[i][4]))/3)))
	
notas_media_rounded = []
for i in range(len(notas_media)):
	notas_media_rounded.append(round(notas_media[i],2))


print(notas_media_rounded)
	












