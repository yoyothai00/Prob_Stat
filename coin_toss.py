import random
 
N = 100
c = 0
for i in range(N):
    head = random.random() >= 0.5
    if head:
        c += 1
 
print "Heads:",c
print "Freq/N:",float(c)/N