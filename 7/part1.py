
with open("input.txt") as f:
    line = f.readlines()[0]
    initial_positions = [int(fish) for fish in line.rstrip().split(',')]

initial_positions.sort()
median = initial_positions[int(len(initial_positions) / 2)]

fuel = 0
for pos in initial_positions:
    fuel += abs(median - pos)

print(fuel)
