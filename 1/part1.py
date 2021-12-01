
increases = -1
last_number = 0

with open("input.txt") as f:
    for line in f:
        new_number = int(line.rstrip())
        if new_number > last_number:
            increases += 1
        last_number = new_number

print(increases)
