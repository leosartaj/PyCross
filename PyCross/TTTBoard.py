##
# PyCross
# https://github.com/leosartaj/PyCross.git
#
# Copyright (c) 2014 Sartaj Singh
# Licensed under the MIT license.
##

"""
Contains main board class
"""

import copy

EMPTY = '_'
X = 'X'
O = 'O'

class TTTBoard:
    """
    Initializes a TicTacToe board
    Provides various helper functions
    """
    def __init__(self, dim = 3, board = None):
        self.dim = dim
        if board == None:
            board = [ [EMPTY for dummy_cou in range(dim)] for dummy_cou2 in range(dim)]
        self.board = board

    def __str__(self):
        board = '\n'
        for dummy_row in range(self.dim):
            for dummy_col in range(self.dim):
                board += str(self.board[dummy_row][dummy_col]) + ' '
            board += '\n'
        return board

    def get_dim(self):
        return self.dim

    def square(self, row, col):
        return self.board[row][col]

    def get_empty_squares(self): # returns a list of form (row, col) of empty squares
        empty = []
        for dummy_row in range(self.dim):
            for dummy_col in range(self.dim):
                if self.board[dummy_row][dummy_col] == EMPTY:
                    empty.append((dummy_row, dummy_col))
        return empty

    def move(self, player, row, col):
        if self.board[row][col] == EMPTY:
            self.board[row][col] = player

    def check_win(self): # gives the result [None|X|O|EMPTY]
        leng = self.get_empty_squares()
        player = self._check_col()
        if player != None:
            return player
        player = self._check_row()
        if player != None:
            return player
        player = self._check_dia()
        if player != None:
            return player
        if len(leng) == 0:
            return EMPTY
        return None

    def _check_col(self):
        for dummy_col in range(self.dim):
            player = self.square(0, dummy_col)
            if player == EMPTY:
                continue
            win = 1
            for dummy_row in range(1, self.dim):
                if self.square(dummy_row, dummy_col) != player:
                    win = 0
                    break
            if win == 1:
                return player
        return None

    def _check_row(self):
        for dummy_row in range(self.dim):
            player = self.square(dummy_row, 0)
            if player == EMPTY:
                continue
            win = 1
            for dummy_col in range(1, self.dim):
                if self.square(dummy_row, dummy_col) != player:
                    win = 0
                    break
            if win == 1:
                return player
        return None

    def _check_dia(self):
        player = self.square(0, 0)
        if player != EMPTY:
            row, col, win = 1, 1, 1
            while col < self.dim:
                if self.square(row, col) != player:
                    win = 0
                    break
                row += 1
                col += 1
            if win == 1:
                return player
        player = self.square(0, self.dim - 1)
        if player != EMPTY:
            row, col, win = 1, self.dim - 2, 1
            while col > -1:
                if self.square(row, col) != player:
                    win = 0
                    break
                row += 1
                col -= 1
            if win == 1:
                return player
        return None

    def clone(self): # clones the board object
        clo = copy.deepcopy(self)
        return clo
