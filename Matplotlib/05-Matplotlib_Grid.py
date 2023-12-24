import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

## Adding Grid Lines to a Plot
# With Pyplot, you can use the grid() function to add grid lines to the plot.

# Add grid lines to the plot:

def grid1(a,b):
    
    plt.plot(a,marker="o",ls=":")
    plt.plot(b,marker="*",ls="--")
    plt.title("Students")
    plt.xlabel("Boys")
    plt.ylabel("Girls")
    plt.grid()
    
    plt.show()
    
a=np.array([34,98,56,87])
b=np.array([76,34,87,23])

grid1(a,b)

# Display only grid lines for the x-axis:

def gridx(a,b):
    
    plt.plot(a,marker="o",ls=":",c="r")
    plt.plot(b,marker="*",ls="--",c="y")
    plt.title("Students")
    plt.xlabel("Boys")
    plt.ylabel("Girls")
    plt.grid(axis="x")
    
    plt.show()
    
a=np.array([34,98,56,87])
b=np.array([76,34,87,23])

gridx(a,b)

# Display only grid lines for the y-axis:

def gridy(a,b):
    
    plt.plot(a,marker="o",ls=":",c="r",ms=5,mec="k",mfc="m")
    plt.plot(b,marker="*",ls="--",c="y",ms=10,mec="k",mfc="m")
    plt.title("Students")
    plt.xlabel("Boys")
    plt.ylabel("Girls")
    plt.grid(axis="x")
    
    plt.show()
    
a=np.array([34,98,56,87])
b=np.array([76,34,87,23])

gridy(a,b)

## Set Line Properties for the Grid
# You can also set the line properties of the grid, like this: grid(color = 'color', linestyle = 'linestyle', linewidth = number).

# Set the line properties of the grid:

def gridp(a,b):
    
    plt.plot(a,marker="o",ls=":",c="r",ms=5,mec="k",mfc="m")
    plt.plot(b,marker="*",ls="--",c="y",ms=10,mec="k",mfc="m")
    plt.title("Students")
    plt.xlabel("Boys")
    plt.ylabel("Girls")
    plt.grid(ls="--",lw=1,c="g")
    
    plt.show()
    
a=np.array([34,98,56,87])
b=np.array([76,34,87,23])

gridp(a,b)