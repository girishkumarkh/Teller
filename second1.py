import os
import sys

import math
import random

random.seed()

# arrival time basicially setted constant to 5(=alpha) (as given in question)
def arrivalTime():
    mean=5
    return -mean * math.log(1 - random.random())

# serving time for Consumer Class: (as default delared as 3 for consumers)
def serveTime1():
    return -3 * math.log(1 - random.random())

# serving time for Business Class: (mean is passed as argument)
def serveTime2(mean):
    return -mean * math.log(1 - random.random())

    
def main(bus,maxi):
    sumq1 = 0.0
    sumq2 = 0.0
    for i in range(maxi):
       queues1 = []
       queues2 = []
       fq=[]
       ta = arrivalTime()
       ts1 = serveTime1()
       ts2 = serveTime2(bus)
       c = 0
       Q1 = 1
       Q2 = 1
    
       while (c <= 480):
           # if time arrive is less for service time 1 and 2
           if (ta < ts1 and ta < ts2): # 2 BUSY CASE
               # if two tellers are busy so join the queue
              ts1 = ts1 - ta
              ts2 = ts2 - ta            
              c = c + ta    
              ta = arrivalTime()    
              if (Q1 < Q2):
                 Q1 = Q1 + 1
              else:
                 Q2 = Q2 + 1
           # if NOT  
           else:
               # time arrive > service time 1 and < service time 2
               if (ta > ts1 and ta < ts2): # 1 FREE and 1 BUSY CASE
                  ta = ta - ts1
                  c = c + ts1
                  Q1 = Q1 - 1
                  ts1 = serveTime1()
               # or time arrive < service time 1 and > service time 2
               elif (ta < ts1 and ta > ts2): # 1 BUSY and 1 FREE CASE
                  ta = ta - ts2
                  c = c + ts2
                  Q2 = Q2 - 1
                  ts2 = serveTime2(bus)
               # if not for above two cases. and checks whether service time for
               # 1 is greater than 2 and either cases 
               else:
                  if (ts1 > ts2):
                      ta = ta - ts2
                      c = c + ts2
                      ts2 = serveTime2(bus)
                  else:
                      ta = ta - ts1
                      c = c + ts2
                      ts1 = serveTime1()
                  Q1 = Q1 - 1
                  Q2 = Q2 - 1                      
                      
           # finally checks wheter the queue is empty
           if (Q1 == 0):
               # stops two queues to a new customer arrival
               if (Q2 > 0):
                   c = c + ta
                   ta = arrivalTime()
               Q1 = Q1 + 1
           if (Q2 == 0):
               c = c + ta
               Q2 = Q2 + 1
               ta = arrivalTime()
            
           queues1.append(Q1)
           queues2.append(Q2)
       fq.append(max(queues1))
       fq.append(max(queues2))
       sumq1 = sumq1 + min(fq)
    print sumq1/maxi
