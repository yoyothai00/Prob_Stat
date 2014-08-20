import random
 
N = 10
c = 0

check = []

for i in range(N+1):
	check.append(0.0)

for j in range(N):
	for i in range(N):
	    head = random.random() >= 0.5
	    if head:
	        c += 1
	check[c] += 1
	c = 0

for i in range(N+1):
	print check[i]/N

print '-------------------------------'
print sum(check)
# print "Heads:",c
# print "Freq/N:",float(c)/N