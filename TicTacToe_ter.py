#!/usr/bin/env python2

## TicTacToe
# https://github.com/leosartaj/TicTacToe.git
#
# Copyright (c) 2014 Sartaj Singh
# Licensed under the MIT license.
##

import play
import helper

NTRIALS = 10  # Number of trials to run

def main():
    while True:
        try:
            diff = raw_input("Enter Difficulty level [E|M|H] --> ")
        except:
            return
        if diff== 'E':
            break
        elif diff== 'M':
            NTRIALS = 50
            break
        elif diff== 'H':
            NTRIALS = 100
            break
    try:
        dim = input("Size of grid --> ")
    except: 
        return

# plays the game on a terminal
    while True:
        try:
            play.play_terminal(dim, helper.mc_move, NTRIALS)
        except:
            return
        try:
            game = raw_input("Another game ? [Y/N] --> ")
        except:
            return
        if game != 'Y' and game != '':
            return

if __name__ == '__main__':
    main()
