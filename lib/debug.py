#!/usr/bin/env python3
# lib/debug.py

from models.__init__ import CONN, CURSOR
import ipdb

Exercise.drop_table()
Exercise.create_table()


e1 = Exercise('Pushups', 'lie facing the floor and, keep back straight, raise body by pressing down on hands.')
e2 = Exercise('Planks', 'n isometric core strength exercise that involves maintaining a position similar to a push-up for the maximum possible time.')
e3 = Exercise('Pull Ups', 'Use your body weight to bulk up your back and biceps')
e4 = Exercise('Dips', 'Shred your chest and triceps with your body weight')

ipdb.set_trace()
