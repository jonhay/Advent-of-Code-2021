data = [int(x) for x in open('Day 7/data').read().strip().split(',')]
r = []

def cst(a):
	return a*(a+1)//2

for dest in range(min(data), max(data)+1):
	cost = sum([cst(abs(x-dest)) for x in data])
	r.append(cost)
print(min(r))