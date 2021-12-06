
with open("input.txt") as f:
    line = f.readlines()[0]
    initial_fish = [int(fish) for fish in line.rstrip().split(',')]

data = {
    0: 0,
    1: 0,
    2: 0,
    3: 0,
    4: 0,
    5: 0,
    6: 0,
    7: 0,
    8: 0
}

for fish in initial_fish:
    data[fish] = data.get(fish) + 1


for i in range(80):
    # remember previous first fish count
    numbers_of_fish_to_create = data[0]

    for data_index in range(8):
        # shift to left
        data[data_index] = data[data_index + 1]

    data[6] = data.get(6) + numbers_of_fish_to_create
    data[8] = numbers_of_fish_to_create


print(sum(data.values()))
