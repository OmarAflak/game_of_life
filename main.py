import os
import numpy as np
from time import sleep

def next_board(board):
    neighbors_pos = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    board_ = {(i + h, j + w): 0 for i, j in board for h, w in neighbors_pos if board[(i, j)] == 1 and (i + h, j + w) not in board}
    board = {**board, **board_}
    get_next_state = lambda s, n: int((n in [2, 3] and s == 1) or (n == 3 and s == 0))
    neighbors_count = {(i, j) : sum([board[(i + p[0], j + p[1])] for p in neighbors_pos if (i + p[0], j + p[1]) in board]) for i, j in board}
    next_board = dict()
    for position, state in board.items():
        next_state = get_next_state(state, neighbors_count[position])
        next_board[position] = next_state
    return next_board

def display_board(board, height, width, live_char, dead_char):
    print('╔' + '═' * width +  '╗')
    for i in range(height):
        print('║', end='')
        for j in range(width):
            c = live_char if (i, j) in board and board[(i, j)] == 1 else dead_char
            print(c, end='')
        print('║')
    print('╚' + '═' * width +  '╝')

def clear_console():
    os.system('clear')

def random_board(height, width):
    tmp = np.random.rand(height, width)
    return {(i, j): int(tmp[i][j] > 0.5) for j in range(width) for i in range(height)}

def read_board_from_file(filename):
    file = open(filename, 'r')
    lines = file.readlines()
    lines = [line[:-1] for line in lines]
    board = {}
    for i, line in enumerate(lines):
        for j, c in enumerate(line):
            if c == '1':
                board[(i, j)] = 1
    return board

if __name__ == '__main__':
    height, width = 40, 100
    board = read_board_from_file('structures/glider_gun.txt')
    for i in range(1000):
        clear_console()
        display_board(board, height, width, '+', ' ')
        board = next_board(board)
        sleep(0.05)
