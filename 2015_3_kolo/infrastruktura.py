class Povezani:
    def __init__(self, mnozica):
        self.mesta = mnozica
    def dodaj(self, mesto):
        self.mesta.add(mesto)
    def je_notri(self, mesto):
        return (mesto in self.mesta)
    def zdruzi(self, other):
        return Povezani(self.mesta | other.mesta)

from sys import stdin

pov = []

for line in stdin:
    line = line.strip('\n')
    m1, m2 = line.split(' ')

    if pov == []:
        pov.append(Povezani({m1, m2}))
    else:
        ind = -1
        for i in range(len(pov)):
            if pov[i].je_notri(m1) and pov[i].je_notri(m2):
                ind = 1
                break
            elif pov[i].je_notri(m1) or pov[i].je_notri(m2):
                if ind == -1:
                    ind = i
                    pov[i].dodaj(m1)
                    pov[i].dodaj(m2)
                else:
                    pov[ind] = pov[ind].zdruzi(pov[i])
                    pov.pop(i)
                    break
        if ind == -1:
            pov.append(Povezani({m1, m2}))

if len(pov) == 1:
    print("")
else:
    a = pov[0].mesta.pop()
    for i in range(1, len(pov)):
        print(a, pov[i].mesta.pop(), sep=' ', end = '\n')
