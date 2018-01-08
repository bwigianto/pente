import copy
#board = [19 * [0] for i in xrange(19)]

def five(board, seed=None):
    for i in xrange(len(board)):
        for j in xrange(len(board[1])):
            if board[i][j] == 1:

    #if seed:



def removals(board, stone, pos, diff):
    one = sum(pos, diff) 
    two = sum(one, diff)
    three = sum(two, diff)
    if not is_valid(board, three):
        return []
    if stone_at(board, one) == opponent(stone) and stone_at(board, two) == opponent(stone) and stone_at(board, three) == stone:
        return [one, two]
    return []

def add_stone(board, stone, pos):
    out = copy.deepcopy(board)
    out[pos[0]][pos[1]] = stone
    to_remove = removals(board, stone, pos, (-1, 0)) + \
        removals(board, stone, pos, (1, 0)) + \
        removals(board, stone, pos, (0, -1)) + \
        removals(board, stone, pos, (0, 1)) + \
        removals(board, stone, pos, (1, 1)) + \
        removals(board, stone, pos, (1, -1)) + \
        removals(board, stone, pos, (-1, 1)) + \
        removals(board, stone, pos, (-1, -1))
    for p in to_remove:
        out[p[0]][p[1]] = 0
    return out

def stone_at(board, pos):
    return board[pos[0]][pos[1]]

def opponent(stone):
    if stone == 1:
        return 2
    return 1

def sum(pos, dpos):
    return (pos[0] + dpos[0], pos[1] + dpos[1])

def is_valid(board, pos):
    return pos[0] >= 0 and pos[0] < len(board) and pos[1] >= 0 and pos[1] < len(board[0])

def valid_move(board, pos):
    return is_valid(board, pos) and stone_at(board, pos) == 0
#print board
