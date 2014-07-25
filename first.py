import math
import random

random.seed()

def nextTime(mean):
    return -mean * math.log(1 - random.random())

def question1(alpha, maxi):
    avg,suma = 0,0
    for i in range(maxi):
        suma = suma + nextTime(alpha)
    avg = suma/maxi
    print avg

def question2(alpha, beta, maxi):
    sumq = 0.0
    for i in range(maxi):
       queuelist = []
       ta, ts, c, Q = nextTime(alpha), nextTime(beta), 0, 1
       
       # 8 hours = 480 minutes
       while (c <= 480):
           if (ta < ts):
               ts -= ta
               c += ta
               Q += 1
               ta = nextTime(alpha)
           else:
               ta -= ts
               c += ts
               Q -= 1
               ts = nextTime(beta)
           while (Q == 0):
               c += ta
               Q += 1
               ta = nextTime(alpha)
           queuelist.append(Q)
       #print average sum of max(queuelist)
       sumq = sumq + max(queuelist)
    print sumq/maxi

