# -*- coding: utf-8 -*-


operacoes = {}

def twoPLStrict(h1):
	looks = []
	unlooks = []
	delay = []
	for t in h1:
		dado  = t.split('[')
		cont = False
		for de in delay:
			if t[1] in de:
				delay.append(t)
				cont = True
		if cont:
			continue

		if len(dado) > 1:
			dado = dado[1].replace(']', '')
			for look in looks:
				if dado in look and t[1] not in look:
					bloqueado = True	
		bloqueado = False
		if t.startswith('c') or t.startswith('a'):
			for look in looks:
				if t[1] in look:
					looks.remove(look)
					unlooks.append(t)
		else:
			
			if not bloqueado:
				looks.append(t)
			else:
				delay.append(t)
		print delay
		print looks


def monta_history():
	# import ipdb; ipdb.set_trace()
	h1 = []
	for tran, op in operacoes.items():
		h1 += op
	import random
	random.shuffle(h1)
	
	for i in h1:
		if i.startswith('c'):
			h1.remove(i)
			indice = i[1]
			pos = ''
			for j in h1:
				if indice in j:
					pos = j
			posicao = h1.index(pos)
			h1.insert(posicao+1, i)
	return h1


def main():
    arq = open('testes.txt', 'r')
    
    for line in arq.readlines():
    	lista = line.split()
    	operacoes[lista[0]] = []
    	for i in lista:
    		if i != lista[0]:
    			operacoes[lista[0]].append(i)

    h1 = monta_history()
    twoPLStrict(h1)



if __name__ == '__main__':
    main()