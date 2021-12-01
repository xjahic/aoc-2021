import collections

three_measurement_queue = collections.deque([0, 0, 0])
increases = 0
previous_sum = 0

with open("input.txt") as f:
    for line in f:
        current_number = int(line.rstrip())

        if three_measurement_queue[-1] == 0:
            three_measurement_queue.appendleft(current_number)
            three_measurement_queue.pop()

            if three_measurement_queue[-1] != 0:
                previous_sum = sum(three_measurement_queue)
        else:
            # we have at least one three-measurement

            to_remove = three_measurement_queue.pop()

            new_sum = previous_sum - to_remove + current_number
            if new_sum > previous_sum:
                increases += 1

            three_measurement_queue.appendleft(current_number)
            previous_sum = new_sum

print(increases)
