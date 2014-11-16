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

# GUI
import gtk

class customDifficultyClass:
    """
    Loads the custom difficulty dialog box
    """
    def __init__(self, parent):

        self.parent = parent # save the parent caller

        self.load_interface() # load the interface

        self.save_objects() # save objects

        self.builder.connect_signals(self.setup_signals()) # setup signals

        self.center()

        self.window.show_all() # display widgets

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
        fName = self.find_file('customDifficulty.glade')
        self.builder = gtk.Builder()
        self.builder.add_from_file(fName)

    def save_objects(self):
        """
        Get the required objects
        """
        self.window = self.builder.get_object('mainwindow')
        self.entry = self.builder.get_object('entry')

    def setup_signals(self):
        """
        Sets up the signals
        """
        sig = { 'on_mainwindow_destroy': self.close
              , 'on_ok_clicked'       : self.ok
              , 'on_entry_activate'   : self.ok
              , 'on_cancel_clicked'   : self.cancel }

        return sig

    def center(self):
        """
        Centers the window to the
        location of open instance of
        PyCross main window
        """
        self.window.set_transient_for(self.parent.window) # set the main window as parent
        self.window.set_position(gtk.WIN_POS_CENTER_ON_PARENT)

    def ok(self, button):
        """
        Handles when ok is pressed
        """
        entry = self.entry
        buf = entry.get_buffer()
        try:
            trials = int(buf.get_text())
            if trials > 100 or trials < 1: # do not except invalid number
                raise ValueError
            trails  = trials * 10 # for the program
            self.parent.setdiff('custom', trials) # change difficulty
            self.close() # close the window
        except ValueError: # inavlid input
            self.entry.grab_focus() # again focus

    def cancel(self, button):
        currdiff = self.parent.currdiff
        menuitem = self.parent.diffmenu[currdiff] # get the menuitem
        menuitem.set_active(True) # reset to previous difficulty
        self.close()

    def close(self, *args):
        """
        Handles Destroy Event
        """
        self.window.destroy()
