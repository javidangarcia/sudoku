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

def find_empty(board):
    for row in range(len(board)):
        for col in range(len(board[0])):
            if board[row][col] == 0:
                return (row, col)

print_board(board)

