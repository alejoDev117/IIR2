import os

file = open("reglas del automata.txt","r")
id = 1
for i in file:
    print(str(id) +"-"+ i)
    id +=1
file.close()