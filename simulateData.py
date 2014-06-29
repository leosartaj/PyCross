#!/usr/bin/env python2

## TicTacToe
# https://github.com/leosartaj/TicTacToe.git
#
# Copyright (c) 2014 Sartaj Singh
# Licensed under the MIT license.
##

import play
import helper

def main():
    try:
        trials = input("Enter number of simulation trials --> ")
    except:
        return
    try:
        NTRIALS = input("Enter number of trials --> ")
    except:
        return
    try:
        dim = input("Size of grid --> ")
    except: 
        return

# simulates the game on a terminal
    while True:
        try:
            play.simulate_data(dim, trials, helper.mc_move, NTRIALS)
        except:
            return
        try:
            game = raw_input("Another simulation ? [Y/N] --> ")
        except:
            return
        if game != 'Y' and game != '':
            return

if __name__ == '__main__':
    main()


