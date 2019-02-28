import sys
from pprint import pprint
# wc -l
# 5 a_example.txt
# 80001 b_lovely_landscapes.txt
# 1001 c_memorable_moments.txt
# 90001 d_pet_pictures.txt
# 80001 e_shiny_selfies.txt
from random import choice, sample, shuffle


class Pic:
    def __init__(self, id, orient, tags):
        self.orient = orient
        self.tags = set(tags)
        self.id = id
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

# horiz_pics = sorted(horiz_pics, key=lambda x: len(x.tags))
# vert_pics = sorted(vert_pics, key=lambda x: len(x.tags))

#tag count code
# tags = set()
# for p in horiz_pics+vert_pics:
#     for t in p.tags:
#         tags.add(t)
#
# print(len(tags))
solution = []

keep_going = True
pic = choice(horiz_pics)
horiz_pics.remove(pic)
solution.append(pic)
#
fnl_score = 0
#
while keep_going:
    # print(len(horiz_pics))
    tags_sample = pic.tags # sample(pic.tags, max(int(.05*len(pic.tags)),1))

    my_sample = sample(horiz_pics, max(int(0.01*len(horiz_pics)),1))

    for p in my_sample:
        if len(p.tags.intersection(tags_sample))<len(tags_sample)*0.25: #play here
            if len(my_sample) <= 1:
                break
            my_sample.remove(p)

    best_score=0
    if len(my_sample) >= 1:
        next_pic = choice(my_sample)
        for p in my_sample:
            s = score(pic, p)
            if s>best_score:
                next_pic = p
                best_score =s

    horiz_pics.remove(next_pic)

    keep_going = len(horiz_pics)>0

    solution.append(next_pic)
    fnl_score+=score(pic,next_pic)
    pic = next_pic

shuffle(vert_pics)
for i in range(0,len(vert_pics),2):
    a = vert_pics[i]
    b = vert_pics[i+1]

    fnl_score+=score(a,b)
    solution.append([a,b])

print("SCORE {}".format(fnl_score))
out = open(sys.argv[1]+".output", "wt")
out.write("{}\n".format(int(len(solution))))

for p in solution:
    if isinstance(p, list):
        out.write("{} {}\n".format(p[0].id, p[1].id))
    else:
        out.write("{}\n".format(p.id))

# out.write("{}\n".format(int(len(horiz_pics) + len(vert_pics)/2)))
# for i in range(0,len(vert_pics), 2):
#     out.write("{} {}\n".format(vert_pics[i].id, vert_pics[i+1].id))
# for i in range(0,len(horiz_pics)):
#     out.write("{}\n".format(horiz_pics[i].id,))
