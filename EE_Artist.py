# -*- coding: utf-8 -*-
# Python 2.7

## Everything Eventually - Artist
# Initial Author: R Healy
# Conception Date: 30 October 2013
# 
# Concept: A method to generate pngs of randomized pixel colours. 
# Will create all images imaginable, eventually. :)

import png, numpy

## Functions 
# Function randy - returns a random number
def randy(s):
    return numpy.random.randint(0,s)

## Inputs (Should consider command line options in future)
cs = 256 # the range of colours
ht = 700 # height in pixels
wt = 600 #width in pixels

# Initialize counters
i = 0
dt ='' 

# Set up the tuple required for pypng
while i < wt:
    dt = dt+'i4,i4,i4'    
    if i < wt-1:  
        dt = dt+','
    i = i + 1

# Create empty list of tuples
p = numpy.zeros((ht,),dtype=(dt))

# Populate tuples
j = 0
while j < ht:
    lst = list(p[j]) # convert the tupple to a list (immutability)
    i = 0
    while i < 3 * wt:
        lst[i] = randy(cs) # This could take on any mathematical operator 
        i = i + 1
    p[j] = tuple(lst) # convert list to a tuple
    j = j + 1

#print p # Currently a debugging switch. later this could be used for storage

# Write out image - currtly overwrites.
f = open('random.png', 'wb')
w = png.Writer(width=wt, height=ht)
w.write(f, p)
f.close()