diagram = {}
# {x: {y: count} }
#

with open("input.txt") as f:
    for line in f:
        line = line.rstrip()
        left, right = line.split(' -> ')
        x1, y1 = left.split(',')
        x2, y2 = right.split(',')

        x1, x2, y1, y2 = int(x1), int(x2), int(y1), int(y2)

        # vertical lines
        if x1 == x2:
            if x1 not in diagram:
                diagram[x1] = {}

            if y1 > y2:
                for i in range(y2, y1 + 1):
                    diagram[x1][i] = diagram[x1].get(i, 0) + 1
            else:
                for i in range(y1, y2 + 1):
                    diagram[x1][i] = diagram[x1].get(i, 0) + 1

        # horizontal lines
        elif y1 == y2:
            if x1 > x2:
                for i in range(x2, x1 + 1):
                    if i not in diagram:
                        diagram[i] = {}
                    diagram[i][y1] = diagram[i].get(y1, 0) + 1
            else:
                for i in range(x1, x2 + 1):
                    if i not in diagram:
                        diagram[i] = {}
                    diagram[i][y1] = diagram[i].get(y1, 0) + 1


count = 0

for rows in diagram.values():
    for value in rows.values():
        if value >= 2:
            count += 1

print(count)


# print(diagram)
# for i in range(0, 10):
#     for j in range(0, 10):
#         if i in diagram[j]:
#             print(diagram[j][i], end="")
#         else:
#             print('.', end="")
#     print()