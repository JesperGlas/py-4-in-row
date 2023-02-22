from genericpath import exists
import os
from random import randint
from re import L
import sys
from turtle import circle
from typing import List, Tuple
import pygame as pg

STEP: int = 100
MARGIN: int = 10
GRID_SIZE: int = STEP - MARGIN*2
MARK_SIZE: int = GRID_SIZE - MARGIN*2
RESOLUTION: Tuple[int, int] = (700, 700)

MAX_COLS: int = 7
MAX_ROWS: int = 6

WHITE: Tuple[float, float, float] = (255, 255, 255)
BLACK: Tuple[float, float, float] = (0, 0, 0)
GREEN: Tuple[float, float, float] = (0, 255, 0)
RED: Tuple[float, float, float] = (255, 0, 0)

HUMAN: int = 0
AI: int = 1

def main():
    print("Hello")
    
    # init variables
    window: pg.Surface = init()
    board: List[List[int]] = [[] for col in range(7)]

    checkFour(board)
    
    players: Tuple[Tuple(str, int), Tuple[str, int]] = (
        ("Jesper", HUMAN),
        ("AI4Row", HUMAN)
    )

    # main loop
    while True:
        render(window, board)
        if players[activePlayer(board)][1] == HUMAN:
            checkInput(board)
        else:
            aiTurn(board)
            
        if checkEnd(board):
            pg.quit()
            sys.exit()
                
def init() -> pg.Surface:
    pg.init()
    window = pg.display.set_mode(RESOLUTION)
    pg.display.set_caption("4-In-a-Row")
    
    return window
        
def checkInput(board: List[List[int]]) -> None:
    for e in pg.event.get():
        if e.type == pg.QUIT:
            pg.quit()
            sys.exit()
        if e.type == pg.MOUSEBUTTONUP:
            mouse_x: int = pg.mouse.get_pos()[0]
            col: int = mouse_x//STEP
            if validMove(col, board):
                board[col].append(activePlayer(board))
            
        
def render(window: pg.Surface, board: List[List[int]]) -> None:
    window.fill(BLACK)
    renderBoard(window)
    renderMarks(window, board)
    renderMove(window, board)
            
    pg.display.flip()

def renderBoard(window: pg.Surface) -> None:
    for columns in range(7):
        left: int = STEP*columns + MARGIN
        for rows in range(6):
            top: int = STEP + STEP*rows + MARGIN
            rect: pg.Rect = pg.Rect(left, top, GRID_SIZE, GRID_SIZE)
            MARK_SIZE: int = GRID_SIZE - MARGIN*2
            MARK_SIZE: int = GRID_SIZE - MARGIN*2
            pg.draw.rect(window, WHITE, rect)
            
def renderMarks(window: pg.Surface, board: List[List[int]]) -> None:
    for i, col in enumerate(board):
        center_x: int = i * STEP + STEP/2
        for j, grid in enumerate(col):
            center_y: int = (RESOLUTION[1]-STEP - STEP*j) + STEP/2
            color: Tuple[int, int, int] = GREEN if grid == 0 else RED
            pg.draw.circle(window, color, (center_x, center_y), MARK_SIZE/2)

def renderMove(window: pg.Surface, board: List[List[int]]) -> None:
    mouse_x: int = pg.mouse.get_pos()[0]
    active_player = activePlayer(board)
    col: int = mouse_x//STEP
    if validMove(col, board):
        center_x: int = col * STEP + STEP/2
        center_y: int = STEP/2
        color: Tuple[int, int, int] = GREEN if active_player == 0 else RED
        pg.draw.circle(window, color, (center_x, center_y), MARK_SIZE/2)
        
def validMove(col: int, board: List[List[int]]) -> bool:
    return len(board[col]) < MAX_ROWS

def aiTurn(board: List[List[int]]) -> None:
    valid = False
    while not valid:
        col: int = randint(0, 6)
        valid = validMove(col, board)
    board[col].append(activePlayer(board))

def activePlayer(board: List[List[int]]) -> int:
    turns: int = sum(len(col) for col in board)
    return turns % 2

def checkEnd(board: List[List[int]]) -> bool:
    if checkVictory(board):
        return True
    if sum(len(col) for col in board) >= 42:
        print("It's a draw!")
        return True
    return False

def checkVictory(board: List[List[int]]) -> bool:
    # col check
    state: Tuple[int, int] = (-1, -1)
    state = checkCol(board)
    if state[0] >= 4:
        print(f'Player {state[1]} won!')
        return True
        
    state = checkRow(board)
    if state[0] >= 4:
        print(f'Player {state[1]} won!')
        return True
        
    #row check

def checkCol(board: List[List[int]]) -> Tuple[int, int]:
    player: int = -1
    count: int = 1
    for col in board:
        for mark in col:
            if mark == player:
                count += 1
            else:
                player = mark
                count = 1
        if count >= 4:
            break
        
    return (count, player)

# NOT WORKING!
def checkRow(board: List[List[int]]) -> Tuple[int, int]:
    player: int = -1
    count: int = 1
    for i in range(MAX_ROWS):
        for j, col in enumerate(board):
            if i < len(col):
                if col[i] == player:
                    count += 1
                else:
                    player = col[i]
                    count = 1
            else:
                player = -1
                count = 1
        
    return (count, player)

def checkFour(board: List[List[int]]) -> Tuple[int, int]:
    checked: List[List[int]] = [[0]*6]*7
    print(board)
    print(checked)
    for i, col in enumerate(board):
        for j, grid in enumerate(col):
            pass
    
if __name__ == '__main__':
    main()