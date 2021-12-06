
with open("input.txt") as f:
    line = f.readlines()[0]
    initial_fish = [int(fish) for fish in line.rstrip().split(',')]

for i in range(80):
    updated_fish = []
    new_fish_count = 0
    for fish in initial_fish:
        if fish == 0:
            updated_fish.append(6)
            new_fish_count += 1
        else:
            updated_fish.append(fish - 1)

    if new_fish_count > 0:
        updated_fish.extend([8] * new_fish_count)
    initial_fish = updated_fish

    # print("iteration", i, ': ', initial_fish)

print(len(initial_fish))
