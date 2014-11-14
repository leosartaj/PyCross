#!/usr/bin/env python2

##
# PyCross
# https://github.com/leosartaj/PyCross.git
#
# Copyright (c) 2014 Sartaj Singh
# Licensed under the MIT license.
##

"""
Creates SVG for PyCross
Supports creating blank, cross or circle SVG
"""

from math import pi
import optparse 
import cairo

def parse_args():
    """
    Parses the arguments
    """
    usage = """usage: %prog [type] [options]

    Types:
    blank -> for blank SVG
    cross -> for cross SVG
    circle -> for circle SVG

    Run 
    python2 iconCreator.py -h/--help
    For help
"""
    parser = optparse.OptionParser(usage)

    help = "Height of SVG"
    parser.add_option('--height', type='int', help=help, default=130)

    help = "Width of SVG"
    parser.add_option('--width', type='int', help=help, default=130)

    options, args = parser.parse_args()

    if len(args) == 1:
        element = args[0]
    else:
        parser.error('Invalid number of arguments, got ' + str(len(args)) + ' args expecting 1/2')

    if element == 'blank' or element == 'cross' or element == 'circle':
        return options, element
    else:
        parser.error('Invalid argument ' + args[0])


def draw_blank(options, fName='blank.svg'):
    """
    Creates Blank SVG
    """
    height, width = options.height, options.width
    ps  = cairo.SVGSurface(fName, height, width)
    cr = cairo.Context(ps)

    cr.set_source_rgb(255, 255, 255)
    cr.rectangle(0, 0, height, width)
    cr.fill_preserve()

    cr.set_source_rgb(0, 0, 0)
    cr.set_line_width(10)
    cr.stroke_preserve()

def draw_cross(options, fName='cross.svg'):
    """
    Creates Cross SVG
    """
    height, width = options.height, options.width
    ps  = cairo.SVGSurface(fName, options.height, options.width)
    cr = cairo.Context(ps)

    cr.set_source_rgb(255, 255, 255)
    cr.rectangle(0, 0, height, width)
    cr.fill_preserve()

    cr.set_source_rgb(0, 0, 0)
    cr.set_line_width(10)
    cr.move_to(15, 15)
    cr.line_to(height - 15, width - 15)
    cr.move_to(15, width - 15)
    cr.line_to(height - 15, 15)
    
    cr.stroke_preserve()

def draw_circle(options, fName='circle.svg'):
    """
    Creates Circle SVG
    """
    height, width = options.height, options.width
    ps  = cairo.SVGSurface(fName, options.height, options.width)
    cr = cairo.Context(ps)

    # Creates a white filled rectangle
    # with thick black border
    cr.new_path()
    cr.set_source_rgb(255, 255, 255)
    cr.rectangle(0, 0, height, width)
    cr.fill_preserve()
    cr.set_source_rgb(0, 0, 0)
    cr.set_line_width(10)
    cr.stroke_preserve()

    # Creates a black thick
    # circle in the center
    cr.new_path()
    cr.arc(height / 2, width / 2, (height / 2) - 15, 0, 2 * pi)
    cr.stroke_preserve()

if __name__ == '__main__':
    options, element = parse_args() # parse the args

    if element == 'blank':
        draw_blank(options)
    elif element == 'cross':
        draw_cross(options)
    elif element == 'circle':
        draw_circle(options)
