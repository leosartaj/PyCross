#!/usr/bin/env python2

##
# PyCross
# https://github.com/leosartaj/PyCross.git
#
# Copyright (c) 2014 Sartaj Singh
# Licensed under the MIT license.
##

"""
Functions for playing game on a terminal
Implements the single player version only
"""

import TTTBoard
from helper import switch_player, mc_move

# Useful constants
EMPTY = TTTBoard.EMPTY
X = TTTBoard.X
O = TTTBoard.O

def play_terminal(dim, trials):
    """
    Makes the game playable on a terminal
    """
    board = TTTBoard.TTTBoard(dim)
    while True:
        other = raw_input("You are O or X [O/X] --> ")
        if other == X or other == O:
            break
        if other == '':
            other = O
            break
    player = switch_player(other)
    while True:
        if format_result(board, player):
            return
        move = mc_move(board, player, trials)
        board.move(player, move[0], move[1])
        if format_result(board, player):
            return
        print board
        while True:
            rowcol = raw_input("[row] [col] --> ")
            rowcol = rowcol.split(' ')
            if len(rowcol) != 2:
                continue
            orow = int(rowcol[0])
            ocol = int(rowcol[1])
            if orow > -1 and orow < dim and ocol > -1 and ocol < dim and board.square(orow, ocol) == EMPTY:
                break
            print ''
        board.move(other, orow, ocol)

def format_result(board, player):
    """
    prints the result and returns True if the game is over otherwise returns False
    """
    result = board.check_win()
    if result != None:
        if result == EMPTY:
            print "\nIts a draw"
        elif result == player:
            print "\nMachine wins!"
        else:
            print "\nYou win!"
        print board
        return True
    return False

def main():
    try:
        while True:
            diff = raw_input("Enter Difficulty level [E|M|H] --> ")
            if diff== 'E':
                NTRIALS = 10  # Number of trials to run
                break
            elif diff== 'M':
                NTRIALS = 25
                break
            elif diff== 'H':
                NTRIALS = 100
                break
        dim = input("Size of grid --> ")
        while True:
            play_terminal(dim, mc_move, NTRIALS) # plays the game on a terminal
            game = raw_input("Another game ? [Y/N] --> ")
            if game != 'Y' and game != '':
                return
    except KeyboardInterrupt: 
        return

if __name__ == '__main__':
    main()
