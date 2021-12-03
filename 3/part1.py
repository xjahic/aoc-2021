zero_counter = {}
num_lines = 0

with open("input.txt") as f:
    for line in f:
        line = line.rstrip()
        for i in range(0, len(line)):
            zero_counter[i] = zero_counter.get(i, 0) + (1 if int(line[i]) == 0 else 0)
        num_lines += 1

half_lines = num_lines / 2

most_common_bits = ''
for zero_occurrences in zero_counter.values():
    most_common_bits += ('0' if zero_occurrences > half_lines else '1')

gamma_rate = int(most_common_bits, 2)
epsilon_rate = pow(2, len(zero_counter)) - 1 - gamma_rate

print(epsilon_rate * gamma_rate)