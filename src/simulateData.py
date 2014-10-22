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

def simulate_data(dim, data_trials, mc_move, trials):
    """
    simulates the game data_trials times on the terminal
    """
    player = X
    other = switch_player(player)
    count = {EMPTY: 0, X: 0, O: 0}
    for cou in range(data_trials):
        board = TTTBoard.TTTBoard(dim)
        while True:
            if data_result(board, count):
                break
            move = mc_move(board, player, trials)
            board.move(player, move[0], move[1])
            if data_result(board, count):
                break
            move = mc_move(board, other, trials)
            board.move(other, move[0], move[1])
    return count

def data_result(board, count):
    """
    checks if the game is over
    otherwise updates count
    """
    result = board.check_win()
    if result != None:
        count[result] += 1
        return True
    return False

def stats(count, trials):
    """
    prints the stats on stdOut
    """
    xwin = '(' + str((float(count[X]) / trials) * 100) + ')'
    owin = '(' + str((float(count[O]) / trials) * 100) + ')'
    draw = '(' + str((float(count[EMPTY]) / trials) * 100) + ')'
    print 'Total games =', trials
    print 'X wins = ', count[X], xwin
    print 'O wins = ', count[O], owin
    print 'Draws = ', count[EMPTY], draw

def main():
    try:
        trials = input("Enter number of simulation trials --> ")
        NTRIALS = input("Enter number of trials --> ")
        dim = input("Size of grid --> ")
        while True:
            count = simulate_data(dim, trials, mc_move, NTRIALS) # simulates the game on a terminal
            stats(count, trials)
            game = raw_input("Another simulation ? [Y/N] --> ")
            if game != 'Y' and game != '':
                return
    except KeyboardInterrupt:
        return

if __name__ == '__main__':
    main()
