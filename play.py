##
# TicTacToe
# https://github.com/leosartaj/TicTacToe.git
#
# Copyright (c) 2014 Sartaj Singh
# Licensed under the MIT license.
##

import TTTBoard
from helper import switch_player

# Useful constants
EMPTY = TTTBoard.EMPTY
X = TTTBoard.X
O = TTTBoard.O

def play_terminal(dim, mc_move, trials):
    """
    Makes the game playable on a terminal
    """
    board = TTTBoard.TTTBoard(dim)
    while True:
        try:
            other = raw_input("You are O or X [O/X] --> ")
        except:
            return
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
            try:
                rowcol = raw_input("[row] [col] --> ")
                rowcol = rowcol.split(' ')
                if len(rowcol) != 2:
                    continue
                orow = int(rowcol[0])
                ocol = int(rowcol[1])
            except KeyboardInterrupt:
                return
            if orow > -1 and orow < dim and ocol > -1 and ocol < dim and board.square(orow, ocol) == EMPTY:
                break
            print ''
        board.move(other, orow, ocol)

def format_result(board, player): # prints the result and returns True if the game is over otherwise returns False
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

def simulate_data(dim, data_trials, mc_move, trials):
    """
    simulates the game on a terminal
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
    xwin = '(' + str((float(count[X]) / data_trials) * 100) + ')'
    owin = '(' + str((float(count[O]) / data_trials) * 100) + ')'
    draw = '(' + str((float(count[EMPTY]) / data_trials) * 100) + ')'
    print 'Total games =', data_trials
    print 'X wins = ', count[X], xwin
    print 'O wins = ', count[O], owin
    print 'Draws = ', count[EMPTY], draw

def data_result(board, count):
    result = board.check_win()
    if result != None:
        count[result] += 1
        return True
    return False
