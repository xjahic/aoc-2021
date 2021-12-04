bingo_numbers = []
bingo_numbers_set = False

boards = []

with open("input.txt") as f:
    for line in f:
        line = line.rstrip()
        if not bingo_numbers_set:
            numbers = line.split(',')
            bingo_numbers = [int(number) for number in numbers]
            bingo_numbers_set = True
        else:
            if line == '':
                boards.append([])
            else:
                boards[-1].append([int(number) for number in line.split(' ') if number.isdigit()])

winner_boards_indices = []
last_bingo_number = -1

last_winner_board = []


def mark_number_on_board(board, number):
    for i in range(0, len(board)):  # board_row
        for j in range(0, len(board)):  # number in board_row
            if board[i][j] == number:
                board[i][j] = -1


def has_winning_row(board):
    for board_row in board:
        if sum(board_row) == -5:
            return True
    return False


def has_winning_column(board):
    transposed_board = [[board[j][i] for j in range(len(board))] for i in range(len(board[0]))]
    return has_winning_row(transposed_board)


for bingo_number in bingo_numbers:
    for board in boards:
        mark_number_on_board(board, bingo_number)

    last_winner_emerged = False
    # check winners
    for board_inner_index, board in enumerate(boards):
        if board_inner_index in winner_boards_indices:
            continue

        is_board_winner = has_winning_row(board) or has_winning_column(board)

        # checking completed
        if is_board_winner:
            winner_boards_indices.append(board_inner_index)
            if len(boards) == len(winner_boards_indices):
                last_winner_emerged = True

    if last_winner_emerged:
        break

last_winner_board = boards[winner_boards_indices[-1]]
sum_of_winner_board = [sum(board_row) for board_row in last_winner_board]

result_sum = 0
for row in last_winner_board:
    for v in row:
        if v != -1:
            result_sum += v

print(result_sum * bingo_number)