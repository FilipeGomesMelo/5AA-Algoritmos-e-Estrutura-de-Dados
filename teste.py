f = open("Datasets/1002.csv", "r")

file = f.read().split('\n')

for line in file:
    print(line)