# -*- coding: utf-8 -*-
"""
Created on Sun Oct 18 19:20:41 2020

@author: S4lt3d
"""

import PIL
import numpy as np
import math
import itertools

def genprimes(limit): # derived from 
                      # Code by David Eppstein, UC Irvine, 28 Feb 2002
    D = {}            # http://code.activestate.com/recipes/117119/
    q = 2

    while q <= limit:
        if q not in D:
            yield q
            D[q * q] = [q]
        else:
            for p in D[q]:
                D.setdefault(p + q, []).append(p)
            del D[q]
        q += 1

# x and y pixels to move around
x = 0
y = 0
# vector to move along
vx = 1
vy = 0

# a list to keep track of our walk
walk = []
# the number of walks to take
limit = 320000
prime_generator = genprimes(1000000000)

current_num = 0
while current_num < limit:
    next_prime = prime_generator.__next__()
    while current_num != next_prime:
        current_num = current_num + 1
        for i in range(1):
            x = x + vx
            y = y - vy
            walk.append([x,y])
    # Rotate moving vector by 90 degrees
    vx = vx * -1
    vy, vx = vx, vy
    
# remove duplicates from list
walk.sort()
walk = list(walk for walk,_ in itertools.groupby(walk))
walk_list = np.array(walk)

# prepare list to become pixels
walk_list -= np.min(walk_list, axis=0)

# make image
width, height = np.max(walk_list, axis=0)
im = PIL.Image.new('RGB', (width+1, height+1), (255, 255, 255))

for x, y in walk_list:
    im.putpixel((x, y), (0,0,0))

im.show()
