
previous_reading = -1
increasing = 0
data = []

with open('data') as f:    data = [int(i.strip()) for i in f.readlines()]

for reading in data:
    
    if previous_reading > 0 and reading > previous_reading:
        increasing += 1
        
    previous_reading = reading
    

print(increasing)
