def n_queens(n, board=[]):
    if n == len(board):
        return 1

    count = 0

    for col in range(n):
        board.append(col)

        if is_valid(board):
            count += n_queens(n, board)
        
        board.pop()

    return count

def is_valid(board):
    cur_row, cur_col = len(board)-1, board[-1]

    for row, col in enumerate(board[:-1]):
        col_diff = abs(cur_col - col)
        row_diff = abs(cur_row - row)
        if col_diff == 0 or row_diff == col_diff:
            return False

    return True


for i in range(10):
    print(n_queens(i, board=[]))