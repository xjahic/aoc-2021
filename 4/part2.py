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

winner_board = []
last_bingo_number = -1

for bingo_numbers_count, bingo_number in enumerate(bingo_numbers):
    for board in boards:
        for i in range(0, len(board)):  # board_row
            for j in range(0, len(board)):  # number in board_row
                if board[i][j] == bingo_number:
                    board[i][j] = -1
    # check winners
    did_someone_win = False

    for board in boards:
        is_board_winner = False

        # check rows
        for i in range(len(board)):
            is_row_winner = True
            for j in range(len(board)):
                if board[i][j] != -1:
                    is_row_winner = False
                    break

            if is_row_winner:
                is_board_winner = True
                break

        # check columns
        for i in range(len(board)):
            is_column_winner = True
            for j in range(len(board)):
                if board[j][i] != -1:
                    is_column_winner = False
                    break

            if is_column_winner:
                is_board_winner = True
                break

        # checking completed
        if is_board_winner:
            winner_board = board
            did_someone_win = True
            break

    if did_someone_win:
        last_bingo_number = bingo_number
        break

sum_of_winner_board = [sum(board_row) for board_row in winner_board]
result_sum = sum(sum_of_winner_board) + (25 - bingo_numbers_count) + 1
print(result_sum * last_bingo_number)


