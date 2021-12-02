
horizontal = 0
depth = 0

with open('Day 2/data') as f:    data = [i.strip() for i in f.readlines()]

for i in range(0,len(data)):
    instruction = data[i].split()
    direction = instruction[0]
    increment = int(instruction[1])

    if direction == "forward":
        horizontal += increment
    elif direction == "down":
        depth += increment
    elif direction == "up":
        depth -= increment


product = horizontal * depth
print(f"Horizontal: {horizontal}")
print(f"Depth: {depth}")
print(f"Product: {product}")