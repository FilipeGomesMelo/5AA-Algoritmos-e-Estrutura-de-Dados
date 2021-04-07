import random as rand
import datetime as time

rand.seed(time.time())

num_vertices = int(input('numero de cidades'))

edge_chance = int(input('chance de ter um onibus direto de uma cidade para a outra'))

lista = []

for i in range(num_vertices):
    for j in range(num_vertices):
        if i != j:
            num = rand.randint(1, 100)
            if num <= edge_chance:
                lista.append('{};{};{}'.format(i,j,rand.randint(1, 1000)))

print('FIM')

for i in range(num_vertices):
    for j in range(num_vertices):
        print('{};{}'.format(i,j))