# Matplotib
# Matplotlib is a low level graph plotting library bwhich servers as data visulaisation.

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Pyplot
# Most of the Matplotlib utilities lies under the pyplot submodule, 
# and are usually imported under the plt alias

#Draw a line in a diagram from position (0,0) to position (6,250):

def task1(xpoints,ypoints):
    
    plt.plot(xpoints,ypoints)
    plt.show()
    
xpoints=np.array([0,6])
ypoints=np.array([0,250])

task1(xpoints,ypoints)


## Plotting x and y points

# The plot() function is used to draw points (markers) in a diagram.
# By default, the plot() function draws a line from point to point.
# If we need to plot a line from (1, 3) to (8, 10), 
# we have to pass two arrays [1, 8] and [3, 10] to the plot function.


# Draw a line in a diagram from position (1, 3) to position (8, 10):

def task2(a,b):
    
    plt.plot(a,b)
    plt.show()
    
a=np.array([1,8])
b=np.array([3,10])

task2(a,b)

## Plotting Without Line
# To plot only the markers, you can use shortcut string notation parameter 'o', which means 'rings'.

# Draw two points in the diagram, one at position (1, 3) and one in position (8, 10):

def task3(x,y):
    
    plt.plot(x,y,"o")
    plt.show()
    
x=np.array([1,8])
y=np.array([3,10])

task3(x,y)

## Multiple Points
# You can plot as many points as you like, just make sure you have the same number of points in both axis.

# Draw a line in a diagram from position (1, 3) to (2, 8) then to (6, 1) and finally to position (8, 10):

def task4(xaxis,yaxis):
    
    plt.plot(xaxis,yaxis)
    plt.show()
    
xaxis=np.array([1,2,6,8])
yaxis=np.array([3,8,1,10])

task4(xaxis,yaxis)

## Default X-Points
# If we do not specify the points on the x-axis, they will get the default values 0, 1, 2, 3 etc., 
# depending on the length of the y-points.

# Plotting without x-points:

def task5(known):
    
    plt.plot(known)
    plt.show()
    
known=np.array([3, 8, 1, 10, 5, 7])

task5(known)