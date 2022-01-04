N = 9 # board dimensions and numbers to be placed (1-9)
EMPTY = 0 # symbol to detnote unfilled entries

backtrack = 0

def sudoku_solver(board):
    global backtrack
    '''
    Use backtracking to solve a Sudoku puzzle
    Input: board, an N by N array of numbers or EMPTY entries
    Return: None, the board is modified in-place

    Assumptions: input Sudoku board is valid (solvable)
    '''
    # note the True/False returns in the function merely helps the recursive calls, they should not be used to dictate the solvability of the puzzle

    # base case
    if find_empty_spot(board) == (None, None):
        return True

    # recursive backtracking
    for value in range(1, N+1):
        i, j = find_empty_spot(board)
        if is_move_valid(board, i, j, value):
            # place onto board
            board[i][j] = value
            # recursive call
            if sudoku_solver(board):
                print_board(board) # found a solution, print it
                #return True

            # remove piece, backtrack
            backtrack += 1
            board[i][j] = EMPTY

    # guessed every value, not solvable
    return False

def is_move_valid(board, i, j, value):
    '''
    Check if value can be placed at board[i][j] for Sudoku to be valid
    Return type: Boolean
    '''

    # check if row has value already
    if value in board[i]:
        return False
    # check if column has value already
    for k in range(N):
        if board[k][j] == value:
            return False
    # check if square section has value already
    for y in range(i//3*3, i//3*3 + 3):
        for x in range(j//3*3, j//3*3 + 3):
            if board[y][x] == value:
                return False

    return True

def get_state(board):
    '''
    Return three arrays deonating the board elements already filled
    '''
    rows = [] # (5, 6) means row 5 already has the number 6
    cols = [] # (5, 6) means col 5 already has the number 6
    squares = [] # (1, 1, 6) means middle-middle square has the number 6

    for i in range(N):
        for j in range(N):
            if board[i][j] != EMPTY:
                rows.append((i, board[i][j]))
                cols.append((j, board[i][j]))
                squares.append((i//3, j//3, board[i][j]))

    # sort all of them
    rows.sort()
    cols.sort()
    squares.sort()

    return rows, cols, squares



def find_empty_spot(board):
    '''
    Find and return indices of an empty spot to place a number
    Return: a tuple (i,j). (None, None) if board is filled
    '''

    for i in range(N):
        for j in range(N):
            if board[i][j] == EMPTY:
                return (i,j)

    return None, None

def print_board(board):
    for i in range(N):
        print(board[i])

    print()

board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]

for i in range(N):
    for j in range(N):
        if board[i][j] != '.':
            board[i][j] = int(board[i][j])
        else:
            board[i][j] = 0


# print_board(board)

sudoku_solver(board)

# print_board(board)
print(backtrack)