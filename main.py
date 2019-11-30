import os
import numpy as np
from time import sleep

def count_neighbors(grid, i, j):
    counter = 0
    neighbors = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    for a, b in neighbors:
        if 0 <= i + a < len(grid) and 0 <= j + b < len(grid[0]):
            counter += grid[i + a][j + b]
    return counter

def next_step(grid):
    height = len(grid)
    width = len(grid[0])
    get_next_state = lambda s, n: int(n == 3 or n == 2 and s == 1)
    neighbors = [[count_neighbors(grid, i, j) for j in range(width)] for i in range(height)]
    return [[get_next_state(grid[i][j], neighbors[i][j]) for j in range(width)] for i in range(height)]

def display_grid(grid, live_char, dead_char):
    height, width = len(grid), len(grid[0])
    print('╔' + '═' * width +  '╗')
    for i in range(height):
        print('║', end='')
        for j in range(width):
            c = live_char if grid[i][j] == 1 else dead_char
            print(c, end='')
        print('║')
    print('╚' + '═' * width +  '╝')

def clear_console():
    os.system('clear')

def read_board_from_file(filename, height=None, width=None):
    file = open(filename, 'r')
    lines = file.readlines()
    lines = [line[:-1] for line in lines]
    if not height:
        height = len(lines)
    if not width:
        width = len(lines[0])
    board = [[0] * width for i in range(height)]
    for i, line in enumerate(lines):
        for j, c in enumerate(line):
            if c == '1':
                board[i][j] = 1
    return board

def random_board(height, width):
    tmp = np.random.rand(height, width)
    return [[int(tmp[i][j] > 0.5) for j in range(width)] for i in range(height)]

if __name__ == '__main__':
    board = read_board_from_file('glider_gun.txt')
    #board = random_board(50, 150)
    for i in range(1000):
        clear_console()
        display_grid(board, '+', ' ')
        board = next_step(board)
        sleep(0.05)
