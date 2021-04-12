#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  9 17:44:18 2021

@author: alok
"""

def parts(x):
    if x == 0:
        print('   ',  '------')
        print('   ',  '|    |')
        print('   ',  '|     ')
        print('   ',  '|     ')
        print('   ',  '|     ')
        print('   ',  '|     ')
        print('------------')
    if x == 1:
        print('   ',  '------')
        print('   ',  '|    |')
        print('   ',  '|    O')
        print('   ',  '|     ')
        print('   ',  '|     ')
        print('   ',  '|     ')
        print('------------')
    if x == 2:
        print('   ',  '------')
        print('   ',  '|    |')
        print('   ',  '|    O')
        print('   ',  '|   -|-')
        print('   ',  '|     ')
        print('   ',  '|     ')
        print('------------')
    if x == 3:
        print('   ',  '------')
        print('   ',  '|    |')
        print('   ',  '|    O')
        print('   ',  '|   -|-')
        print('   ',  '|    | ')
        print('   ',  '|     ')
        print('------------')
    if x == 4:
        print('   ',  '------')
        print('   ',  '|    |')
        print('   ',  '|    O')
        print('   ',  '|   -|-')
        print('   ',  '|    | ')
        print('   ',  '|   /  ')
        print('------------')
    if x == 5:
        print('   ',  '------')
        print('   ',  '|    |')
        print('   ',  '|    O')
        print('   ',  '|   -|-')
        print('   ',  '|    | ')
        print('   ',  '|   / \\')
        print('------------')
