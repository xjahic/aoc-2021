with open("input.txt") as f:
    line = f.readlines()[0]
    initial_fish = [int(fish) for fish in line.rstrip().split(',')]

count = 0


def count_fish(days, fish, res):
    fish_reproduction = 0
    days_until_zero = fish + 1

    six_days_fish = days - days_until_zero
    if six_days_fish > 0:
        fish_reproduction += int(six_days_fish // 6)

    eight_days_fish = days - days_until_zero
    if eight_days_fish > 0:
        fish_reproduction += int(eight_days_fish // 8)

    if fish_reproduction > 0:
        return count_fish(six_days_fish - 6, fish, fish_reproduction) + count_fish(eight_days_fish - 8, fish,
                                                                                   fish_reproduction)
    else:
        return res


for fish in initial_fish:
    count += count_fish(80, fish, count)

print(count)
