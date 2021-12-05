# Solution for https://adventofcode.com/2021/day/3
# By Jon Hay
from collections import Counter

data = [x for x in open('Day 3/data').read().strip().split('\n')]

gamma = ''
epsilon = ''
for bit in range(len(data[0])):
	common = Counter([x[bit] for x in data])

	if common['0'] > common['1']:
		data = [x for x in data if x[bit] == '0']
	else:
		data = [x for x in data if x[bit] == '1']
	gamma = data[0]

data = [x for x in open('Day 3/data').read().strip().split('\n')]
for bit in range(len(data[0])):
	common = Counter([x[bit] for x in data])

	if common['0'] > common['1']:
		data = [x for x in data if x[bit] == '1']
	else:
		data = [x for x in data if x[bit] == '0']
	if data:
		epsilon = data[0]
print(int(gamma,2)*int(epsilon,2))