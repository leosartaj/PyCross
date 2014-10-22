#! /bin/sh

##
# TicTacToe
# https://github.com/leosartaj/TicTacToe.git
#
# Copyright (c) 2014 Sartaj Singh
# Licensed under the MIT license.
##

# The directory where the uninstall.sh script is kept
SCRIPT_DIR=$(readlink -f ${0%/*})

# Whether root access is provided
ROOT_ACCESS=1

# UID of the user
USER_UID=$($SCRIPT_DIR/scripts/uid.sh)

# If user = root, the root_access = true
if [ "$USER_UID" = "0" ]
then
    ROOT_ACCESS=0
fi

# If no root access, exit
if [ "$ROOT_ACCESS" != "0" ]
then
    echo 'Cannot uninstall without root access'
    exit 1
fi

# Path to install
path=/usr/local/TicTacToe

if [ -d "$path" ]
then
    rm -rf "$path"
    rm -f /usr/bin/tictactoe
else
    echo 'TicTacToe is not installed yet. Use install.sh to install.'
fi
