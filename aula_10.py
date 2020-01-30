from datetime import *
from dateutil.relativedelta import *
import calendar

# Trabalhando com datetime e dateutil

NOW = datetime.now()
#print(NOW)

TODAY = date.today()
#print(TODAY)

next_month = NOW + relativedelta(months=+1, weeks=+1, hours =+2)
#print(next_month)

next_month = (NOW + relativedelta(days =-1))  + relativedelta(months=+1, weeks=+1, hours =+2)
#print(next_month)

next_sexta = NOW  + relativedelta(weekday=FR)
#print(next_sexta)

# Resolvendo exercicio 1

def soma_imposto(custo_item, taxa_imposto):
	#custo_pos_imposto = custo_item + (taxa_imposto * custo_item)/100 
	custo_pos_imposto = custo_item * (1 + (taxa_imposto/100))  
	return custo_pos_imposto

def soma_imposto(custo_item, taxa_imposto):
	#custo_pos_imposto = custo_item + (taxa_imposto * custo_item)/100 
	return custo_item * (1 + (taxa_imposto/100))  
	 



print(soma_imposto(100, 10))
