horizontal = 0
depth = 0
aim = 0

with open("input.txt") as f:
    for line in f:
        [instruction, value] = line.rstrip().split(' ')
        value = int(value)

        if 'forward' == instruction:
            horizontal += value
            depth += aim * value
        elif 'up' == instruction:
            aim -= value
        else:
            aim += value

print(horizontal * depth)
