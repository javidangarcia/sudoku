board = [
    [7, 8, 0, 4, 0, 0, 1, 2, 0],
    [6, 0, 0, 0, 7, 5, 0, 0, 9],
    [0, 0, 0, 6, 0, 1, 0, 7, 8],
    [0, 0, 7, 0, 4, 0, 2, 6, 0],
    [0, 0, 1, 0, 5, 0, 9, 3, 0],
    [9, 0, 4, 0, 6, 0, 0, 0, 5],
    [0, 7, 0, 3, 0, 0, 0, 1, 2],
    [1, 2, 0, 0, 0, 7, 4, 0, 0],
    [0, 4, 9, 2, 0, 6, 0, 0, 7]
]


def solve_sudoku(board):
    slot = next_empty(board)
    if slot == None:
        return True
    else:
         row, col = slot

    for num in range(1, 10):
        if valid_move(board, num, (row, col)):
            board[row][col] = num

            if solve_sudoku(board):
                return True
            
            board[row][col] = 0

    return False


def valid_move(board, num, position):
    for col in range(len(board[0])):
        if board[position[0]][col] == num and position[1] != col:
            return False

    for row in range(len(board)):
        if board[row][position[1]] == num and position[0] != row:
            return False

    block_y = position[0] // 3
    block_x = position[1] // 3

    for row in range(block_y * 3, block_y * 3 + 3):
        for col in range(block_x * 3, block_x * 3 + 3):
            if board[row][col] == num and (row, col) != position:
                return False
    
    return True
    

def print_board(board):
    for row in range(len(board)):
        if row % 3 == 0 and row != 0:
            print("- - - - - - - - - - - - ")

        for col in range(len(board[0])):
            if col % 3 == 0 and col != 0:
                print(" | ", end = "")
            if col == 8:
                print(board[row][col])
            else:
                print(str(board[row][col]) + " ", end = "")


def next_empty(board):
    for row in range(len(board)):
        for col in range(len(board[0])):
            if board[row][col] == 0:
                return (row, col)
    return None


print("=======================")
print("        Original")
print("=======================")
print_board(board)
solve_sudoku(board)
print("\n")
print("=======================")
print("        Solution")
print("=======================")
print_board(board)

