#!/usr/bin/env python2

##
# TicTacToe
# https://github.com/leosartaj/TicTacToe.git
#
# Copyright (c) 2014 Sartaj Singh
# Licensed under the MIT license.
##

import play
import helper


def main():
    while True:
        try:
            diff = raw_input("Enter Difficulty level [E|M|H] --> ")
        except:
            return
        if diff== 'E':
            NTRIALS = 10  # Number of trials to run
            break
        elif diff== 'M':
            NTRIALS = 25
            break
        elif diff== 'H':
            NTRIALS = 100
            break
    try:
        dim = input("Size of grid --> ")
    except: 
        return

    while True:
        play.play_terminal(dim, helper.mc_move, NTRIALS) # plays the game on a terminal
        try:
            game = raw_input("Another game ? [Y/N] --> ")
        except:
            return
        if game != 'Y' and game != '':
            return

if __name__ == '__main__':
    main()
