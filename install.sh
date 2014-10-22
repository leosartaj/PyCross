#! /bin/sh

##
# TicTacToe
# https://github.com/leosartaj/TicTacToe.git
#
# Copyright (c) 2014 Sartaj Singh
# Licensed under the MIT license.
##

# The directory where the install.sh script is kept
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
    echo 'Cannot install without root access'
    exit 1
fi

INSTALL_DIR=/usr/local/TicTacToe

if [ ! -d $INSTALL_DIR ]
then
    mkdir $INSTALL_DIR           # Make directory if directory does not exist
fi

# Install files
install -m 0755 "$SCRIPT_DIR/scripts/tictactoe" "/usr/bin/" # Copy the TicTacToe script
install -m 0755 "$SCRIPT_DIR"/src/*.py "$INSTALL_DIR"
