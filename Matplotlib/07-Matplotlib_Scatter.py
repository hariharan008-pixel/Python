import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Creating Scatter Plots
# With Pyplot, you can use the scatter() function to draw a scatter plot.

# A simple scatter plot:

def scat1(a,b):
    
    plt.scatter(a,b)
    plt.xlabel("How old the car")
    plt.ylabel("Speed of the car")
    plt.show()
    
a=np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
b=np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])

scat1(a,b)

# Draw two plots on the same figure:

def scat2(a,b,c,d):
    
    plt.scatter(a,b)
    
    plt.scatter(c,d)
    
    plt.xlabel("How old the car")
    plt.ylabel("Speed of the car")
    plt.show()
    
a=np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
b=np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
c=np.array([2,2,8,1,15,8,12,9,7,3,11,4,7,14,12])
d=np.array([100,105,84,105,90,99,90,95,94,100,79,112,91,80,85])

scat2(a,b,c,d)

## Size
# You can change the size of the dots with the s argument.
# Just like colors, make sure the array for sizes has the same length as the arrays for the x- and y-axis:

# Set your own size for the markers:

def scat3(x,y):
    
    size=np.array([20,50,100,200,500])
    plt.scatter(x,y,s=size)
    plt.show()
    
x=np.array([11,22,65,34,89])
y=np.array([65,98,34,78,56])

scat3(x,y)

## Alpha
# You can adjust the transparency of the dots with the alpha argument.
# Just like colors, make sure the array for sizes has the same length as the arrays for the x- and y-axis:

# Set your own size for the markers:

def scat4(m,n):
    
    size=np.array([20,50,100,200,500])
    plt.scatter(m,n,s=size,alpha=0.5)
    plt.show()
    
m=np.array([11,22,65,34,89])
n=np.array([65,98,34,78,56])

scat4(m,n)

## Colors
# You can set your own color for each scatter plot with the color or the c argument:

# Set your own color of the markers:

def scat5(i,j,k,l):
    
    plt.scatter(i,j, c="hotpink")
    
    plt.scatter(k,l, c="yellow")
    
    plt.xlabel("How old the car")
    plt.ylabel("Speed of the car")
    plt.show()
    
i=np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
j=np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
k=np.array([2,2,8,1,15,8,12,9,7,3,11,4,7,14,12])
l=np.array([100,105,84,105,90,99,90,95,94,100,79,112,91,80,85])

scat5(i,j,k,l)

# Color Each Dot
# You can even set a specific color for each dot by using an array of colors as value for the c argument:

# Note: You cannot use the color argument for this, only the c argument.

def scat6(e,f):
    
    color=np.array(["red","green","blue","yellow","pink","black","orange","purple","beige","brown","gray","cyan","magenta"])
    plt.scatter(e,f, c=color)
    
    plt.xlabel("How old the car")
    plt.ylabel("Speed of the car")
    plt.show()
    
e=np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
f=np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])

scat6(e,f)

## Combine Color Size and Alpha

# Create random arrays with 100 values for x-points, y-points, colors and sizes:

def scat7(a,b):
    
    sizes=np.random.randint(100, size=(100))
    colors=np.random.randint(100, size=(100))
    plt.scatter(a,b, s=sizes, c=colors, alpha= 1)
    plt.title("Test - Scatter Plot")
    plt.xlabel("Efforts")
    plt.ylabel("Results")
    
    plt.show()
    
a=np.random.randint(100, size=(100))
b=np.random.randint(100, size=(100))

scat7(a,b)