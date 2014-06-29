#!/usr/bin/env python2

## TicTacToe
# https://github.com/leosartaj/TicTacToe.git
#
# Copyright (c) 2014 Sartaj Singh
# Licensed under the MIT license.
##

import play
import helper

NTRIALS = 1  # Number of trials to run

while True:
    try:
        diff = raw_input("Enter Difficulty level [E|M|H] --> ")
    except:
        exit()
    if diff== 'E':
        break
    elif diff== 'M':
        NTRIALS = 10
        break
    elif diff== 'H':
        NTRIALS = 100
        break

# plays the game on a terminal
play.play_terminal(3, helper.mc_move, NTRIALS)
