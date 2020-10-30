# -*- coding: utf-8 -*-

import enum
import sys

class ParseField(enum.IntEnum):
    NAME = 0
    LANDMASS = 1
    ZONE = 2
    AREA = 3
    POPULATION = 4
    LANGUAGE = 5
    RELIGION = 6
    BARS = 7
    STRIPES = 8
    COLOURS = 9
    RED = 10
    GREEN = 11
    BLUE = 12
    GOLD = 13
    WHITE = 14
    BLACK = 15
    ORANGE = 16
    MAIN_HUE = 17
    CIRCLES = 18
    CROSSES = 19
    SALTIRES = 20
    QUARTERS = 21
    SUNSTARS = 22
    CRESCENT = 23
    TRIANGLE = 24
    ICON = 25
    ANIMATE = 26
    TEXT = 27
    TOP_LEFT = 28
    BOTTOM_RIGHT = 29

class Religion(enum.IntEnum):
    CATHOLIC = 0
    OTHER_CHRISTIAN = 1
    MUSLIM = 2
    BUDDHIST = 3
    HINDU = 4
    ETHNIC = 5
    MARXIST = 6
    OTHER = 7

class Colour(enum.IntEnum):
    OTHER = 0
    RED = 1
    GREEN = 2
    BLUE = 3
    GOLD = 4
    WHITE = 5
    BLACK = 6
    ORANGE = 7
    BROWN = 8

class FlagAttributes(object):
    def __init__(self, line = None):
        if line == None:
            self.name = 'undefined'
            self.religion = Religion.OTHER
            self.bars = 0
            self.stripes = 0
            self.colours = 0
            self.red = False
            self.green = False
            self.blue = False
            self.gold = False
            self.white = False
            self.black = False
            self.orange = False
            self.mainhue = Colour.OTHER
            self.circles = 0
            self.crosses = 0
            self.saltires = 0
            self.quarters = 0
            self.sunstars = 0
            self.crescent = False
            self.triange = False
            self.icon = False
            self.animate = False
            self.text = False
            self.topleft = Colour.OTHER
            self.botright = Colour.OTHER
        else:
            attributes = line.strip().split(',')
            self.name = attributes[ParseField.NAME]
            self.religion = Religion(int(attributes[ParseField.RELIGION]))
            self.bars = int(attributes[ParseField.BARS])
            self.stripes = int(attributes[ParseField.STRIPES])
            self.colours = int(attributes[ParseField.COLOURS])
            self.red = bool(int(attributes[ParseField.RED]))
            self.green = bool(int(attributes[ParseField.GREEN]))
            self.blue = bool(int(attributes[ParseField.BLUE]))
            self.gold = bool(int(attributes[ParseField.GOLD]))
            self.white = bool(int(attributes[ParseField.WHITE]))
            self.black = bool(int(attributes[ParseField.BLACK]))
            self.orange = bool(int(attributes[ParseField.ORANGE]))
            self.mainhue = Colour.__dict__.get(attributes[ParseField.MAIN_HUE].upper())#, Colour.OTHER)
            self.circles = int(attributes[ParseField.CIRCLES])
            self.crosses = int(attributes[ParseField.CROSSES])
            self.saltires = int(attributes[ParseField.SALTIRES])
            self.quarters = int(attributes[ParseField.QUARTERS])
            self.sunstars = int(attributes[ParseField.SUNSTARS])
            self.crescent = bool(int(attributes[ParseField.CRESCENT]))
            self.triangle = bool(int(attributes[ParseField.TRIANGLE]))
            self.icon = bool(int(attributes[ParseField.ICON]))
            self.animate = bool(int(attributes[ParseField.ANIMATE]))
            self.text = bool(int(attributes[ParseField.TEXT]))
            self.topleft = Colour.__dict__.get(attributes[ParseField.TOP_LEFT].upper())#, Colour.OTHER)
            self.botright = Colour.__dict__.get(attributes[ParseField.BOTTOM_RIGHT].upper())#, Colour.OTHER)

    def parse(f):
        return [FlagAttributes(line) for line in f]

