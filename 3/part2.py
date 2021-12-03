zero_counter = {}
num_lines = 0

input_lines = []

with open("input.txt") as f:
    for line in f:
        line = line.rstrip()
        input_lines.append(line)
        for i in range(0, len(line)):
            zero_counter[i] = zero_counter.get(i, 0) + (1 if int(line[i]) == 0 else 0)
        num_lines += 1

half_lines = num_lines / 2

most_common_bits = ''
for zero_occurrences in zero_counter.values():
    most_common_bits += ('0' if zero_occurrences > half_lines else '1')

first_most_common_bit = most_common_bits[0]
lines_for_oxygen_rating = []
lines_for_scrubber_rating = []
for input_line in input_lines:
    if input_line[0] == first_most_common_bit:
        lines_for_oxygen_rating.append(input_line)
    else:
        lines_for_scrubber_rating.append(input_line)


def oxygen_rating(lines):
    for i in range(1, len(lines[0])):
        most_common = {}
        for line in lines:
            bit = line[i]
            most_common[bit] = most_common.get(bit, 0) + 1

        most_common_in_iteration = '1'  # defaulted to 1
        if most_common.get('0', 0) > most_common.get('1', 0):
            most_common_in_iteration = '0'

        updated_lines_for_oxygen_rating = []
        for line_in_oxygen_rating in lines:
            if line_in_oxygen_rating[i] == most_common_in_iteration:
                updated_lines_for_oxygen_rating.append(line_in_oxygen_rating)

        lines = updated_lines_for_oxygen_rating
        if len(lines) == 1:
            break

    oxygen_generator_rating = int(lines[0], 2)
    return oxygen_generator_rating


def scrubber_rating(lines):
    for i in range(1, len(lines[0])):
        most_common = {}
        for line in lines:
            bit = line[i]
            most_common[bit] = most_common.get(bit, 0) + 1

        least_common_in_iteration = '0'  # defaulted to 0
        if most_common.get('0', 0) > most_common.get('1', 0):
            least_common_in_iteration = '1'

        updated_lines_for_scrubber_rating = []
        for line_in_scrubber_rating in lines:
            if line_in_scrubber_rating[i] == least_common_in_iteration:
                updated_lines_for_scrubber_rating.append(line_in_scrubber_rating)

        lines = updated_lines_for_scrubber_rating
        if len(lines) == 1:
            break

    scrubber_generator_rating = int(lines[0], 2)
    return scrubber_generator_rating


print(oxygen_rating(lines_for_oxygen_rating) * scrubber_rating(lines_for_scrubber_rating))
