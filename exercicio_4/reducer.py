#!/usr/bin/python3

import sys


lista_coste =[]

# Loop around the data
# It will be in the format key\tval
# Where key is the store name, val is the sale amount
#

for line in sys.stdin:
    data_mapped = line.strip()
    lista_coste.append(float(data_mapped))
    lista_coste.sort()
    
print(lista_coste[-1])
 
 
