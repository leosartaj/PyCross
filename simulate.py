#!/usr/bin/env python2

## TicTacToe
# https://github.com/leosartaj/TicTacToe.git
#
# Copyright (c) 2014 Sartaj Singh
# Licensed under the MIT license.
##

import play
import helper

try:
    NTRIALS = input("Enter number of trials --> ")
except:
    exit()

# simulates the game on a terminal
play.simulate_terminal(3, play.X, helper.mc_move, NTRIALS)

