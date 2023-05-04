from math import exp

x = 10
tau = 100
s = 0.09

def d(x):
   return - x/tau + s 


for idx in range(500):
    x = x + d(x)
    print(x)
