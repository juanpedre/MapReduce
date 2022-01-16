#!/usr/bin/python3

import sys

maximo=0.0
diccionario = {}

# Loop around the data
# It will be in the format key\tval
# Where key is the store name, val is the sale amount
#

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        continue
    tarjeta, coste = data_mapped
    (diccionario.setdefault(tarjeta,[])).append(coste)

for tarjeta in diccionario: 
    lista =diccionario[tarjeta] 

    for i in lista:
    	if float(i) >= maximo:
    	   maximo = float (i) 
    print(tarjeta,"\t",maximo)
    maximo=0.0   	

