#!/usr/bin/env python2

##
# PyCross
# https://github.com/leosartaj/PyCross.git
#
# Copyright (c) 2014 Sartaj Singh
# Licensed under the MIT license.
##

from PyCross import __version__

try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup, find_packages

setup(
    name = 'PyCross',
    version = __version__,
    author = 'Sartaj Singh',
    author_email = 'singhsartaj94@gmail.com',
    description = ('Singleplayer/Multiplayer Tic-Tac-Toe game'),
    long_description = open('README.rst').read() + '\n\n' + open('CHANGELOG.rst').read(),
    license = 'MIT',
    keywords = 'game tic-tac-toe tictactoe play',
    url = 'http://github.com/leosartaj/PyCross',
    packages=find_packages(),
    package_data={'PyCross.gui.svg': ['*.svg'], 'PyCross.gui': ['*.glade']},
    scripts=['bin/pycross'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Environment :: X11 Applications :: GTK',
        'Environment :: Console',
        'Natural Language :: English',
        'Programming Language :: Python :: 2.7',
        'Topic :: Games/Entertainment :: Board Games',
    ],
)
