# Solution for https://adventofcode.com/2021/day/3
# By Jon Hay


gamma_bin = ""
epsilon_bin = ""
gamma_int = 0
epsilon_int = 0
o2_bin = ""
co2_bin = ""
o2_int = 0
co2_int = 0

with open('Day 3/data') as f:    data = [i.strip() for i in f.readlines()]

def count_ones(data_input):
    one_frequency_counter = [0,0,0,0,0,0,0,0,0,0,0,0,]
    for reading in data_input:
        for i in range(0,len(reading)):
            if reading[i] == "1":
                one_frequency_counter[i] += 1
    return one_frequency_counter

def get_significant_bits(counts_imput):
    significant_bits = ""
    for bit in range(0, len(counts_imput)):
        if counts_imput[bit] >= (len(data) / 2):
            significant_bits += "1"
        else:
            significant_bits += "0"
    return significant_bits

def invert_bin(bin_string):
    new_bit_string = ""
    for bit in range(0,len(bin_string)):
        if bin_string[bit] == "1":
            new_bit_string += "0"
        else:
            new_bit_string += "1"
    return new_bit_string

gamma_bin = get_significant_bits(count_ones(data))
epsilon_bin = invert_bin(gamma_bin)


print(f"Gamma Bin: {gamma_bin}")
print(f"Epsilon Bin: {epsilon_bin}")

gamma_int = int(gamma_bin,2)
epsilon_int = int(epsilon_bin,2)

print(f"Gamma Int: {gamma_int}")
print(f"Epsilon Int: {epsilon_int}")

power_consumption = gamma_int * epsilon_int

print(f"Power Consumption: {power_consumption}")

kept_data = []
def filter_data(data_input, select_for, bit_mask):
    print("start")
    new_list = []

    marker = 0
    con_count = 0
    new_counter = 0
    old_counter = 0
    previous_match = True

    for bit in range(0, len(bit_mask)):
        for reading in range(0, len(data_input)):
            data_bit = data_input[reading][bit]
            if data_bit == bit_mask[bit] and previous_match and con_counter :
                print("count")
                con_counter += 1
                marker = reading
                con_counter = bit
            else:
                con_counter = 0
            print(f"Count : {con_count}")

    return data_input[marker]

o2_bin = filter_data(data, "1", gamma_bin)
co2_bin = filter_data(data, "0", epsilon_bin)


print(f"o2 Bin: {o2_bin}")
print(f"co2 Bin: {co2_bin}")

print(f"o2 Int: {int(o2_bin,2)}")
print(f"co2 Int: {int(co2_bin,2)}")
