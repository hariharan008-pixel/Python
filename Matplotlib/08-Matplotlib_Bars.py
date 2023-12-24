import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

## Matplotlib Bars
# Creating Bars
# With Pyplot, you can use the bar() function to draw bar graphs:

# Draw 4 bars:

def bar1(a,b):
    
    plt.bar(a,b)
    plt.show()
    
a=np.array(["A","B","C","D"])
b=np.array([20,40,60,80])

bar1(a,b)

## Horizontal Bars
# If you want the bars to be displayed horizontally instead of vertically, use the barh() function:

# Draw 4 horizontal bars:

def bar2(x,y):
    
    plt.barh(x,y)
    plt.show()
    
x=np.array(["A","B","C","D"])
y=np.array([20,40,60,80])

bar2(x,y)

## Bar Color
# The bar() and barh() take the keyword argument color to set the color of the bars:

# Draw 4 red bars:

def bar3(c,d,e,f):
    
    plt.bar(c,d, color="red")
    plt.bar(e,f, color="yellow")
    plt.show()
    
c=np.array(["X","Y","Z","A","B"])
d=np.array([90,58,23,56,21])

e=np.array(["J","D","S","H","V"])
f=np.array([45,54,76,98,67])

bar3(c,d,e,f)

## Bar Width
# The bar() takes the keyword argument width to set the width of the bars:

# Draw 4 very thin bars:

def bar4(h,b):
    
    plt.bar(h,b, width=0.4)             # The default width value is 0.8 
    plt.show()
    
h=np.array([76,84,53,65])
b=np.array([87,34,76,54])

bar4(h,b)

## Bar Height
# The barh() takes the keyword argument height to set the height of the bars:

# Draw 4 very thin bars:

def bar5(h,b):
    
    plt.barh(h,b, height=0.4)             # The default height value is 0.8 
    plt.show()
    
h=np.array([76,84,53,65])
b=np.array([87,34,76,54])

bar5(h,b)