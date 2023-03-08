import pandas as pd

read_file = open(r'/home/pippozord/Scrivania/anagrafica.txt')

lines = read_file.readlines();
list = []
list.append(lines[0])
lines = lines[1:]
i = 1

for line in lines:
    tmp = str(i);
    list.append('Giocatore' + tmp + ' ' + line)
    i = i+1;

print(list[0:3])

with open(r'/home/pippozord/Scrivania/Statistica/2023/superhero-datascience/content/data/Anagrafica.csv', 'w') as write_file:
    for line in list:
        write_file.write("%s" %line)    