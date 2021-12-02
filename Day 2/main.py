
horizontal = 0
depth = 0
aim = 0

with open('Day 2/data') as f:    data = [i.strip() for i in f.readlines()]

for i in range(0,len(data)):
    instruction = data[i].split()
    direction = instruction[0]
    increment = int(instruction[1])

    if direction == "forward":
        horizontal += increment
        depth += (increment * aim)
    elif direction == "down":
        aim += increment
    elif direction == "up":
        aim -= increment


product = horizontal * depth
print(f"Horizontal: {horizontal}")
print(f"Depth: {depth}")
print(f"Product: {product}")