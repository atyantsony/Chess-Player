from curses.ascii import isupper
import pyautogui as pg
import numpy as np
from time import sleep
import cv2 as cv
from random import randint

white_turn = True
all_steps = []

white_coordinates = {}
black_coordinates = {}

cell_size = 50

def init():
    global cell_size
    screenshot = pg.screenshot()
    screenshot = cv.cvtColor(np.array(screenshot), cv.COLOR_RGB2BGR)
    white_board = pg.locateOnScreen("graphics/white_board.png")
    init_x = white_board.left + (cell_size/2)+ 1
    init_y = white_board.top + (cell_size/2) + 1
    for alp in range (97, 105):
        init_y = white_board.top + (cell_size/2) + 1
        for num in range(8,0,-1):
            key = chr(alp) + str(num)
            val = (init_x, init_y)
            white_coordinates[key] = val
            init_y += (cell_size + 2)
        init_x += (cell_size + 2)
    
    black_board = pg.locateOnScreen("graphics/black_board2.png")
    init_x = black_board.left + (cell_size/2)
    init_y = black_board.top + (cell_size/2)
    for alp in range (104,96,-1):
        init_y = black_board.top + (cell_size/2)
        for num in range(1,9):
            key = chr(alp) + str(num)
            val = (init_x, init_y)
            black_coordinates[key] = val
            init_y += cell_size
        init_x += cell_size

def mov(initial, destination):
    pg.click(button='left', x=initial[0], y=initial[1])
    # sleep(7+randint(0,7))
    pg.click(button='left', x=destination[0], y=destination[1])


def recognize(piece, dest, init_file = None):
    turn = "black_"
    if (white_turn): turn = "white_"
    screenshot = pg.screenshot()
    screenshot = cv.cvtColor(np.array(screenshot), cv.COLOR_RGB2BGR)
    conf = 0.8
    if piece == "pawn" and not(white_turn): conf = 0.95
    color1 = (174,177,135,255)
    color2 = (133,121,79,255)
    color3 = (171,163,58,255)
    color4 = (133,121,79,255)
    for p in pg.locateAllOnScreen("graphics/"+turn+str(piece)+".png", confidence = conf):
        if (init_file != None):
            if white_turn and not (p.left <= white_coordinates[init_file + str(1)][0] <= p.left+p.width):
                # sleep(5+randint(0,5))
                continue
            if (not white_turn) and (not (p.left <= black_coordinates[init_file + str(1)][0] <= p.left+p.width)):
                # sleep(5+randint(0,5))
                continue

        if (piece == "pawn" and init_file == None):
            if not (p.left <= dest[0] <= p.left+p.width):
                # sleep(5+randint(0,5))
                continue

        pg.click(button="left", x=p.left+(p.width/2), y=p.top+(p.height/2))

        pg.moveTo(dest[0], dest[1], duration=3)
        # sleep(10+randint(0,10))
        
        if pg.pixelMatchesColor(dest[0],dest[1],color1,10) or pg.pixelMatchesColor(dest[0],dest[1],color2,10) or pg.pixelMatchesColor(dest[0],dest[1],color3,10) or pg.pixelMatchesColor(dest[0],dest[1],color4,10):
            pg.click()
            return
        if pg.pixelMatchesColor(dest[0]+22,dest[1]-22,color1,10) or pg.pixelMatchesColor(dest[0]+22,dest[1]-22,color2,10) or pg.pixelMatchesColor(dest[0]+22,dest[1]-22,color3,10) or pg.pixelMatchesColor(dest[0]+22,dest[1]-22,color4,10):
            pg.click()
            return


def read_step(step):
    piece = "pawn"
    dest_file = ""
    dest_row = ""

    if (step == "0-0"):
        # short castle
        initial, dest = None, None
        if white_turn:
            initial = white_coordinates["e1"]
            dest = white_coordinates["g1"]
        else:
            initial = black_coordinates["e8"]
            dest = black_coordinates["g8"]
        mov(initial, dest)
        return

    if (step == "0-0-0"):
        # long castle
        initial, dest = None, None
        if white_turn:
            initial = white_coordinates["e1"]
            dest = white_coordinates["c1"]
        else:
            initial = black_coordinates["e8"]
            dest = black_coordinates["c8"]
        mov(initial, dest)
        return

    init_file = None
    first = True
    for chr in step:
        if isupper(chr):
            piece = chr
        if chr >= 'a' and chr <= 'h':
            if first:
                init_file = chr
                first = False
            dest_file = chr
        if chr >= '1' and chr <= '8':
            dest_row = chr

    dest = None
    if white_turn: dest = white_coordinates[dest_file + dest_row]
    else: dest = black_coordinates[dest_file + dest_row]

    if (init_file != None and init_file != dest_file):
        recognize(piece, dest, init_file)
    else:
        recognize(piece, dest)

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
    if (len(steps) != 0): all_steps.append(steps)
    f.close()


take_input()
for i in range(5,0,-1):
    print("Starting in", i)
    sleep(1)

init()

for row in all_steps:
    for step in row:
        read_step(step)
        white_turn = not white_turn
        sign = randint(0,1)
        # if (sign == 0):
        #     sleep(90+randint(0,30))
        # else:
        #     sleep(90-randint(0,30))

screensht = pg.screenshot()
screensht = cv.cvtColor(np.array(screensht), cv.COLOR_RGB2BGR)
resign = pg.locateCenterOnScreen("graphics/resign.png")
if resign != None:
    pg.doubleClick(button="left", x=resign.x, y=resign.y, interval=2)