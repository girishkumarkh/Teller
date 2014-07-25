import os
import sys

import math
import random

random.seed()

# arrival time basicially setted constant to 10
def arrivalTime():
    mean=10
    return -mean * math.log(1 - random.random())

# serving time for Consumer Class: (as default delared as 6 for consumers)
def serveTime():
    return -6 * math.log(1 - random.random())

    
def main(maxi):
    sumq = 0.0
    for i in range(maxi):
       queues = []
       fq=[]
       ta = arrivalTime()
       ts1 = serveTime()
       ts2 = serveTime()
       c = 0
       Q = 1
    
       while (c <= 480):
           # if time arrive is less for service time 1 and 2
           if (ta < ts1 and ta < ts2):
               # if two tellers are busy so join the queue
              ts1 = ts1 - ta
              ts2 = ts2 - ta            
              c = c + ta    
              ta = arrivalTime()    
              Q = Q + 1
           # if NOT  
           else:
             # time arrive > service time 1
             # one teller is free to do service
              if (ta > ts1):
                 if (ts1 < ts2):
                    ta = ta - ts1
                    c = c + ts1
                 else:
                    ta = ta - ts2
                    c = c + ts2
                 ts1 = serveTime()
                 Q = Q - 1
               # or time arrive > service time 2
              if (ta > ts2):
                  if (ts1 < ts2):
                     ta = ta - ts1
                     c = c + ts1
                  else:
                     ta = ta - ts2 
                     c = c + ts2
                  ts2 = serveTime()
                  Q = Q - 1
                  
           # finally checks wheter the queue is empty
           while (Q <= 0):
               c = c + ta
               Q = Q + 1
               ta = arrivalTime()
            
           queues.append(Q)
       sumq = sumq + max(queues)
    print sumq/maxi
