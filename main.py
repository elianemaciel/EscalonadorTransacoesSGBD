# -*- coding: utf-8 -*-


operacoes = {}

def twoPLStrict(h1):
    looks_r = []
    looks_w = []
    unlooks = []
    delay = []
    for t in h1:
        dado  = t.split('[')
        cont = False
        bloqueado = False
        # print delay
        for de in delay:
            if t[1] in de:
                delay.append(t)
                cont = True
                break
        if cont:
            continue

        if len(dado) > 1:
            dado = dado[1].replace(']', '')
            for look in looks_w:
                if dado in look and t[1] not in look:
                    bloqueado = True
                    break
            for look in looks_r:
                if dado in look and t[1] not in look:
                    bloqueado = True
                    break   
        if t.startswith('c') or t.startswith('a'):
            for look in looks_w:
                if t[1] in look:
                    looks_w.remove(look)
                    unlooks.append(t)
                    
            for look in looks_r:
                if t[1] in look:
                    looks_r.remove(look)
                    unlooks.append(t)
            print "Commit - %s" % t
                    
        else:
            
            if bloqueado:
                delay.append(t)
            else:
                if t[0] == 'w':
                    looks_w.append(t)
                elif t[0] == 'r':
                    looks_r.append(t)
                print t

    for op in delay:
        if op.startswith('c') or op.startswith('a'):
            print "Commit - %s" % op
        delay.remove(op)
    

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
    print "1 - Ler do arquivo"
    print "2 - Digitar a entrada"
    op = input("Digite a opção ")

    if op == 1:

        arq = open('testes.txt', 'r')
        
        for line in arq.readlines():
            lista = line.split()
            operacoes[lista[0]] = []
            for i in lista:
                if i != lista[0]:
                    operacoes[lista[0]].append(i)
       
        h1 = monta_history()        
    else:
        h1 = raw_input("Digite o valor da entrada:")
        h1 = h1.split()

    print "Historia - ", h1
    twoPLStrict(h1)


if __name__ == '__main__':
    main()