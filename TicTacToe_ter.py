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
            play.play_terminal(dim, helper.mc_move, NTRIALS) # plays the game on a terminal
            game = raw_input("Another game ? [Y/N] --> ")
            if game != 'Y' and game != '':
                return
    except KeyboardInterrupt: 
        return

if __name__ == '__main__':
    main()
