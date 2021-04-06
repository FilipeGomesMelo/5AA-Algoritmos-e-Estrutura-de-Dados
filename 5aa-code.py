import sys       
from math import floor 
        
def main():
    def parent(i):
        return floor((i-1)/2)

    def left(i):
        return 2*i+1

    def right(i):
        return 2*(i+1)

    def heapify(array,i,n,distances,vertices):
        l = left(i)
        r = right(i)
        if l < n and distances[array[l]] < distances[array[i]]:
            menor = l
        else:
            menor = i
        if r < n and distances[array[r]] < distances[array[menor]]:
            menor = r
        if menor != i:
            vertices[array[i]] = menor
            vertices[array[menor]] = i
            array[i],array[menor]=array[menor],array[i]
            heapify(array,menor,n,distances,vertices)
    
    def bubbleup(array,n,distances,vertices):
        if n > 0 and n < len(array):
            pai = parent(n)
            if pai >=0 and distances[array[pai]] > distances[array[n]]:
                vertices[array[pai]] = n
                vertices[array[n]] = pai
                array[pai],array[n]=array[n],array[pai]
                bubbleup(array,pai, distances, vertices)

    def extract_min(array,n,distances, vertices):
        menorel = array[0]
        array[0] = array[n]
        array.pop()
        heapify(array,0,n,distances,vertices)
        return menorel

    def dijkstra(source, target):
        distances = {}
        previous = {}
        vertices = {}
        aux = 0
        for key in dicio_cidades.keys():
            previous[key] = None
            distances[key] = sys.maxsize
            vertices[key] = aux
            aux += 1
        distances[source] = 0
        heap = list(dicio_cidades.keys())
        bubbleup(heap, vertices[source], distances, vertices)
        while len(heap) > 0:
            u = extract_min(heap, len(heap)-1, distances, vertices)
            if u == target:
                return (distances[u], previous)
            elif distances[u] == sys.maxsize:
                return -1
            for v in dicio_cidades[u].keys():
                weight = dicio_cidades[u][v]
                if distances[v] > distances[u] + weight:
                    distances[v] = distances[u] + weight
                    previous[v] = u
                    bubbleup(heap, vertices[v], distances, vertices)

    dicio_cidades = {}
    # nomes = []
    # mapa = []
    # aux = 0

    while True:
        entrada = input()
        
        if entrada == 'FIM':
            break

        entrada = entrada.split(';')
        
        cidade1 = entrada[0]
        cidade2 = entrada[1]

        # print(cidade1,cidade2)

        if cidade1 not in dicio_cidades:
            dicio_cidades[cidade1] = {}
        if cidade2 not in dicio_cidades:
            dicio_cidades[cidade2] = {}


        dicio_cidades[cidade1][cidade2] = float(entrada[2])

    for key in dicio_cidades.keys():
        print(key)
        for key2 in dicio_cidades[key].keys():
            print('\t', key2, dicio_cidades[key][key2])
    
    while True:
        entrada = input()

        if entrada == 'FIM':
            break

        entrada = entrada.split(';')

        source = entrada[0]
        target = entrada[1]

        saida = dijkstra(source, target)

        if saida == -1:
            print('oops deu errado')
        else:
            d = saida[0]
            p = saida[1]

            print(d)

            aux = p[target]

            print(target, end = ' ')

            while aux != None:
                print(aux, end=' ')
                aux = p[aux]

    # d = dijkstra(t, s, n, mapa)
    # print(d)

if __name__ == '__main__':
    main()
