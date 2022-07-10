import random

def stringToList(string):
    listRes = list(string.split(" "))
    return listRes

randLIST = []
with open('data/readTCP.txt', 'r') as file:
    lines = file.readlines()
    for line in lines:
        randLIST.append(line.strip())

randrand = []
LeNrAnDom = len(randLIST)
for x in range(LeNrAnDom):
    randrand.append(random.choice(randLIST))

with open('data/TRUErandomVPN.txt', 'w') as file:
    for x in range(LeNrAnDom):
        file.write(randrand[x])
        file.write("\n")

sTring = ""
with open('data/TRUErandomVPN.txt', 'r') as file:
    lines = file.readlines()
    for line in lines:
        sTring = sTring +' '+line.strip()

sTring = sTring[1:]
sTring = 'for value in '+sTring

with open('proton.sh', 'r') as target:
    lines = target.readlines()
    for line in lines:
        line = line.strip()
        rUn = open('proton-run.sh', 'a')
        if line.find('for value in ') > -1:
            line = sTring
            rUn.write(line)
            rUn.write('\n')
        else:
            rUn.write(line)
            rUn.write('\n')
        rUn.close()
