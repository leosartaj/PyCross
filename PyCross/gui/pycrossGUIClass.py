#!/usr/bin/env python2

##
# PyCross
# https://github.com/leosartaj/PyCross.git
#
# Copyright (c) 2014 Sartaj Singh
# Licensed under the MIT license.
##

# system imports
import os
import sys
from random import randrange

# For the GUI
import gtk

try:
    # For debugging purposes
    sys.path.insert(0, '../') # allows importing modules from different directory
    import TTTBoard
    from helper import switch_player, mc_move
except ImportError:
    import PyCross.TTTBoard as TTTBoard
    from PyCross.helper import switch_player, mc_move

# Useful constants
EMPTY = TTTBoard.EMPTY
X = TTTBoard.X
O = TTTBoard.O

class pycrossGUIClass:
    """ 
    Sets up the GUI interface
    """
    def __init__(self):

        self.load_interface() # load the interface

        self.save_objects() # save objects

        self.builder.connect_signals(self.setup_signals()) # setup signals

        self.window.show_all() # display widgets

        self.difflevels = self.gen_diff() # generate diffulty levels

        # Constants
        self.currdiff = '_Easy' # current difficulty level
        self.playerscore = 0
        self.compscore = 0
        self.drawscore = 0
        self.updateScoreBoard()

        self.setup_game()

    def setup_game(self, dim=3):
        """
        Sets up the logical stuff
        """
        self.board = TTTBoard.TTTBoard(dim)
        self.trials = self.difflevels[self.currdiff]
        self.player = X

    def gen_diff(self):
        """
        Generate predifined diffculty levels
        """
        easy = 50
        medium = 200
        hard = 500
        return {'_Easy': easy, '_Medium': medium, '_Hard': hard}

    def find_file(self, fName):
        """
        Hack for loading
        the desired file
        """
        fName = os.path.join(os.path.dirname(__file__), fName)
        return fName

    def load_interface(self):
        """
        Loads the interface
        in particular loads the glade file
        """
        fName = self.find_file('pycrossGUI.glade')
        self.builder = gtk.Builder()
        self.builder.add_from_file(fName)

    def setup_signals(self):
        """
        Sets up the signals
        """
        sig = { 'on_mainwindow_destroy': self.close
              , 'on_clicked'           : self.click
              , 'on_easy_activate'     : self.easy
              , 'on_medium_activate'   : self.medium
              , 'on_hard_activate'     : self.hard }

        return sig

    def easy(self, menuitem):
        """
        Set Easy difficulty
        """
        self.setdiff('_Easy')

    def medium(self, menuitem):
        """
        Set Medium difficulty
        """
        self.setdiff('_Medium')

    def hard(self, menuitem):
        """
        Set Hard difficulty
        """
        self.setdiff('_Hard')

    def setdiff(self, diff):
        """
        Change The difficulty
        """
        if self.currdiff != diff:
            self.currdiff = diff
            self.setup_game()
            self.resetGUI()

    def save_objects(self):
        """
        Get the required objects
        """
        self.window = self.builder.get_object('mainwindow')
        self.scoreboard = self.builder.get_object('textview')
        self.cells = self.load_cells()
        self.diffmenu = self.load_diffmenu()

    def load_diffmenu(self):
        """
        Loads the difficulty menuitems
        """
        easy = self.builder.get_object('easy')
        medium = self.builder.get_object('medium')
        hard = self.builder.get_object('hard')

        return [easy, medium, hard]

    def load_cells(self):
        """
        Loads The cells
        """
        cells = []
        k = 1

        for i in range(3):
            temp = [] # temporary list
            for j in range(3):
                name = "eventbox" + str(k)
                cell = self.builder.get_object(name)
                temp.append(cell)
                k += 1
            cells.append(temp)

        return cells

    def find_index(self, cell, cells):
        """
        Finds out the location of a cell
        """
        for i in range(3):
            for j in range(3):
                if cell == cells[i][j]:
                    return i, j
        return None

    def updateGUI(self, player, i, j):
        """
        Updates the GUI when a move is made
        """
        obj = self.cells[i][j]
        image = obj.get_children()[0]
        if player == X:
            fName = self.find_file('svg/cross.svg')
        elif player == O:
            fName = self.find_file('svg/circle.svg')
        elif player == EMPTY:
            fName = self.find_file('svg/blank.svg')
        image.set_from_file(fName)
        
    def move_comp(self, comp):
        """
        Now Computer makes the deadly move
        """
        trials = randrange(self.trials - 5, self.trials + 5) # make it difficult to predict
        move = mc_move(self.board, comp, trials)
        self.board.move(comp, move[0], move[1])
        return move[0], move[1]
    
    def updateScores(self, winner):
        """
        Update the scores
        """
        if winner == X:
            self.playerscore += 1
        elif winner == O:
            self.compscore += 1
        elif winner == EMPTY:
            self.drawscore += 1

    def updateScoreBoard(self):
        """
        Updates The Score Board
        """
        text = ' Player: ' + str(self.playerscore) + ' Computer: ' + str(self.compscore) + ' Draw: ' + str(self.drawscore)

        scoreboard = self.scoreboard
        buf = scoreboard.get_buffer()
        buf.set_text(text)

    def canPlay(self):
        """
        Checks if another move is possible
        """
        result = self.board.check_win()
        if result == None:
            return True
        return False

    def resetGUI(self):
        """
        Resets The board
        for a new game
        """
        for i in range(3):
            for j in range(3):
                self.updateGUI(EMPTY, i, j)

    def reset(self):
        """
        Resets the game
        """
        self.setup_game()
        self.resetGUI()
        self.updateScoreBoard() # update the score board

    def click(self, widget, event):
        """
        Handles click action
        """
        if not self.canPlay():
            self.updateScores(self.board.check_win())
            self.reset()
            return

        i, j = self.find_index(widget, self.cells) # get the coordinates
        if not (i, j) in self.board.get_empty_squares(): # do not move if already moved
            return
        self.board.move(self.player, i, j) # make the move
        self.updateGUI(self.player, i, j) # updates the GUI with the move

        if not self.canPlay():
            return

        # Computers time
        comp = switch_player(self.player)
        ni, nj = self.move_comp(comp) # get the new move coordinates
        self.updateGUI(comp, ni, nj) 

    def close(self, *args):
        """
        Handles Destroy Event
        """
        gtk.main_quit()
