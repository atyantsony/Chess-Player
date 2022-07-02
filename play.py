from curses.ascii import isupper
from tkinter.tix import CELL
from cv2 import destroyAllWindows
import pyautogui as pg
import numpy as np
from time import sleep
import cv2 as cv

white_turn = True
all_steps = []

white_coordinates = {}
black_coordinates = {}

CELL_SIZE = 50

def init():
    screenshot = pg.screenshot()
    screenshot = cv.cvtColor(np.array(screenshot), cv.COLOR_RGB2BGR)
    white_board = pg.locateOnScreen("graphics/white_board.png", confidence = 0.9)
    init_x = white_board.left + (CELL_SIZE/2)
    init_y = white_board.top + (CELL_SIZE/2)
    for alp in range (97, 105):
        init_y = white_board.top + (CELL_SIZE/2)
        for num in range(8,0,-1):
            key = chr(alp) + str(num)
            val = (init_x, init_y)
            white_coordinates[key] = val
            init_y += CELL_SIZE/2
        init_x += CELL_SIZE/2
    
    black_board = pg.locateOnScreen("graphics/black_board.png", confidence=0.9)
    init_x = black_board.left + (CELL_SIZE/2)
    init_y = black_board.top + (CELL_SIZE/2)
    for alp in range (104, 96, -1):
        init_y = black_board.top + (CELL_SIZE/2)
        for num in range(1,9):
            key = chr(alp) + str(num)
            val = (init_x, init_y)
            black_coordinates[key] = val
            init_y += CELL_SIZE/2
        init_x += CELL_SIZE/2

def mov():
    None
def locate(dest_file, dest_row):
    None
def recognize(peice):
    if peice == "pawn":
        None
    turn = "black_"
    if (white_turn): turn = "white_"
    screenshot = pg.screenshot()
    screenshot = cv.cvtColor(np.array(screenshot), cv.COLOR_RGB2BGR)


def read_step(step):
    peice = "pawn"
    dest_file = ""
    dest_row = ""

    if (step == "0-0"):
        # short castle
        None
    if (step == "0-0-0"):
        # long castle
        None
    for chr in step:
        if isupper(chr):
            peice = chr
        if chr >= 'a' and chr <= 'h':
            dest_file = chr
        if chr >= '1' and chr <= '8':
            dest_row = chr
    dest = []
    if white_turn: dest = white_coordinates(dest_file + dest_row)
    else: dest = black_coordinates(dest_file + dest_row)

    if peice == "pawn":
        None
    else:
        None

def take_input():
    f = open("input.txt", "r")
    str = f.read()
    global all_steps
    word = ""
    steps = []
    for c in str:
        if (c == ' '):
            if '.' in word:
                word = ""
                continue
            steps.append(word)
            word = ""
            if (len(steps) == 2):
                all_steps.append(steps)
                steps = []
        else:
            word = word + c
    f.close()

    # printing the input for debug 
    '''
    for st in all_steps:
        for st2 in st:
            print(st2, "\t", end=' ')
        print('\n')
    '''

take_input()

for i in range(5,0,-1):
    print("Starting in", i)
    sleep(1)

init()

for row in all_steps:
    for step in row:
        read_step(step)
        mov()
        white_turn = not white_turn