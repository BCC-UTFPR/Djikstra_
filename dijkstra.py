from collections import defaultdict
from heapq import *
import heapq_max as heap

def dijkstra(edges, f, t):
    g = defaultdict(list)
    # l -> de; r-> para; c->custo
    for l,r,c in edges:
        g[l].append((c,r))

    q, visitado = [(0,f,())], set()
    while q:
        (custo, v1, caminho) = heappop(q) #Função para o caminho máximo -> heap.pop_heap(q)
        if v1 not in visitado:
            visitado.add(v1)
            caminho = (v1, caminho)
            if v1 == t: return (custo, caminho)

            for c, v2 in g.get(v1, ()):
                if v2 not in visitado:
                    #Função para fazer o cálculo do caminho mínimo
                    heappush(q, (custo+c, v2, caminho))
                    #Função necessária para fazer o calculo do caminho máximo
                    heap.push_heap(q, (custo+c, v2, caminho))

    return float("inf")

if __name__ == "__main__":
    edges = []

    arquivo = open('prova.txt', 'r')
    linhas = arquivo.readlines()
    
    for i, linha in enumerate(linhas):
        
        rota = linha.split()
        if len(rota) > 1:
            lista = []
            lista.append(rota[0])
            lista.append(rota[1])
            lista.append(int(rota[2]))
            #lista.append(abs(int(rota[0])-int(rota[1])))
            edges.append(lista)


    '''edges = [
        ("A", "B", 7),
        ("A", "D", 5),
        ("B", "C", 8),
        ("B", "D", 9),
        ("B", "E", 7),
        ("C", "E", 5),
        ("D", "E", 15),
        ("D", "F", 6),
        ("E", "F", 8),
        ("E", "G", 9),
        ("F", "G", 11),
        ("E", "G", 1)
    ]'''

    print dijkstra(edges, '27078', '27081')
