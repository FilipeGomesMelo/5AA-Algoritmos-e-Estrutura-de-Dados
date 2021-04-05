import sys       
from math import floor 
        
def main():

    class No:
        def __init__(self,p,k,i):
            self.peso = p
            self.chave = k
            self.index = i

    def parent(i):
        return floor((i-1)/2)

    def left(i):
        return 2*i+1

    def right(i):
        return 2*(i+1)

    def heapify(array,i,n):
        l = left(i)
        r = right(i)
        if l < n and array[l].peso < array[i].peso:
            menor = l
        else:
            menor = i
        if r < n and array[r].peso < array[menor].peso:
            menor = r
        if menor != i:
            array[i].index = menor
            array[menor].index = i
            array[i],array[menor]=array[menor],array[i]
            heapify(array,menor,n)
    
    def bubbleup(array,n):
        if n > 0 and n < len(array):
            pai = parent(n)
            if pai >=0 and array[pai].peso > array[n].peso:
                array[pai].index = n
                array[n].index = pai
                array[pai],array[n]=array[n],array[pai]
                bubbleup(array,pai)

    def extract_min(array,n):
        menorel = array[0]
        array[0] = array[n]
        array.pop()
        heapify(array,0,n)
        return menorel

    def dijkstra(source, target, n, mapa):
        distances = []
        previous = []
        vertices = []
        for i in range(n):
            previous.append(None)
            no = No(sys.maxsize,i,i)
            distances.append(no)
            vertices.append(no)
        distances[source].peso = 0
        bubbleup(distances,source)
        while len(distances) > 0:
            u = extract_min(distances,len(distances)-1)
            if u.chave == target:
                return u.peso
            for v in mapa[u.chave]:
                index = v[0]
                weight = v[1]
                if vertices[index].peso > u.peso + weight:
                    vertices[index].peso = u.peso + weight
                    previous[index] = u
                    bubbleup(distances,vertices[index].index)

    entrada = input().split()
    n = int(entrada[0])
    m = int(entrada[1])
    s = int(entrada[2])-1
    t = int(entrada[3])-1
    
    mapa = []
    for i in range(n):
        mapa.append([])

    for i in range(m):
        entrada = input().split()
        cid1 = int(entrada[0])-1
        cid2 = int(entrada[1])-1
        dist = int(entrada[2])
        mapa[cid1].append((cid2, dist))
        mapa[cid2].append((cid1, dist))

    d = dijkstra(t, s, n, mapa)
    print(d)

if __name__ == '__main__':
    main()
