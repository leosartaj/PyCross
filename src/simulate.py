#!/usr/bin/env python2

##
# TicTacToe
# https://github.com/leosartaj/TicTacToe.git
#
# Copyright (c) 2014 Sartaj Singh
# Licensed under the MIT license.
##

import TTTBoard
from helper import switch_player, mc_move

# Useful constants
EMPTY = TTTBoard.EMPTY
X = TTTBoard.X
O = TTTBoard.O

def simulate_terminal(dim, mc_move, trials):
    """
    simulates the game on a terminal
    """
    board = TTTBoard.TTTBoard(dim)
    player = X
    other = switch_player(player)
    while True:
        if sim_result(board):
            return
        move = mc_move(board, player, trials)
        board.move(player, move[0], move[1])
        if sim_result(board):
            return
        print board
        move = mc_move(board, other, trials)
        board.move(other, move[0], move[1])
        print board

def sim_result(board):
    result = board.check_win()
    if result != None:
        if result == EMPTY:
            print "\nIts a draw"
        else:
            print "\n", result,  "wins!"
        print board
        return True
    return False

def main():
    try:
        NTRIALS = input("Enter number of trials --> ")
        dim = input("Size of grid --> ")
        while True:
            simulate_terminal(dim, mc_move, NTRIALS) # simulates the game on a terminal
            game = raw_input("Another simulation ? [Y/N] --> ")
            if game != 'Y' and game != '':
                return
    except KeyboardInterrupt:
        return

if __name__ == '__main__':
    main()
