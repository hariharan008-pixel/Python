import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

## Linestyle
# You can use the keyword argument "linestyle", or shorter "ls", to change the style of the plotted line:

# Use a dotted line:

def task1(xaxis):
    
    plt.plot(xaxis, ls="dotted")   # ls=":"
    plt.show()
    
xaxis=np.array([9,3,7,4])

task1(xaxis)

# Use a dashed line:

def task2(yaxis):
    
    plt.plot(yaxis, ls="dashed")   # ls="--"
    plt.show()

yaxis=np.array([9,3,7,4])

task2(yaxis)

# Line Styles
# You can choose any of these styles:

# 'solid' 	'-'	
# 'dotted'	':'	
# 'dashed'	'--'	
# 'dashdot'	'-.'

## Line Width
# You can use the keyword argument linewidth or the shorter lw to change the width of the line.
# The value is a floating number, in points

# Plot with a 20.5pt wide line:

def task3(a):
    
    plt.plot(a, lw=20.5)
    plt.show()
    
a=np.array([98,34,87,45,75])

task3(a)

## Line Color
# You can use the keyword argument color or the shorter c to set the color of the line:

# Set the line color to red:

def task4(z):
    
    plt.plot(z,c="r")
    plt.show()
    
z=np.array([45,98,56])

task4(z)

## Multiple Lines
# You can plot as many lines as you like by simply adding more plt.plot() functions:

def multiline(a,b):
    
    plt.plot(a,marker="D",mec="k",mfc="r",ls="--",c="r")
    plt.plot(b,marker="H",mec="k",mfc="g",ls="--",c="g")
    plt.show()
    
a=np.array([3, 8, 1, 10])
b=np.array([6, 2, 7, 11])

multiline(a,b)