##
# PyCross
# https://github.com/leosartaj/PyCross.git
#
# Copyright (c) 2014 Sartaj Singh
# Licensed under the MIT license.
##

"""
Helper functions for tic tac toe
"""

import random

# Useful constants
from TTTBoard import EMPTY
from TTTBoard import X
from TTTBoard import O

MCMATCH = 1.0  # Score for squares played by the machine player
MCOTHER = 1.0  # Score for squares played by the other player

# SCORING VALUES - DO NOT MODIFY
# Used for minimax implementation
SCORES = {X: 1, EMPTY: 0, O: -1}

def switch_player(player):
    """
    toggle active player
    """
    if player == X:
        return O
    else:
        return X

def mc_trial(board, player):
    """
    fills the board
    until the game 
    is finished
    """
    empty = board.get_empty_squares()
    leng = len(empty)
    while True:
        box = random.randrange(leng)
        row = empty[box][0]
        col = empty[box][1]
        board.move(player, row, col)
        result = board.check_win()
        if result != None:
            return 
        del empty[box]
        leng -= 1
        player = switch_player(player)

def mc_update_scores(scores, board, player):
    """
    updates the scores
    after a game is finished
    """
    result = board.check_win()
    other = switch_player(player)
    if result != player and result != other:
        return
    dim = board.get_dim()
    other = switch_player(result)
    for cou1 in range(dim):
        for cou2 in range(dim):
            status = board.square(cou1, cou2)
            if status == result:
                if result == player:
                    scores[cou1][cou2] += MCMATCH
                else:
                    scores[cou1][cou2] += MCOTHER
            elif status == other:
                if result == player:
                    scores[cou1][cou2] -= MCMATCH
                else:
                    scores[cou1][cou2] -= MCOTHER

def stop_win(board, player):
    """
    Stops a straight forward win 
    Tries to win when straight forward
    everything cannot be left on probability
    """
    empty = board.get_empty_squares()
    other = switch_player(player)
    for box in empty:
        if trymove(board, player, box) == player:
            return box
        if trymove(board, other, box) == other:
            return box
    return None

def trymove(board, player, move):
    """
    Try a move
    returns the result
    """
    copy = board.clone()
    copy.move(player, move[0], move[1])
    return copy.check_win()

def get_best_move(board, scores):
    """
    returns the best
    possible move from the available
    moves
    """
    best = []
    empty = board.get_empty_squares()
    maxi = float('-inf')
    for squ in empty:
        score = scores[squ[0]][squ[1]]
        if score > maxi:
            best = []
            best.append(squ)
            maxi = score
        elif score == maxi:
            best.append(squ)
    index = random.randrange(len(best))
    return best[index]

def mc_move(board, player, trials):
    """
    returns the best possible move
    after collecting data over N trials
    """
    stop = stop_win(board, player) # try to stop a straight forward win
    if stop != None:
        return stop
    dim = board.get_dim()
    scores = [ [0 for dummy_cou in range(dim)] for dummy_cou2 in range(dim)] 
    for dummy_cou in range(trials):
        copy_board = board.clone()
        mc_trial(copy_board, player)
        mc_update_scores(scores, copy_board, player)
    return get_best_move(board, scores)

def mm_move(board, player):
    """
    Make a move on the board.
    
    Returns a tuple with two elements.  The first element is the score
    of the given board and the second element is the desired move as a
    tuple, (row, col).
    """
    result = board.check_win()
    if result == X:
        return SCORES[X], (-1, -1) 
    elif result == O:
        return SCORES[O], (-1, -1) 
    elif result == EMPTY:
        return SCORES[EMPTY], (-1, -1) 
    scores, poss = [], []
    for square in board.get_empty_squares():
        copy = board.clone()
        copy.move(player, square[0], square[1])
        score = mm_move(copy, switch_player(player))
        scores.append(score[0])
        poss.append(square)
    if player == X:
        mscore = max(scores)
    else:
        mscore = min(scores)
    bpos = poss[scores.index(mscore)]
    return mscore, bpos

def minimax_move(board, player, trials):
    """
    Wrapper to allow the use of the same infrastructure that was used
    for Monte Carlo Tic-Tac-Toe.
    """
    move = mm_move(board, player)
    assert move[1] != (-1, -1), "returned illegal move (-1, -1)"
    return move[1]
