## Markers
# You can use the keyword argument marker to emphasize each point with a specified marker

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Mark each point with a circle:

def task1(x,y):
    
    plt.plot(x,y,marker="o")
    plt.show()
    
x=np.array([1,2,3,4,5])
y=np.array([5,2,7,3,9])

task1(x,y)

#Mark each point with a star:

def task2(a,b):
    
    plt.plot(a,b,marker="*")
    plt.show()
    
a=np.array([6,8,3,5])
b=np.array([8,3,8,9])

task2(a,b)

# Marker	Description

# 'o'	Circle	
# '*'	Star	
# '.'	Point	
# ','	Pixel	
# 'x'	X	
# 'X'	X (filled)	
# '+'	Plus	
# 'P'	Plus (filled)	
# 's'	Square	
# 'D'	Diamond	
# 'd'	Diamond (thin)	
# 'p'	Pentagon	
# 'H'	Hexagon	
# 'h'	Hexagon	
# 'v'	Triangle Down	
# '^'	Triangle Up	
# '<'	Triangle Left	
# '>'	Triangle Right	
# '1'	Tri Down	
# '2'	Tri Up	
# '3'	Tri Left	
# '4'	Tri Right	
# '|'	Vline	
# '_'	Hline

## Format Strings fmt
# This parameter is also called fmt, and is written with this syntax:
# marker|line|color

# Mark each point with a circle-dotted-red

def task3(yaxis):
    
    plt.plot(yaxis,"o:r")
    plt.show()
    
yaxis=np.array([6,9,2,7])

task3(yaxis)

# Line Reference
# Line Syntax	Description
# '-'	Solid line	
# ':'	Dotted line	
# '--'	Dashed line	
# '-.'	Dashed/dotted line

# Note: If you leave out the line value in the fmt parameter, no line will be plotted.

## Color Reference
# Color Syntax Description
# 'r'	Red	
# 'g'	Green	
# 'b'	Blue	
# 'c'	Cyan	
# 'm'	Magenta	
# 'y'	Yellow	
# 'k'	Black	
# 'w'	White

## Marker Size - which is represent as ms 
## Marker Edge Colour - which represent as "mec" or "markeredgecolor"
#3 Marker Face Colour - which represnt as "mfc" or "markerfacecolor"

# Set the size of the markers to 20 - edge colour to green - face colour to yellow:

def task4(xaxis):
    
    plt.plot(xaxis, "o--k", ms=20, mfc="y", mec="g")
    plt.show()
    
xaxis=np.array([5,9,3,4])

task4(xaxis)