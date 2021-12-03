# Solution for https://adventofcode.com/2021/day/3
# By Jon Hay

gamma_rate_one_counter = [0,0,0,0,0,0,0,0,0,0,0,0,]
gamma_bin = ""
epsilon_bin = ""
gamma_int = 0
epsilon_int = 0

with open('Day 3/data') as f:    data = [i.strip() for i in f.readlines()]

for reading in data:
    for i in range(0,len(reading)):
        if reading[i] == "1":
            gamma_rate_one_counter[i] += 1


print(f"Number of Readings: {len(data)}")
print(f"One bit counts: {gamma_rate_one_counter}")

for bit in range(0, len(gamma_rate_one_counter)):
    if gamma_rate_one_counter[bit] < (len(data) / 2):
        gamma_bin += "0"
        epsilon_bin += "1"
    else:
        gamma_bin += "1"
        epsilon_bin += "0"


print(f"Gamma Bin: {gamma_bin}")
print(f"Epsilon Bin: {epsilon_bin}")

gamma_int = int(gamma_bin,2)
epsilon_int = int(epsilon_bin,2)

print(f"Gamma Int: {gamma_int}")
print(f"Epsilon Int: {epsilon_int}")

power_consumption = gamma_int * epsilon_int

print(f"Power Consumption: {power_consumption}")

