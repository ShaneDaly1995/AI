#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  2 09:34:48 2018

@author: shanedaly
"""
import numpy as np
import time
"""
False - Dirty Area
True - Clean Area
"""
active_area= [[0, False], [1, True], [2, False], [3, False]]
performance = 1000

"""
Optimisation Score
-100: Movement
500: Clean
"""

def main():
    
    for x in range(len(active_area)):
        check_area(x, active_area)
        
    confirm(active_area)
    
def check_area(location, active_area):
    global performance
    current_square = active_area[location]
    
    if current_square[1] == False:
        print("----------- Movement -----------")
        print("{} - Dirty: Send to Clean.\n".format(current_square))
        print("{} - Current Performance Measure".format(performance))
        clean(current_square[0], active_area)
    performance = np.subtract(performance, 100) 
    return performance
    
def clean(index, active_area):
    global performance
    print("----------- Cleaner -----------")
    print("{} - Vaccuming...\n".format(active_area[index]))
    current_node = active_area[index]
    current_node[1] = True
    time.sleep(2)
    print("{} - Success!\n".format(active_area[index]))
    performance = np.add(performance, 500) 
    print("{} - Current Performance Measure".format(performance))
        
def confirm(active_area):
    outcome = False
    print("-------------------------------") 
    print("\n",active_area)
    
    for x in range(len(active_area)):
        node = active_area[x]
        
        if node[1] != True:
            outcome = False
        else:
            outcome = True
    
    if outcome != True:
            print("Cleaning Failed..")
    else:
            print("\nVaccum Entering Sleep.")
      
main()