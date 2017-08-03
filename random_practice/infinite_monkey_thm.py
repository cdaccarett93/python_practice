import random


def generate():
    randlist = ['a', 'b', 'c', 'd', 'e', 'f', 'g',
                'h', 'i', 'j', 'k', 'l', 'm', 'n',
                'o', 'p', 'q', 'r', 's', 't', 'u',
                'v', 'w', 'x', 'y', 'z', ' ']
    a = ""
    for i in range(28):
        a += random.choice(randlist)

    return a


def score(s, goal):
    numSame = 0
    looplen = len(goal)
    for i in range(looplen - 1):
        if s[i] == goal[i]:
            numSame += 1
        else:
            pass

    totalscore = numSame / looplen * 100

    return totalscore


def test(t):
    bestscore = 0
    counter = 0
    while bestscore != 100:
        counter += 1
        sstring = generate()
        currscore = score(sstring, t)
        if currscore > bestscore:
            beststring = sstring
            bestscore = currscore
        if counter > 1000000 and counter % 1000000 == 0:
            print(counter, bestscore, beststring)
    return beststring


goalstring = 'methinks it is like a weasel'

print(test(goalstring))
