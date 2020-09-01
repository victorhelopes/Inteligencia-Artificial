#! /usr/bin/env python3

import random
import time

#action = gbc063.algoritmo(current, options)
def algoritmo_profundidade(obj,info,visitados,cont):
	time.sleep(1)
	if(cont == 100):
		return cont
	visitados.add(info[1])
	#print(visitados)
	for i in info[2]:
		atual = obj.move(i)
		if i not in visitados:
			algoritmo_profundidade(obj,atual,visitados,cont+1)

def  algoritmo(obj,info):
	visitados =set()
	algoritmo_profundidade(obj,info,visitados,0)
