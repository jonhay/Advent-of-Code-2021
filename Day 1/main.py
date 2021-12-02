# Solution for https://adventofcode.com/2021/day/1
# By Jon Hay

previous_sum = -1
increasing = 0
data = []
sums = []

with open('Day 1/data') as f:    data = [int(i.strip()) for i in f.readlines()]

for index in range(2,len(data)):
    sums.append(data[index-2]+data[index-1]+data[index])

for sum in sums:
    
    if previous_sum > 0 and sum > previous_sum:
        increasing += 1
        
    previous_sum = sum
    

print(increasing)
