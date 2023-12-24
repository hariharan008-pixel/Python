import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

## Label
# With Pyplot, you can use the xlabel() and ylabel() functions to set a label for the x- and y-axis.

# Add labels to the x- and y-axis:

def task1(a,b):
    
    plt.plot(a)
    plt.plot(b)
    plt.xlabel("Number of male athlete")
    plt.ylabel("Number of female athlete")
    plt.show()
    
a=np.array([76,34,98,56])
b=np.array([65,98,23,34])

task1(a,b)

## Create a Title for a Plot
#With Pyplot, you can use the title() function to set a title for the plot.

# Add a plot title and labels for the x- and y-axis:

def task2(x,y):
    
    plt.plot(x)
    plt.plot(y)
    plt.title("Spartans Gym")
    plt.xlabel("Number of male")
    plt.ylabel("Number of female")
    plt.show()
    
x=np.array([76,34,98])
y=np.array([65,98,23])

task2(x,y)

## Font Properties for Title and Labels:
# You can use the fontdict parameter in xlabel(), ylabel(), and title() to set font properties for the title and labels.

## Location for Title:
#You can use the loc parameter in title() to position the title.
#Legal values are: 'left', 'right', and 'center'. Default value is 'center'.


# Set font properties and loc for the title and labels:

def task3(x,y):
    
    font1 = {'family':'serif','color':'blue','size':20}
    font2 = {'family':'serif','color':'darkred','size':15}

    plt.plot(x)
    plt.plot(y)
    plt.title("Spartans Gym", fontdict=font1, loc="left")
    plt.xlabel("Number of male", fontdict=font2)
    plt.ylabel("Number of female", fontdict=font2)
    plt.show()
    
x=np.array([76,34,98])
y=np.array([65,98,23])

task3(x,y)

