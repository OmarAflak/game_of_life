import os
import numpy as np
from time import sleep

def next_step(board):
    neighbors_pos = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    board_ = {(i + h, j + w): 0 for i, j in board for h, w in neighbors_pos}
    board = {**board, **board_}
    get_next_state = lambda s, n: int(n == 3 or n == 2 and s == 1)
    neighbors_count = {(i, j) : sum([1 for p in neighbors_pos if (i + p[0], j + p[1]) in board]) for i, j in board}
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
            c = live_char if (i, j) in board else dead_char
            print(c, end='')
        print('║')
    print('╚' + '═' * width +  '╝')

def clear_console():
    os.system('clear')

def random_board(height, width, initial_population_size):
    h = np.random.randint(low=0, high=height, size=initial_population_size)
    w = np.random.randint(low=0, high=width, size=initial_population_size)
    return {(i, j): 1 for j in w for i in h}

if __name__ == '__main__':
    height, width, init = 50, 50, 10
    board = random_board(height, width, init)
    for i in range(1000):
        clear_console()
        display_board(board, height, width, '+', ' ')
        board = next_step(board)
        sleep(0.05)
