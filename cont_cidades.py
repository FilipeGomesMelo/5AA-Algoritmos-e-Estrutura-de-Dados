import sys

dicio = {}

for line in sys.stdin:
    cidades = line.split(';')
    
    cidade1 = cidades[0].rstrip(' ')
    cidade2 = cidades[1].rstrip(' ')

    dicio[cidade1] = 1
    dicio[cidade2] = 1
    # print('{};{};{}'.format(cidade1, cidade2, ';'.join(cidades[2:])), end='')

for key in sorted(list(dicio.keys())):
    print(key)

print(len(dicio))