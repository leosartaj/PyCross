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

# For the GUI
import gtk

class pycrossGUIClass:
    """ 
    Sets up the GUI interface
    """
    def __init__(self):

        self.load_interface() # load the interface

        self.save_objects() # save objects

        self.basic_markup() # setup appearances

        self.builder.connect_signals(self.setup_signals()) # setup signals

        self.window.show_all() # display widgets

    def load_interface(self):
        """
        Loads the interface
        in particular loads the glade file
        """
        fName = os.path.join(os.path.dirname(__file__), 'pycrossGUI.glade') # hack for loading the glade file
        self.builder = gtk.Builder()
        self.builder.add_from_file(fName)

    def setup_signals(self):
        """
        Sets up the signals
        """
        sig = { 'on_clicked': self.trys }

        return sig

    def save_objects(self):
        """
        Get the required objects
        """
        self.window = self.builder.get_object('mainwindow')
        self.board = self.builder.get_object('board')

    def basic_markup(self):
        """
        set the appearances, 'cause appearances are good
        """
        pass

    def trys(self, *args):
        """
        Handles Destroy Event
        """
        print 'Yes'

    def close(self, *args):
        """
        Handles Destroy Event
        """
        gtk.main_quit()
