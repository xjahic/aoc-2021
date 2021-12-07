with open("input.txt") as f:
    line = f.readlines()[0]
    initial_positions = [int(fish) for fish in line.rstrip().split(',')]

initial_positions.sort()

fuel_per_position = {i: 0 for i in range(initial_positions[0], initial_positions[-1] + 1)}

for available_position in fuel_per_position.keys():
    if fuel_per_position[available_position] > 0:
        continue

    fuel_total = 0
    for position in initial_positions:
        diff = abs(available_position - position)
        fuel_total += (diff * (diff + 1)) / 2

    fuel_per_position[available_position] = fuel_total


print(min(fuel_per_position.values()))

