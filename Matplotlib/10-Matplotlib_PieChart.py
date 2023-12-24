import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

## Creating Pie Charts
# With Pyplot, you can use the pie() function to draw pie charts:

def pie1(a):
    
    plt.pie(a)
    plt.show()
    
a=np.array([25,35,25,15])

pie1(a)

# As you can see the pie chart draws one piece (called a wedge)
# By default the plotting of the first wedge starts from the x-axis and moves counterclockwise:


## Labels
# The label parameter must be an array with one label for each wedge:

# A simple pie chart:

def pie2(a):
    
    mylabels=np.array(["TCS","CTS","HCL","INFOSYS"])
    plt.pie(a, labels=mylabels)
    plt.show()
    
a=np.array([25,35,25,15])

pie2(a)

## Explode
# Maybe you want one of the wedges to stand out? The explode parameter allows you to do that.

# Pull the "TCS" wedge 0.2 from the center of the pie:

def pie3(a):
    
    mylabels=np.array(["TCS","CTS","HCL","INFOSYS"])
    myexplode=np.array([0.2,0,0,0])
    plt.pie(a, labels=mylabels, explode=myexplode)
    plt.show()
    
a=np.array([25,35,25,15])

pie3(a)

## Shadow
# Add a shadow to the pie chart by setting the shadows parameter to True:

# Add a shadow:

def pie4(a):
    
    mylabels=np.array(["TCS","CTS","HCL","INFOSYS"])
    myexplode=np.array([0.2,0,0,0])
    plt.pie(a, labels=mylabels, explode=myexplode, shadow=True)
    plt.show()
    
a=np.array([25,35,25,15])

pie4(a)

## Legend
# To add a list of explanation for each wedge, use the legend() function:

# Add a legend:

def pie5(a):
    
    mylabels=np.array(["TCS","CTS","HCL","INFOSYS"])
    myexplode=np.array([0.2,0,0,0])
    plt.pie(a, labels=mylabels, explode=myexplode, shadow=True)
    plt.legend()
    plt.show()
    
    
a=np.array([25,35,25,15])

pie5(a)

## Legend With Header
# To add a header to the legend, add the title parameter to the legend function.

# Add a legend with a header:
    
def pie6(a):
    
    mylabels=np.array(["TCS","CTS","HCL","INFOSYS"])
    myexplode=np.array([0.2,0,0,0])
    plt.pie(a, labels=mylabels, explode=myexplode, shadow=True)
    plt.legend(title="Companies")
    plt.show()
    
    
a=np.array([25,35,25,15])

pie6(a)

## Start Angle
# As mentioned the default start angle is at the x-axis, but you can change the start angle by specifying a startangle parameter.
# The startangle parameter is defined with an angle in degrees, default angle is 0:

# Start the first wedge at 90 degrees:

def pie7(a):
    
    mylabels=np.array(["TCS","CTS","HCL","INFOSYS"])
    myexplode=np.array([0.2,0,0,0])
    plt.pie(a, labels=mylabels, explode=myexplode, shadow=True, startangle=90)
    plt.legend(title="Companies")
    plt.show()
    
    
a=np.array([25,35,25,15])

pie7(a)

## Colors
# You can set the color of each wedge with the colors parameter.

# Specify a new color for each wedge:

def pie7(a):
    
    mylabels=np.array(["TCS","CTS","HCL","INFOSYS"])
    myexplode=np.array([0.2,0,0,0])
    mycolors=np.array(["black", "hotpink", "b", "#4CAF50"])
    plt.pie(a, labels=mylabels, explode=myexplode, shadow=True, startangle=90, colors=mycolors)
    plt.legend(title="Companies")
    plt.show()
    
    
a=np.array([25,35,25,15])

pie7(a)