import copy
#board = [19 * [0] for i in xrange(19)]

def add_stone(board, stone, pos):
    out = copy.deepcopy(board)
    out[pos[0]][pos[1]] = stone
    return out

def is_valid(board, pos):
    return board[pos[0]][pos[1]] == 0

#print board
