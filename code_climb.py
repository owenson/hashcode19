import sys
from copy import copy
from pprint import pprint
from random import shuffle, randint


class Pic:
    def __init__(self, id, orient, tags):
        self.orient = orient
        self.tags = set(tags)
        self.id = id
    # def merge(self, p):
    #     self.tags.add(p.tags)
    #     self.id = [ self.id, p.id ]
    # def getOutput(self):
    #     return ' '.join(self.id)
    def __repr__(self):
        return self.orient + " " + ' '.join(self.tags)

def score(pic_a, pic_b):
    un = pic_a.tags.intersection(pic_b.tags)
    diff_a = pic_a.tags.difference(pic_b.tags)
    diff_b = pic_b.tags.difference(pic_a.tags)
    # print (len(un), len(diff_a), len(diff_b))
    return min(len(un), len(diff_a), len(diff_b))

horiz_pics = []
vert_pics = []

###PARSE
f = open(sys.argv[1], "rt")
n = f.readline()
i=0
for l in f:
    (orient, n) = l.strip().split(" ")[:2]
    tags = l.strip().split(" ")[2:]
    if orient == "H":
        horiz_pics.append(Pic(i, orient, tags))
    else:
        vert_pics.append(Pic(i, orient, tags))
    i+=1

def writeout():
    out = open(sys.argv[1]+".output", "wt")
    out.write("{}\n".format(int(len(horiz_pics) + len(vert_pics)/2)))
    for i in range(0,len(vert_pics), 2):
        out.write("{} {}\n".format(vert_pics[i].id, vert_pics[i+1].id))
    for i in range(0,len(horiz_pics)):
        out.write("{}\n".format(horiz_pics[i].id,))

shuffle(horiz_pics)
solution=horiz_pics
lastScore = 0
while True:
    oldSolution = copy(solution)
    # shuffle(horiz_pics)

    for i in range(int(len(solution)*.05)):

        a = randint(0,len(solution)-1)
        b = randint(0,len(solution)-1)
        tmp = solution[b]
        solution[b] = solution[a]
        solution[a] = tmp
    fscore = 0
    for i in range(1,len(solution)):
        fscore += score(solution[i-1], solution[i])
    print(fscore, lastScore)
    if fscore < lastScore:
        solution = oldSolution
    else:
        lastScore = fscore
        writeout()

