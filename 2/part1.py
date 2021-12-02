horizontal = 0
depth = 0

with open("input.txt") as f:
    for line in f:
        [instruction, value] = line.rstrip().split(' ')
        value = int(value)

        if 'forward' == instruction:
            horizontal += value
        elif 'up' == instruction:
            depth -= value
        else:
            depth += value

print(horizontal * depth)
